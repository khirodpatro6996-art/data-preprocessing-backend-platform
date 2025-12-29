from fastapi import FastAPI
from app.routes.preprocess import router as preprocess_router

app = FastAPI(
    title="Data Preprocessing Backend API",
    version="1.0.0"
)

app.include_router(preprocess_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "Data Preprocessing Backend is running",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
def health():
    return {"status": "ok"}
