# End-to-End RAG Pipeline

This directory contains a complete implementation of a Retrieval-Augmented Generation (RAG) pipeline using PGVector, OpenAI embeddings, and the Docling research paper as an example dataset.

## Project Structure

```text
rag-pipeline/
├── rag_chat.py                 # Interactive query interface
├── examples.py                 # Usage examples
├── build_vectordb.py           # Database setup script (run once)
├── README.md                   # This file
└── rag/                        # Implementation package (no need to modify)
    ├── __init__.py     
    ├── config.py               # Configuration settings
    ├── rag_system.py           # Main orchestrator
    ├── vector_store.py         # PGVector interface
    ├── document_processor.py   # Document chunking
    └── embedding_service.py    # Embedding generation
```

## Architecture Overview

The RAG pipeline consists of the following components:

1. **Document Processing**: Extract and chunk the Docling research paper
2. **Embedding Generation**: Create embeddings using OpenAI's text-embedding-3-small
3. **Vector Storage**: Store embeddings in PGVector database
4. **Similarity Search**: Query the database to find relevant chunks
5. **Response Generation**: Use retrieved context to generate answers with OpenAI

## Prerequisites

- Docker and Docker Compose installed
- OpenAI API key
- Python 3.9+

## Setup

 **Start PGVector Database**:
```bash
cd ../pgvector-setup/docker
docker-compose up -d
cd ../../rag-pipeline
```

## Usage

### Step 1: Build the Vector Database

First, populate the vector database with the Docling paper:

```bash
python build_vectordb.py
```

This will:
- Download and process the Docling research paper
- Create 29 chunks using hybrid chunking
- Generate embeddings for each chunk
- Store everything in PGVector

### Step 2: Query the System

Run the interactive query interface:

```bash
python rag_chat.py
```

### Step 3: Explore Examples

Study the example scripts to understand different usage patterns:

```bash
python examples.py
```

## Programmatic Usage

You can also use the RAG system in your own Python scripts:

```python
from rag import RAGSystem

# Initialize the system
rag = RAGSystem()

# Ask a question
response = rag.query("What is Docling and what are its main features?")
print(response)

# Get more context
response_with_context = rag.query(
    "How does Docling handle tables?",
    show_context=True  # Shows the retrieved chunks
)
print(response_with_context)
```
