from langchain_core.documents import Document

from app.rag.vector_store import vector_store


def retrieve_documents(
    query: str,
    k: int = 4,
) -> list[Document]:
    """
    Retrieve the most relevant document chunks.
    """

    return vector_store.similarity_search(
        query=query,
        k=k,
    )