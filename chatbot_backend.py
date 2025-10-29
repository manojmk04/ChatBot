"""
chatbot_backend.py
LangChain LCEL with Ollama + RunnableWithMessageHistory (Fixed Memory)
"""

import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# --- LOAD ENV ---
load_dotenv()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:3.8b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

# --- LLM ---
llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_HOST,
    temperature=TEMPERATURE
)

# --- FIXED PROMPT WITH CHAT HISTORY ---
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant who remembers context who answers very precisely with exact response briefly instead of long texts."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{question}")
])

# --- PARSER ---
parser = StrOutputParser()

# --- CHAIN ---
chain = prompt | llm | parser

# --- STORE FOR SESSIONS ---
store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    """Return per-session chat history."""
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# --- WRAP WITH MESSAGE HISTORY ---
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history"
)

# --- CHATBOT RESPONSE FUNCTION ---
def chatbot_response(question: str, session_id: str) -> str:
    """Respond with memory retention."""
    result = chain_with_history.invoke(
        {"question": question},
        config={"configurable": {"session_id": session_id}}
    )
    return result

# --- TEST ---
if __name__ == "__main__":
    sid = "demo_session"
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chatbot_response(user_input, sid)
        print(f"Bot: {reply}")
