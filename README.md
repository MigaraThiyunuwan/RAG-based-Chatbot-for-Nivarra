# 🌴 RAG-based Chatbot for Nivarra

A **Retrieval-Augmented Generation (RAG)** powered chatbot that provides informative answers about **Nivarra**, a fictional island nation. The system uses LLaMA 3.1 with Ollama, HuggingFace embeddings, FAISS for retrieval, and a simple web interface built with Flask.

---

## 🧠 What is RAG?

**Retrieval-Augmented Generation (RAG)** is a method that enhances large language models by retrieving relevant context from an external knowledge base before generating a response. This allows the model to:

- Use up-to-date or domain-specific information
- Provide more factual and grounded responses
- Reduce hallucination and model limitations

---

## 🌽 About Nivarra

**Nivarra** is an *imaginary island nation* created using AI-generated content. The chatbot provides knowledge about:

- History, politics, and governance
- Climate, agriculture, and economy
- Culture, languages, and festivals
- Tourism, healthcare, and education

This makes it a great sandbox for exploring the power of RAG-based LLM applications.

---

## 🛠️ Tech Stack

- **LLM**: LLaMA 3.1 (via [Ollama](https://ollama.com))
- **Embeddings**: `BAAI/bge-small-en-v1.5` from HuggingFace
- **Vector Search**: FAISS
- **Backend**: Python + Flask
- **Frontend**: HTML/CSS (chat-style UI)
- **File Support**: `.txt` and `.pdf` for loading knowledge

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/MigaraThiyunuwan/RAG-based-Chatbot-for-Nivarra.git
cd nivarra-rag-chatbot
```

### 2. Install Requirements

Make sure you have Python 3.8+ and install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install Ollama & LLaMA 3.1

If you haven’t already:

```bash
# Install Ollama
https://ollama.com

# Pull LLaMA 3 model
ollama pull llama3.1
```

> Make sure Ollama is running in the background before you start the chatbot.

### 4. Add Your Knowledge Base

Place your text file (`data.txt`) or PDF (`island.pdf`) with content about Nivarra in the root folder.

### 5. Run the Web Application

```bash
python rag_server.py
python app.py
```

Visit the chatbot in your browser at:

```
http://localhost:5000
```

---



## 📁 Project Structure

```
nivarra-rag-chatbot/
🔍\ app.py               # Flask app for web UI
🔍\ RagLlm.py            # Embedding, retrieval, and response logic
🔍\ data.txt / island.pdf # Nivarra knowledge source
🔍\ templates/
🔍\ └── index.html       # Chat frontend
🔍\ static/
🔍\ └── style.css        # (Optional) UI styling
🔍\ requirements.txt
🔍\ README.md
```

---


## 📌 Disclaimer

> **Nivarra is a fictional island** created for experimental purposes using ChatGPT. This project demonstrates how RAG can improve domain-specific assistants with local LLMs.

---

## 🙌 Acknowledgments

- [Ollama](https://ollama.com) for LLM serving
- [HuggingFace](https://huggingface.co) for embedding models
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
- ChatGPT (for generating Nivarra content 😄)

---

## 💬 Contact

Want to collaborate or ask something?

📧 Reach out via [LinkedIn](https://www.linkedin.com/in/migara-thiyunuwan/)\
🐙 Or open an issue on the repo

---

