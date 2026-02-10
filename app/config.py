"""
Конфигурация приложения.
Все настройки загружаются из переменных окружения или .env файла.
"""

from typing import List

from pydantic import EmailStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Основные настройки приложения"""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="UTF-8", case_sensitive=True
    )

    PROJECT_NAME: str = "FastAPI system"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "production"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_URL = "sqlite+aiosqlite:///./app.db"

    SECRET_KEY: str = "SECRET"
    ALGHORITM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: EmailStr = "noreply@example.com"
    SMTP_FROM_NAME: str = "FASTAPI App"

    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000"]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | List[str]) -> List[str]:
        """Парсинг CORS origins из строки или списка"""
        if isinstance(v, str):
            return [i.strip() for i in v.split(",")]
        return v

    FIRST_SUPERUSER_EMAIL: EmailStr = "admin@vk.com"
    FIST_SUPERUSER_PASSWORD: str = "password"

    SITE_NAME: str = "My Application"
    SITE_DESCRIPTION: str = "My Application Description"
    REGISTRATION_ENABLED: bool = True
    EMAIL_VERIFICATION_ENABLED: bool = False

    @property
    def is_async_db(self) -> bool:
        """Проверка на ассинхронную БД"""
        return "asyncpg" in self.DATABASE_URL or "aiosqlite" in self.DATABASE_URL


settings = Settings()
