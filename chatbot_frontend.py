"""
chatbot_frontend.py
Streamlit-based chat UI for Ollama-powered chatbot.
"""

import streamlit as st
import uuid
from chatbot_backend import chatbot_response, get_session_history

st.set_page_config(page_title="🤖 Chatbot", layout="centered")

# --- SESSION SETUP ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

session_id = st.session_state["session_id"]

st.title("🤖 Local Chatbot")
st.caption("Lets have a chat !!")

# --- DISPLAY PAST CHAT ---
chat_history = get_session_history(session_id)
for msg in chat_history.messages:
    if msg.type == "human":
        st.chat_message("user").markdown(msg.content)
    elif msg.type == "ai":
        st.chat_message("assistant").markdown(msg.content)

# --- USER INPUT ---
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatbot_response(user_input, session_id)
            st.markdown(response)