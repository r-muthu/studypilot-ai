from fastapi import APIRouter, UploadFile, File

from app.models.upload import UploadResponse
from app.services.upload_service import save_file
from app.services.pdf_service import extract_text
from app.services.chunk_service import split_text

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(
    file: UploadFile = File(...)
):
    filepath = await save_file(file)

    text, pages = extract_text(filepath)

    chunks = split_text(text)

    return UploadResponse(
        filename=filepath.name,
        status="uploaded",
        pages=pages,
        characters=len(text),
        chunks=len(chunks)
    )