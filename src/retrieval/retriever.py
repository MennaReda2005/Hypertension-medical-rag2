from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# =========================================================
# EMBEDDINGS
# =========================================================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================================================
# VECTOR DATABASE
# =========================================================

vectorstore = Chroma(
    persist_directory="vectorstore/chroma_db",
    embedding_function=embeddings
)


# =========================================================
# RETRIEVAL
# =========================================================

def retrieve_documents(question: str):

    documents = vectorstore.similarity_search(
        question,
        k=3
    )

    return documents