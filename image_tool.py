# image_analysis_tool.py


from pydantic import BaseModel
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import google.generativeai as genai
import torch
import io
import base64

from langchain_core.tools import tool


from langgraph.prebuilt import ToolNode
import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# Load Deepfake Model Once
# -------------------------------
model_name = "prithivMLmods/Deepfake-Detect-Siglip2"
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# -------------------------------
# Configure Gemini
# -------------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")


# -------------------------------
# Pydantic Schema
# -------------------------------
class ImageAnalysisInput(BaseModel):
    image_base64: str  # Image will be passed as base64


# -------------------------------
# Helper Functions
# -------------------------------
def deepfake_predict(image_pil):
    image = image_pil.convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1).squeeze().tolist()

    labels = model.config.id2label
    prediction = {labels[i]: float(probs[i]) for i in range(len(probs))}
    return prediction


def gemini_analyze(image_pil, prediction):

    buffer = io.BytesIO()
    image_pil.save(buffer, format="JPEG")
    img_bytes = buffer.getvalue()

    prompt = f"""
You are an AI image forensics expert.

Deepfake model probabilities:
{prediction}

Your tasks:
1. Conclude if image is REAL or FAKE.
2. Provide final_label, risk_level, summary, explanation.
3. Use cautious language.
"""

    response = gemini_model.generate_content(
        [
            prompt,
            {"mime_type": "image/jpeg", "data": img_bytes}
        ]
    )

    return response.text


# -------------------------------
# TOOL
# -------------------------------
@tool
def analyze_image_tool(input: ImageAnalysisInput):
    """Analyze image for deepfake and run Gemini forensic analysis."""

    # decode base64
    image_bytes = base64.b64decode(input.image_base64)
    image_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    prediction = deepfake_predict(image_pil)
    gemini_result = gemini_analyze(image_pil, prediction)

    return {
        "deepfake_prediction": prediction,
        "gemini_analysis": gemini_result
    }
