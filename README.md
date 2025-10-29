# 🤖 Chatbot – LangChain + Ollama + Streamlit

A fully local AI-powered chatbot built using **LangChain**, **LCEL**, and **Ollama** — featuring message history, configurable models, and a clean **Streamlit UI**.

Supports open-source models like **Gemma 3**, **Phi 3**, and **Mistral 7B**, running completely offline on your machine.

---

## 🚀 Features
- 🧠 Session-aware chat using `RunnableWithMessageHistory`
- ⚡ Local inference via Ollama (no API key needed)
- 💬 Streamlit frontend with dynamic message updates
- 🔄 Configurable model via `.env` file
- 🪶 Lightweight and modular 2-file design

---

## 🧩 Project Structure
```
chatbot_backend.py     # LangChain backend with Ollama + memory
chatbot_frontend.py    # Streamlit chat interface
.env                   # Environment variables (ignored in Git)
requirements.txt        # Python dependencies
.gitignore              # Ignore venv, .env, cache, etc.
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```
git clone https://github.com/manojmk04/ChatBot.git
cd ChatBot
```

### 2️⃣ Create a virtual environment
```
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file
```
OLLAMA_MODEL=phi3:3.8b
```

### 5️⃣ Start Ollama
```
ollama serve
```

*(Pull the model first if not already installed:)*
```
ollama pull phi3:3.8b
```

### 6️⃣ Run the chatbot
```
streamlit run chatbot_frontend.py
```

Then open the local URL shown (usually `http://localhost:8501`).

---

## 🧠 Switching Models
You can change the model anytime by editing your `.env` file:

```
OLLAMA_MODEL=gemma3:1b
# or
OLLAMA_MODEL=mistral:7b
# or
OLLAMA_MODEL=phi3:3.8b
```

Then rerun Streamlit to load the new model.

---

## 🧹 Clear Chat History
Click the “🧹 Clear Chat” button (if present in UI) or restart Streamlit to start a fresh session.

---
