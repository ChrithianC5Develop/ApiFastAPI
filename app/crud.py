from sqlalchemy.orm import Session
from app import models, schemas, security

def get_user_by_username(db: Session, nombre_usuario: str):
    return db.query(models.Usuarios).filter(models.Usuarios.nombre_usuario == nombre_usuario).first()

def CrearUsuario(db: Session, usuario: schemas.CrearUsuario):
    hashed_password = security.get_password_hash(usuario.contrasenia)
    db_user= models.Usuarios(nombre_usuario=usuario.nombre_usuario,contrasenia=hashed_password, correo=usuario.correo, rol_id=usuario.rol_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

