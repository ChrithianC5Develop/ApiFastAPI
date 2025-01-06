from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    nombre_usuario: str
    correo: str
    
class CrearUsuario(UsuarioBase):
    contrasenia: str
    rol_id: int
    
class Usuario(UsuarioBase):
    id: int
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    nombre_usuario: str