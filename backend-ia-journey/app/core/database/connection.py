from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from uuid import UUID 
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    TEST_ENTERPRISE_ID: Optional[UUID]=None
    DB_PASSWORD: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_ignore_empty=True,
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