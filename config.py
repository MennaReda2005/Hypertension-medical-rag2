import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

#OLLAMA_MODEL = os.getenv(
 #   "OLLAMA_MODEL",
#    "llama3.2:3b"
#)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "vectorstore/chroma_db"
)