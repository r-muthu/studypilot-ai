from langchain_chroma import Chroma

from app.models.embeddings import embeddings


vector_store = Chroma(
    collection_name="studypilot",
    embedding_function=embeddings,
    persist_directory="chroma_db",
)