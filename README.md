# TruthAI 🔍🧠

AI-powered image forensic analysis system to detect whether an image is **REAL** or **AI-generated / Deepfake** using:

* Hugging Face Deepfake Detection Model
* Google Gemini Vision Analysis
* LangChain Tools
* PyTorch & Transformers

---

# 🚀 Features

✅ Deepfake image detection
✅ AI-generated image analysis
✅ Gemini forensic reasoning
✅ Multimodal image understanding
✅ LangChain tool integration
✅ Base64 image processing
✅ Structured AI forensic report

---

# 🛠 Tech Stack

* Python
* LangChain
* Google Gemini
* Hugging Face Transformers
* PyTorch
* PIL (Pillow)
* Pydantic

---

# 📂 Project Structure

```bash
TruthAI/
│
├── image_tool.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/TruthAI.git
cd TruthAI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_google_gemini_api_key
HF_TOKEN=your_huggingface_token
```

⚠️ Never upload `.env` to GitHub.

---

# ▶️ Run Project

Place your image inside the project folder.

Example:

```bash
test.jpg
```

Run:

```bash
python image_tool.py
```

---

# 🧠 How It Works

```text
Input Image
    ↓
Base64 Conversion
    ↓
Deepfake Detection Model
    ↓
Prediction Probabilities
    ↓
Gemini Vision Analysis
    ↓
Final REAL / FAKE Report
```

---

# 📊 Example Output

```python
{
    "deepfake_prediction": {
        "real": 0.82,
        "fake": 0.18
    },

    "gemini_analysis": "The image appears authentic with low probability of AI manipulation..."
}
```

---

# 📦 Required Packages

```bash
pip install torch torchvision torchaudio
pip install transformers
pip install pillow
pip install python-dotenv
pip install langchain
pip install langchain-google-genai
```

---

# 🧪 Model Used

Hugging Face Model:

`prithivMLmods/Deepfake-Detect-Siglip2`

---

# ⚠️ Disclaimer

This project provides probabilistic analysis only.

AI-generated image detection is not always 100% accurate and should not be considered definitive forensic proof.

---

# 👨‍💻 Author

Developed by Afjal

---

# 📜 License

MIT License
