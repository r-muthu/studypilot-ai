from langchain.tools import tool

from app.rag.retriever import retrieve_documents
from app.services.document_retrieval import get_document_metadata, list_documents


@tool
def retrieve_context(query: str) -> str:
    """
    Retrieve relevant information from uploaded study materials.
    """

    documents = retrieve_documents(query)

    if not documents:
        return "No relevant context found."

    contexts = []

    for i, document in enumerate(documents, start=1):
        source = document.metadata.get("source", "Unknown")

        contexts.append(
            f"""Source: {source}

Passage {i}

{document.page_content}
"""
        )

    return "\n\n".join(contexts)


@tool
def retrieve_document(
    filename: str,
    query: str,
) -> str:
    """
    Retrieve relevant passages from one uploaded document.
    """

    documents = retrieve_documents(
        query=query,
        filename=filename,
    )

    if not documents:
        return "No matching passages found."

    passages = []

    for i, document in enumerate(documents, start=1):
        passages.append(
            f"""Passage {i}

{document.page_content}
"""
        )

    return "\n\n".join(passages)


@tool
def list_uploaded_documents() -> str:
    """
    List every uploaded study material.
    """

    documents = list_documents()

    if not documents:
        return "No uploaded documents."

    return "\n".join(documents)


@tool
def document_metadata(
    filename: str,
) -> str:
    """
    Return metadata about one uploaded document.
    """

    metadata = get_document_metadata(filename)

    if metadata is None:
        return "Document not found."

    return f"""
Filename: {metadata['filename']}
Chunks: {metadata['chunks']}
"""


TOOLS = [
    retrieve_context,
    retrieve_document,
    list_uploaded_documents,
    document_metadata,
]