from pydantic import BaseModel, Field
class Configuraciones(BaseModel):
    database_url: str= Field(...,env="DATABASE_URL")
    secret_key: str=Field(...,env="SECRET_KEY")
    algorithm: str=Field("HS256",env="ALGORITHM")
    access_token_expire_minutes: int= Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")    
    class Config:
        env_file=".env"
        env_file_encoding="utf-8"        
#Creamos la instancia de la configuracion
configuraciones=Configuraciones()