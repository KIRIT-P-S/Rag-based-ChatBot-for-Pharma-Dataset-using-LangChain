# Rag-based-ChatBot-for-Pharma-Dataset-using-LangChain
# Pharma RAG Chatbot

An AI-powered **Pharmaceutical Question Answering System** built using **Retrieval-Augmented Generation (RAG)**.  
The chatbot retrieves relevant information from pharmaceutical PDF documents and generates intelligent responses using modern AI technologies.

---

## Features

- 📄 PDF-based pharmaceutical knowledge retrieval
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered answer generation
- ⚡ Fast backend API
- 💬 Interactive chat UI
- 🧠 Context-aware responses
- 🧩 Modular and extensible architecture

---

## 🏗️ System Architecture


User Query
│
▼
FastAPI Backend
│
▼
Vector Search (Chroma DB)
│
▼
Relevant Context Retrieved
│
▼
Gemini LLM Generates Answer
│
▼
Response Returned to UI


---

## 🛠️ Tech Stack

| Component | Technology |
|----------|-------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| LLM | Google Gemini |
| Retrieval | LangChain |

---

## 📂 Project Structure


pharma_chatbot/
│
├── app.py
├── rag_pipeline.py
├── chat_ui.py
│
├── data/
│ └── pharma.pdf
│
├── ingestion/
│ └── ingest_pdf.py
│
├── retrieval/
│ └── retriever.py
│
├── llm/
│ └── pharma_agent.py
│
├── vector_db/
│
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/pharma_chatbot.git
cd pharma_chatbot
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Setup Environment Variables

Set your Google Gemini API key.

Windows

setx GOOGLE_API_KEY "your_api_key"

Linux / Mac

export GOOGLE_API_KEY="your_api_key"

Restart terminal after setting the key.

📥 PDF Ingestion

Convert your pharmaceutical PDF into embeddings and store them in the vector database.

python ingestion/ingest_pdf.py

Expected output:

Chunks created
Vector DB created successfully
PDF ingestion completed
▶️ Run Backend API

Start the FastAPI server.

uvicorn app:app --reload

Server runs at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
💬 Run Chat UI

Launch the Streamlit chat interface.

streamlit run chat_ui.py

The chatbot will open automatically in your browser.

🧪 Example Query
What are the uses of Paracetamol?

Example response:

Paracetamol is commonly used to treat mild to moderate pain and fever. 
It works by reducing the production of prostaglandins in the brain.
🔮 Future Improvements

📚 Multi-PDF ingestion

🧾 Citation highlighting from documents

🎙️ Voice-based assistant

💊 Drug interaction detection

🌐 Cloud deployment

📊 Medical knowledge graph integration

📜 License

MIT License

👨‍💻 Author

Developed as an AI-powered pharmaceutical information system using RAG architecture.
