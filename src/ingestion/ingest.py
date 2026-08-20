from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


DATA_PATH = Path("data/documents")
VECTOR_PATH = "vectorstore/chroma_db"


def load_documents():

    documents = []

    for pdf_file in DATA_PATH.glob("*.pdf"):

        loader = PyPDFLoader(str(pdf_file))

        docs = loader.load()

        documents.extend(docs)

    return documents


def create_vector_database():

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_PATH
    )

    print("Medical documents indexed successfully.")


if __name__ == "__main__":
    create_vector_database()