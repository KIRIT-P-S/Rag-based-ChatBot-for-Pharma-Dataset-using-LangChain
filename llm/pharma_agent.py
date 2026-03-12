import google.generativeai as genai
import os

class PharmaAgent:

    def __init__(self):

        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, query, context):

        prompt = f"""
You are a pharmaceutical expert assistant.

Answer only using the provided context.

Context:
{context}

Question:
{query}
"""

        response = self.model.generate_content(prompt)

        return response.text