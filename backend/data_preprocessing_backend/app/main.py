from fastapi import FastAPI
from app.routes.preprocess import router as preprocess_router

app = FastAPI(title="Data Preprocessing Backend")

app.include_router(preprocess_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
