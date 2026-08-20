🩺 Hypertension Medical RAG

«Evidence-Based Medical Question Answering System for Hypertension»

An AI-powered Retrieval-Augmented Generation (RAG) system designed to answer hypertension-related medical questions using a curated collection of medical documents.

The system combines semantic search, document retrieval, context-aware generation, and confidence checking to provide grounded answers based on the available medical knowledge base rather than relying only on the language model's internal knowledge.

---

🚀 Overview

Medical information requires accuracy, reliable evidence, and controlled generation.

Hypertension Medical RAG addresses this challenge by implementing a complete Retrieval-Augmented Generation pipeline:

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

The system is specifically designed to operate within a defined hypertension knowledge scope and avoid generating unsupported answers when sufficient evidence cannot be retrieved.

---

✨ Key Features

- 🩺 Hypertension-focused medical QA
- 🔎 Semantic document retrieval
- 🧠 Embedding-based similarity search
- 📚 Context-aware RAG pipeline
- ✂️ Recursive document chunking
- 🗃️ Chroma vector database
- 🤖 LLM-powered answer generation
- 🛡️ Confidence / relevance checking
- 🎯 Scope-aware question handling
- 📖 Evidence-grounded responses
- 💬 Interactive Streamlit interface
- 🔐 Environment-based API key management
- ⚡ Lightweight architecture suitable for local development

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
                │       LLM          │
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

Medical documents are loaded and processed before being inserted into the knowledge base.

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

The ingestion pipeline prepares the knowledge base for efficient semantic retrieval.

---

2. Document Chunking

The system uses Recursive Character Text Splitting.

Instead of blindly cutting the document at arbitrary positions, the splitter recursively attempts to preserve meaningful text boundaries.

This helps maintain contextual relationships inside medical content.

Medical Document
       ↓
Paragraphs
       ↓
Sentences
       ↓
Smaller Contextual Chunks

This approach provides a practical balance between:

- Context preservation
- Retrieval precision
- Chunk size
- LLM context limitations

---

3. Embeddings

Each document chunk is converted into a numerical vector representation using an embedding model.

Text Chunk
    ↓
Embedding Model
    ↓
Vector Representation

The same embedding space is used to represent the user's query, allowing the system to identify semantically similar medical content.

---

4. Vector Database

The generated embeddings are stored in ChromaDB.

The vector database allows the system to efficiently retrieve chunks that are semantically related to the user's question.

Query
  ↓
Query Embedding
  ↓
Similarity Search
  ↓
Top Relevant Chunks

---

🔎 Retrieval

The retrieval component searches the vector database for the most relevant chunks.

The retrieved context is then passed to the generation stage.

This prevents the LLM from answering solely from its pretrained knowledge and helps ground responses in the project's medical knowledge base.

---

🤖 Generation

After retrieving relevant evidence, the system constructs a context-aware prompt for the LLM.

Conceptually:

User Question
      +
Retrieved Medical Context
      ↓
LLM
      ↓
Grounded Answer

The model is instructed to prioritize the retrieved evidence and avoid unsupported claims.

---

🛡️ Confidence & Relevance Check

A key component of the system is the confidence/relevance checking layer.

Before returning a response, the system evaluates whether sufficient relevant information was retrieved.

If the available context is insufficient, the system can avoid confidently generating an unsupported medical answer.

This provides an additional safety layer for a medical-domain RAG application.

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

The project includes an interactive Streamlit interface that allows users to:

- Enter a medical question
- Retrieve relevant information
- Generate an evidence-grounded answer
- Interact with the RAG system through a simple web interface

Example interaction:

User:
What are the major risk factors for hypertension?

        ↓

Retriever:
Find relevant medical chunks

        ↓

LLM:
Generate answer using retrieved context

        ↓

System:
Return grounded response

---

📁 Project Structure

Hypertension-medical-rag2/
│
├── data/
│   └── documents/
│       └── medical documents
│
├── src/
│   │
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

«".env", generated vector stores, cache files, and other sensitive/generated artifacts should not be committed to the repository.»

---

⚙️ Technology Stack

Component| Technology
Language| Python
RAG Framework| LangChain
Vector Database| ChromaDB
Embeddings| Sentence Transformers
LLM| Gemini
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

Activate it:

venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

---

3. Install Dependencies

pip install -r requirements.txt

---

🔐 Environment Variables

Create a ".env" file in the project root:

GOOGLE_API_KEY=your_google_api_key_here

⚠️ Never commit the real API key to GitHub.

The ".env" file should remain in ".gitignore".

---

📚 Add Medical Documents

Place the medical documents used by the system inside:

data/documents/

The ingestion pipeline processes the documents, splits them into chunks, generates embeddings, and stores them in ChromaDB.

---

▶️ Running the Application

Start the Streamlit application with:

streamlit run app.py

Then open the local Streamlit URL displayed in the terminal.

---

🧪 Testing

The system should be evaluated using different question categories.

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
System should avoid unsupported retrieval/generation

3. General Non-Medical Question

What is machine learning?

Expected behavior:

Question outside the system scope
        ↓
Reject / redirect appropriately

---

🧠 Why RAG?

A standard LLM may generate answers using knowledge learned during pretraining.

For medical applications, this can introduce problems such as:

- Unsupported claims
- Hallucinations
- Outdated information
- Lack of traceable evidence

RAG addresses this by introducing an external knowledge retrieval step:

Traditional LLM

Question
   ↓
LLM
   ↓
Answer

Compared with:

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

This architecture improves the ability to keep generated responses aligned with the project's available medical knowledge.

---

🔒 Medical Safety

This project is an educational and research-oriented AI system and is not intended to replace professional medical advice, diagnosis, or treatment.

The system should be used as an information-support tool rather than as a clinical decision-making system.

Users should consult qualified healthcare professionals for personal medical decisions.

---

🚧 Current Limitations

Although the system provides an evidence-grounded RAG architecture, several limitations remain:

- The quality of responses depends on the quality of the medical documents.
- Retrieval errors can affect final answers.
- The system is limited to its available knowledge base.
- LLMs can still produce incorrect or incomplete information.
- Confidence checking is not equivalent to clinical validation.
- The current system is not a certified medical device.

---

🚀 Future Improvements

Several improvements can further enhance the system:

🔹 Advanced Retrieval

- Hybrid search combining semantic and keyword retrieval
- Re-ranking retrieved chunks
- Metadata-aware filtering
- Query expansion
- Multi-query retrieval

🔹 Medical Knowledge

- Expand the knowledge base with additional authoritative guidelines
- Add guideline versioning
- Improve document quality and preprocessing
- Add source-level metadata

🔹 Evaluation

Implement a dedicated RAG evaluation framework including:

- Recall@K
- Precision@K
- MRR
- Context relevance
- Faithfulness
- Answer relevance
- Retrieval latency

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

🔬 Research Direction

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

👩‍💻 Author

Menna Reda

AI Engineer | Machine Learning | Deep Learning | NLP | Generative AI

GitHub: "@MennaReda2005" (https://github.com/MennaReda2005)

---

⭐ Acknowledgment

This project was developed as an educational/research implementation of Retrieval-Augmented Generation for medical question answering, with a focus on hypertension-related information.



⭐ If you find this project useful, consider giving the repository a star!
