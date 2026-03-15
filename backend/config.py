from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    SERVER_TIMEZONE: str = "UTC"
    NODE_SERVICE_URL: str = "http://nodejs:3001"
    ALLOWED_ORIGINS: List[str] = ["*"]
    DEFAULT_LATITUDE: float = 51.4769
    DEFAULT_LONGITUDE: float = 0.0005

    class Config:
        env_file = ".env"

settings = Settings()
