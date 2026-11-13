from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    DB_PASSWORD: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
settings = Settings()
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    DATABASE_URL,pool_pre_ping=True
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass