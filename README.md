# 🩺 Hypertension Medical RAG

> **Evidence-Based Medical Question Answering System for Hypertension**

An AI-powered **Retrieval-Augmented Generation (RAG)** system designed to answer hypertension-related medical questions using a curated collection of medical documents.

The system combines **semantic search, document retrieval, context-aware generation, and confidence checking** to provide grounded answers based on the available medical knowledge base.

---

## 🚀 Overview

Medical information requires accuracy, reliable evidence, and controlled generation.

**Hypertension Medical RAG** implements a complete Retrieval-Augmented Generation pipeline:

```text
User Question
      ↓
Question Processing
      ↓
Semantic Retrieval
      ↓
Relevant Medical Chunks
      ↓
Context Construction
      ↓
LLM Generation
      ↓
Confidence / Relevance Check
      ↓
Evidence-Based Answer

The system operates within a defined hypertension knowledge scope and avoids generating unsupported answers when sufficient evidence cannot be retrieved.

---

✨ Key Features

- 🩺 Hypertension-focused medical question answering
- 🔎 Semantic document retrieval
- 🧠 Embedding-based similarity search
- 📚 Retrieval-Augmented Generation
- ✂️ Recursive Character Text Splitting
- 🗃️ ChromaDB vector database
- 🤖 Gemini-powered answer generation
- 🛡️ Confidence and relevance checking
- 🎯 Scope-aware question handling
- 📖 Evidence-grounded responses
- 💬 Interactive Streamlit interface
- 🔐 Secure environment variable management

---

🏗️ System Architecture

                 ┌──────────────────┐
                 │   Medical PDFs   │
                 └────────┬─────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Document Ingestion │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Recursive Chunking │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     Embeddings     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  Chroma Vector DB  │
                └─────────┬──────────┘
                          │
                          │
User Question ────────────┤
                          ▼
                ┌────────────────────┐
                │ Semantic Retrieval │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Relevant Context   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │       Gemini       │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Confidence Check   │
                └─────────┬──────────┘
                          │
                          ▼
                   Final Answer

---

🔄 RAG Pipeline

1. Document Ingestion

Medical documents are loaded and processed before being stored in the knowledge base.

Medical Documents
       ↓
Document Loading
       ↓
Text Extraction
       ↓
Text Cleaning
       ↓
Chunking
       ↓
Embedding Generation
       ↓
Vector Database

---

2. Document Chunking

The system uses Recursive Character Text Splitting.

Instead of blindly cutting documents at arbitrary positions, the splitter recursively attempts to preserve meaningful text boundaries.

This helps maintain contextual relationships within medical content.

Medical Document
       ↓
Paragraphs
       ↓
Sentences
       ↓
Contextual Chunks

---

3. Embeddings

Each document chunk is converted into a numerical vector representation using an embedding model.

Text Chunk
    ↓
Embedding Model
    ↓
Vector Representation

The user's query is also converted into an embedding, allowing the system to identify semantically similar medical content.

---

4. Vector Database

The generated embeddings are stored in ChromaDB.

The vector database allows efficient retrieval of chunks that are semantically related to the user's question.

Query
  ↓
Query Embedding
  ↓
Similarity Search
  ↓
Top Relevant Chunks

---

🔎 Retrieval

The retrieval component searches the vector database for the most relevant medical chunks.

The retrieved context is then passed to the generation stage.

This helps ground the LLM response in the project's medical knowledge base rather than relying solely on the model's internal knowledge.

---

🤖 Generation

After retrieving relevant evidence, the system constructs a context-aware prompt for the LLM.

User Question
      +
Retrieved Medical Context
      ↓
Gemini
      ↓
Grounded Answer

The model is instructed to prioritize the retrieved evidence and avoid unsupported claims.

---

🛡️ Confidence & Relevance Check

The system includes a confidence/relevance checking layer.

Before returning a response, the system checks whether sufficient relevant information was retrieved.

If the available context is insufficient, the system can avoid confidently generating an unsupported medical answer.

This provides an additional safety layer for the medical RAG pipeline.

---

🎯 Scope Control

The system is designed around a defined hypertension knowledge scope.

✅ In-Scope Examples

What is hypertension?

What are the symptoms of high blood pressure?

What are common risk factors for hypertension?

How is hypertension diagnosed?

What lifestyle changes can help control blood pressure?

❌ Out-of-Scope Examples

What is the capital of France?

How do I train a computer vision model?

What is the weather today?

The system should avoid treating unrelated questions as medical questions supported by the hypertension knowledge base.

---

🖥️ User Interface

The project includes an interactive Streamlit interface.

Users can:

- Enter a medical question
- Retrieve relevant information
- Generate an evidence-grounded answer
- Interact with the RAG system through a web interface

Example:

User
 ↓
Medical Question
 ↓
Retriever
 ↓
Relevant Medical Chunks
 ↓
Gemini
 ↓
Confidence Check
 ↓
Final Answer

---

📁 Project Structure

Hypertension-medical-rag2/
│
├── data/
│   └── documents/
│       └── medical documents
│
├── src/
│   ├── ingestion/
│   │   └── ingest.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── generation/
│   │   └── llm.py
│   │
│   └── rag/
│       └── pipeline.py
│
├── vectorstore/
│   └── chroma_db/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── app.py

«Note: ".env", generated vector stores, cache files, and other sensitive/generated artifacts should not be committed to GitHub.»

---

⚙️ Technology Stack

Component| Technology
Language| Python
RAG Framework| LangChain
Vector Database| ChromaDB
Embeddings| Sentence Transformers
LLM| Google Gemini
Interface| Streamlit
Document Processing| PDF/Text Processing
Version Control| Git & GitHub

---

🔧 Installation

1. Clone the Repository

git clone https://github.com/MennaReda2005/Hypertension-medical-rag2.git
cd Hypertension-medical-rag2

2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

---

🔐 Environment Variables

Create a ".env" file in the project root:

GOOGLE_API_KEY=your_google_api_key_here

⚠️ Never commit the real API key to GitHub.

The ".env" file should remain in ".gitignore".

---

📚 Medical Documents

Place the medical documents used by the system inside:

data/documents/

The ingestion pipeline processes the documents, splits them into chunks, generates embeddings, and stores them in ChromaDB.

---

▶️ Running the Application

Start the Streamlit application:

streamlit run app.py

Then open the local Streamlit URL displayed in the terminal.

---

🧪 Testing

The system can be tested using different question categories.

1. In-Scope Medical Question

What are the common risk factors for hypertension?

Expected behavior:

Retrieve relevant medical evidence
        ↓
Generate an evidence-grounded answer

2. Unrelated Medical Question

What are the symptoms of asthma?

Expected behavior:

Question outside the hypertension knowledge scope
        ↓
Avoid unsupported retrieval/generation

3. General Non-Medical Question

What is machine learning?

Expected behavior:

Question outside the system scope
        ↓
Reject / redirect appropriately

---

🧠 Why RAG?

A standard LLM may generate answers using knowledge learned during pretraining.

For medical applications, this can introduce risks such as:

- Unsupported claims
- Hallucinations
- Outdated information
- Lack of traceable evidence

RAG introduces an external retrieval step:

Traditional LLM

Question
   ↓
LLM
   ↓
Answer

Medical RAG

Question
   ↓
Retrieve Medical Evidence
   ↓
Relevant Context
   ↓
LLM
   ↓
Grounded Answer

This architecture helps keep responses aligned with the project's available medical knowledge.

---

🔒 Medical Safety

This project is an educational and research-oriented AI system.

It is not intended to replace professional medical advice, diagnosis, or treatment.

The system should be used as an information-support tool rather than as a clinical decision-making system.

Users should consult qualified healthcare professionals for personal medical decisions.

---

🚧 Current Limitations

- Response quality depends on the quality of the medical documents.
- Retrieval errors can affect final answers.
- The system is limited to its available knowledge base.
- LLMs can still produce incorrect or incomplete information.
- Confidence checking is not equivalent to clinical validation.
- The current system is not a certified medical device.

---

🚀 Future Improvements

🔹 Advanced Retrieval

- Hybrid search combining semantic and keyword retrieval
- Re-ranking retrieved chunks
- Metadata-aware filtering
- Query expansion
- Multi-query retrieval

🔹 Medical Knowledge

- Expand the knowledge base with additional authoritative guidelines
- Add guideline versioning
- Improve document preprocessing
- Add source-level metadata

🔹 Evaluation

Implement a dedicated RAG evaluation framework including:

- Precision@K
- Recall@K
- MRR
- Context Relevance
- Faithfulness
- Answer Relevance
- Retrieval Latency

🔹 Safety

Future versions can include:

- Stronger medical guardrails
- Explicit uncertainty detection
- Contradiction detection
- Source attribution
- High-risk question detection
- Human-in-the-loop review

🔹 User Experience

- Conversation history
- Source/document display
- Retrieved chunk visualization
- Confidence indicators
- Arabic/English multilingual support
- Improved medical dashboard

---

📊 Evaluation Strategy

A robust evaluation pipeline can be organized into three levels:

                 RAG Evaluation
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   Retrieval       Generation       Safety
   Evaluation      Evaluation       Evaluation
        │              │              │
   Precision@K      Faithfulness     Scope
   Recall@K         Relevance        Guardrails
   MRR              Accuracy         Abstention

This separates retrieval quality from generation quality, making it easier to identify where errors originate.

---

🔬 Future Research Direction

The project can be extended from a basic medical RAG system into a more advanced evidence-backed medical reasoning architecture:

Patient / User Query
        ↓
Question Understanding
        ↓
Evidence Retrieval
        ↓
Evidence Ranking
        ↓
Knowledge Synthesis
        ↓
Safety & Confidence Checks
        ↓
Evidence-Grounded Response

This provides a foundation for building more reliable and transparent medical AI systems.

---

📌 Project Goals

The main goals of this project are to:

- Build a domain-specific medical RAG system
- Improve retrieval of relevant hypertension information
- Ground LLM responses in external medical evidence
- Reduce unsupported generation
- Introduce scope and confidence controls
- Provide an accessible user interface
- Establish a foundation for future medical AI evaluation

---

## 🌐 Live Demo

🔗 **[Try the Hypertension Medical RAG System](https://hypertension-medical-rag2-fqsuvmgpphcgkqjm4qttqc.streamlit.app/)**

Experience the system directly through the deployed Streamlit application.


👩‍💻 Author

Menna Reda

AI Engineer | Machine Learning | Deep Learning | NLP | Generative AI

GitHub: "@MennaReda2005" (https://github.com/MennaReda2005)

---

⭐ Acknowledgment

This project was developed as an educational/research implementation of Retrieval-Augmented Generation for medical question answering, with a focus on hypertension-related information.



⭐ If you find this project useful, consider giving the repository a star!
