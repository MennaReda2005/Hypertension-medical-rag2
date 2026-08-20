import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_answer(question, documents):

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are MediGuide AI, a medical information assistant.

Your task is to answer the user's question using ONLY the
medical information provided in the context below.

IMPORTANT RULES:

1. Do NOT copy the context word-for-word unless a specific
   medical term, name, number, dosage, or definition must be
   preserved exactly.

2. Understand the information first, then rewrite it naturally
   in clear, simple, human-friendly language.

3. Preserve the original medical meaning and important details.
   Do NOT change, exaggerate, or simplify information in a way
   that could make it medically inaccurate.

4. Do NOT add medical information, recommendations, diagnoses,
   treatments, or facts that are not supported by the context.

5. If the context does not contain enough information to answer
   the question, say clearly:
   "The available medical information does not provide enough
   information to answer this question."

6. Keep the answer focused on the user's question.

7. Use short paragraphs or bullet points when they make the
   answer easier to understand.

8. Do not mention "context", "documents", "retrieval", "RAG",
   or any technical system details in the final answer.

9. Do not start the answer with unnecessary phrases such as
   "According to the context" or "Based on the documents."

Medical Information:
{context}

User Question:
{question}

Now write a clear, natural, human-friendly answer while
preserving the medical meaning of the provided information.
"""

    response = llm.invoke(prompt)

    return response.content