from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.vector_store import vector_store


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

def split_text(text: str) -> list[str]:
    """
    Split extracted text into overlapping chunks.
    """

    return splitter.split_text(text)


def store_chunks(
    chunks: list[str],
    filename: str,
):
    documents = [
        Document(
            page_content=chunk,
            metadata={
                "source": filename,
                "chunk": index,
                "total_chunks": len(chunks),
            },
        )
        for index, chunk in enumerate(chunks)
    ]

    vector_store.add_documents(documents)