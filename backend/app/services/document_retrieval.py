from app.rag.vector_store import vector_store


def list_documents() -> list[str]:
    """
    Return every uploaded filename.
    """

    data = vector_store.get()

    if not data["metadatas"]:
        return []

    return sorted(
        {
            metadata["source"]
            for metadata in data["metadatas"]
        }
    )

def get_document_metadata(
    filename: str,
):
    """
    Return metadata for one uploaded document.
    """

    data = vector_store.get(
        where={
            "source": filename,
        }
    )

    if not data["metadatas"]:
        return None

    metadata = data["metadatas"][0]

    return {
        "filename": filename,
        "chunks": metadata["total_chunks"],
    }