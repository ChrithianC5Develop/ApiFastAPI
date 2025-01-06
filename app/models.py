from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuarios(Base):
    __tablename__ ="usuarios"
    
    id=Column(Integer, primary_key=True, index=True)
    nombre_usuario=Column(String, unique=True)
    contrasena=Column(String)
    correo=Column(String, unique=True)
    rol_id=Column(Integer)