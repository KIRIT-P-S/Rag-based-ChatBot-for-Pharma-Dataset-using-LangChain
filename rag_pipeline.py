from retrieval.retriever import PharmaRetriever
from llm.pharma_agent import PharmaAgent

class PharmaRAG:

    def __init__(self):

        self.retriever = PharmaRetriever("vector_db")
        self.agent = PharmaAgent()

    def run(self, query):

        docs = self.retriever.retrieve(query)

        context = "\n".join([doc.page_content for doc in docs])

        answer = self.agent.generate(query, context)

        return answer