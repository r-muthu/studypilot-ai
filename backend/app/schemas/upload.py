from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    status: str
    pages: int
    characters: int
    chunks: int