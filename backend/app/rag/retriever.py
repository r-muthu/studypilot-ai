from langchain_core.documents import Document

from app.rag.vector_store import vector_store


def retrieve_documents(
    query: str,
    filename: str | None = None,
    k: int = 4,
) -> list[Document]:
    """
    Retrieve relevant chunks from ChromaDB.
    """

    if filename:
        return vector_store.similarity_search(
            query=query,
            k=k,
            filter={
                "source": filename,
            },
        )

    return vector_store.similarity_search(
        query=query,
        k=k,
    )