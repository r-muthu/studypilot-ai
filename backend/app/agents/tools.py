from langchain.tools import tool

from app.rag.retriever import retrieve_documents
from app.services.document_retrieval import get_document_metadata, list_documents


@tool
def retrieve_context(query: str) -> str:
    """
    Searches across ALL uploaded documents.

    Returns the most relevant passages together with their document sources.

    Use this tool when:

    • the user does not specify a document
    • the question spans multiple documents
    • the user wants a general answer using all uploaded materials

    Args:
        query:
            A semantic description of the information to retrieve.
            Never leave this empty.

    Good queries:
        - "roles responsible for academic matters"
        - "requirements for constitutional amendments"
        - "advantages of diffusion models"

    Poor queries:
        - ""
        - "role"
        - "draft"
        - "document"

    Prefer descriptive concepts over isolated keywords.
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
    Retrieve passages from one uploaded document.

    Args:
        filename:
            Must exactly match one filename returned by
            list_uploaded_documents().

        query:
            A semantic description of the information to retrieve.
            Never leave this empty.

    Good queries:
        - "roles responsible for academic matters"
        - "requirements for constitutional amendments"
        - "advantages of diffusion models"

    Poor queries:
        - ""
        - "role"
        - "draft"
        - "document"

    Prefer descriptive concepts over isolated keywords.
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
    Returns all uploaded filenames.

    Use this tool when:

    • the user asks what documents are available

    • the user refers to "the paper", "this constitution",
    "that lecture", etc., and you must determine which uploaded
    document they mean
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
    Returns metadata about one uploaded document.

    Use this tool when the user asks about:

    • document information

    • number of pages

    • number of chunks

    • upload metadata
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