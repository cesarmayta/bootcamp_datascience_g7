from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from routers import housing



app = FastAPI(
    title="Housing API con FastAPI",
    description="API para predicción de precios de viviendas usando Machine Learning, FastAPI y SQLAlchemy",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://miapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite cualquier origen
    allow_credentials=False,  # Debe ser False cuando se usa "*"
    allow_methods=["*"],      # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],      # Permite todos los headers
)

app.include_router(housing.router)

@app.get("/")
def index():
    return {
        "title": "FASTAPI HOUSING API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }
    
#Base.metadata.create_all(engine)