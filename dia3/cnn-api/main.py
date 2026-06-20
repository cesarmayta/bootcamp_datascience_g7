import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from cnn_model import predict_class

app = FastAPI(
    title="Garbage Classifier API ",
    description="API para clasificación de tipos de basura",
    version="1.0.0"
)

IMAGES_DIR = Path(__file__).resolve().parent / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


@app.get("/")
def index():
    return {
        "title": "API CLASSIFIER API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    destination = IMAGES_DIR / file.filename
    try:
        contents = await file.read()
        with destination.open("wb") as f:
            f.write(contents)
    finally:
        await file.close()
        
    class_name = predict_class(destination)

    return {
        "filename": file.filename,
        "tipo": class_name,
        "path": str(destination)
    }

