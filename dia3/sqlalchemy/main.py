from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ------------------------------------
# Conexión mysql
# ------------------------------------
#sqlite "sqlite:///personas.db"
DATABASE_URL = (
    "mysql+mysqldb://root:root2025@localhost/db_housing_api"
)
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# ------------------------------------
# Clase base para modelos
# ------------------------------------

Base = declarative_base()

# ------------------------------------
# Modelo = tabla
# ------------------------------------
class Persona(Base):
    __tablename__ = "personas"
    
    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    
    def __repr__(self):
        return f"Persona(id={self.id}, nombre='{self.nombre}', edad={self.edad})"
    
# ------------------------------------
# Crear tablas
# ------------------------------------

Base.metadata.create_all(engine)