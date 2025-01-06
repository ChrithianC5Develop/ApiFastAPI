from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import configuraciones

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def get_password_hash(contrasenia: str):
    return pwd_context.hash(contrasenia)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

#Crear el Token de acceso
def create_access_token(data: dict, expires_delta: timedelta= timedelta(minutes=30)):
    to_encode=data.copy()
    expire=datetime.utcnow()+expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, configuraciones.secret_key, algorithm=configuraciones.algorithm)
    return encoded_jwt