from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')
    dbUrl:str
    dbDatabase:str
    logKey:str

class AdminLoginSchema(BaseModel):
    Username:str
    Password:str

settings = Settings()