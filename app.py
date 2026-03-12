from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import PharmaRAG

app = FastAPI()

rag = PharmaRAG()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    answer = rag.run(query.question)
    return {"response": answer}

@app.get("/")
def root():
    return {"message": "Pharma RAG Chatbot API running"}