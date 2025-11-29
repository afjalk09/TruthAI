import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langgraph_backend import chatbot
from langchain_core.messages import SystemMessage


SYSTEM_PROMPT = SystemMessage(content="""
You are an AI assistant with access to tools (web search, arxiv, wikipedia, duckduckgo, tavily).

Rules:
- Use tools only when needed.
- When you give your final answer, always:
  1) Mention which tools you used (if any).
  2) Reference the key sources (URLs or article titles) you relied on.
  3) Be honest if the evidence is weak or conflicting.
""")

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Show chat history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input = st.chat_input("type here")

if user_input:
    # Add user message
    st.session_state['message_history'].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    response = chatbot.invoke(
    {"messages": [
        SYSTEM_PROMPT,  # ✅ add your system prompt here

        # existing chat history conversion
        *[
            HumanMessage(content=m['content']) if m['role']=="user"
            else AIMessage(content=m['content'])
            for m in st.session_state['message_history']
        ]
    ]},
    config=CONFIG
)

    ai_message = response["messages"][-1].content
    if isinstance(ai_message, list):
        clean_text = ""
        for part in ai_message:
            if isinstance(part, dict) and part.get("type") == "text":
                clean_text += part.get("text", "")
            elif isinstance(part, str):
                clean_text += part
    else:
        clean_text = str(ai_message)




    # ADD AI MESSAGE CORRECTLY
    st.session_state['message_history'].append({
        "role": "assistant",
        "content": clean_text
    })

    with st.chat_message("assistant"):
        st.text(clean_text)
        
