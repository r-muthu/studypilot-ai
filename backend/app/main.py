from fastapi import FastAPI

app = FastAPI(
    title="StudyPilot API",
    version="1.0.0",
)


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