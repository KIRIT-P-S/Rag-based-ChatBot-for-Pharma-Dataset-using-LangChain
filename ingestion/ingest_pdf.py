import pytesseract
from pdf2image import convert_from_path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_scanned_pdf(pdf_path):

    images = convert_from_path(pdf_path)
    text = ""

    for img in images:
        text += pytesseract.image_to_string(img)

    return text


def ingest_pdf(pdf_path, persist_dir):

    text = extract_text_from_scanned_pdf(pdf_path)

    if not text.strip():
        print("Still no text extracted")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    docs = splitter.create_documents([text])

    print("Chunks created:", len(docs))

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )

    print("Vector DB created successfully")
    print("PDF ingestion completed")

if __name__ == "__main__":
    ingest_pdf("data/pharma.pdf", "vector_db")