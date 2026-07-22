from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIRECTORY = Path("uploads")

UPLOAD_DIRECTORY.mkdir(exist_ok=True)


async def save_file(file: UploadFile) -> str:
    filepath = UPLOAD_DIRECTORY / file.filename

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    return file.filename