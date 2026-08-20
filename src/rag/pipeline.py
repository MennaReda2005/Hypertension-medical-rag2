from src.retrieval.retriever import retrieve_documents
from src.generation.llm import generate_answer


def ask_medical_question(question: str) -> str:

    # Retrieve relevant medical information
    documents = retrieve_documents(question)

    # Generate final answer
    answer = generate_answer(
        question=question,
        documents=documents
    )

    return answer