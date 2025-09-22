# src/config/settings.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/eduflow"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = True

    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/app.log"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Singleton instance
settings = Settings()
