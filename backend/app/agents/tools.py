from langchain.tools import tool

from app.rag.retriever import retrieve_documents


@tool
def retrieve_context(query: str) -> str:
    """
    Retrieve relevant context from uploaded study materials.
    """

    documents = retrieve_documents(query)

    if not documents:
        return "No relevant information found."

    return "\n\n".join(
        document.page_content
        for document in documents
    )

TOOLS = [
    retrieve_context,
]