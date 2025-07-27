"""Script to build the vector database with the Docling research paper."""

import sys
from rag import RAGSystem
from rag.config import DOCLING_PAPER_URL


def main():
    print("=== Building Vector Database ===\n")

    # Initialize RAG system
    print("Initializing RAG system...")
    rag = RAGSystem()

    # Check if database already has documents
    doc_count = rag.vector_store.get_document_count()
    if doc_count > 0:
        response = input(
            f"\nDatabase already contains {doc_count} documents. Clear and rebuild? (y/n): "
        )
        if response.lower() == "y":
            print("Clearing existing documents...")
            rag.vector_store.clear_all_documents()
        else:
            print("Keeping existing documents.")

    # Ingest the Docling paper
    print("\nIngesting Docling research paper...")
    print(f"URL: {DOCLING_PAPER_URL}")

    try:
        rag.ingest_document(DOCLING_PAPER_URL)
        print("\nVector database built successfully!")

        # Show system stats
        stats = rag.get_stats()
        print("\nSystem Statistics:")
        print(f"- Total documents: {stats['total_documents']}")
        print(f"- Embedding model: {stats['embedding_model']}")
        print(f"- Embedding dimensions: {stats['embedding_dimensions']}")
        print(f"- Chat model: {stats['chat_model']}")

    except Exception as e:
        print(f"\nError building vector database: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
