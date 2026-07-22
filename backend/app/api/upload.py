from fastapi import APIRouter, UploadFile, File

from app.models.upload import UploadResponse
from app.services.upload_service import save_file

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(
    file: UploadFile = File(...)
):
    filename = await save_file(file)

    return UploadResponse(
        filename=filename,
        status="uploaded",
    )