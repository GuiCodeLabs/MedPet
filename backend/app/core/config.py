from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MEDPET"
    DATABASE_URL: str = "sqlite:///./medpet.db"
    SECRET_KEY: str = "sua_chave_secreta_aqui"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
