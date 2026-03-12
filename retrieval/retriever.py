from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

class PharmaRetriever:

    def __init__(self, persist_dir):

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings
        )

    def retrieve(self, query, k=5):

        docs = self.db.similarity_search(query, k=k)

        return docs