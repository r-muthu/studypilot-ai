from fastapi import FastAPI

from app.api.upload import router as upload_router

app = FastAPI(
    title="StudyPilot API",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "StudyPilot API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }