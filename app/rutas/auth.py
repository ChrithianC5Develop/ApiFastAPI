from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import schemas, security, crud
from app.database import get_db
from app.schemas import Token

ruta=APIRouter()

@ruta.post("/login", response_model=Token)
def login_for_access_token(form_data: schemas.CrearUsuario, db:Session = Depends(get_db)):
    usuario=crud.get_user_by_username(db, nombre_usuario=form_data.nombre_usuario)
    
    if not usuario or not security.verify_password(form_data.contrasenia, usuario.contrasena):
        raise HTTPException(status_code=401, detail="Credenciales Invalidas")
    
    access_token = security.create_access_token(data={"sub":usuario.nombre_usuario})
    
    return {"access_token": access_token, "token_type":"bearer"}