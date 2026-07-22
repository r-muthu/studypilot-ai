from langchain_core.documents import Document

from app.rag.vector_store import vector_store


def store_chunks(
    chunks: list[str],
    filename: str,
):
    documents = [
        Document(
            page_content=chunk,
            metadata={
                "source": filename,
            },
        )
        for chunk in chunks
    ]

    vector_store.add_documents(documents)