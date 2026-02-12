from typing import List

from pydantic import EmailStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения заружаемые из .env файла.
    """

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    SMTP_HOST: str
    SMTP_PORT: int = 587
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAILS_FROM_EMAIL: EmailStr
    EMAILS_FROM_NAME: str

    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 10485760  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [
        "jpg",
        "jpeg",
        "png",
        "gif",
        "webp",  # Изображения
        "mp4",
        "avi",
        "mov",
        "webm",  # Видео
        "pdf",
        "doc",
        "docx",
        "xls",
        "xlsx",  # Документы
    ]

    PROJECT_NAME: str = "FastAPI Project"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False

    @field_validator("ALLOWED_EXTENSIONS", mode="before")
    @classmethod
    def parse_allowed_extensions(cls, v):
        """
        Преобразует строку с расширениями из .env в список строк.
        Поддерживает как строку с разделителем запятая, так и уже готовый список.
        """
        if isinstance(v, str):
            return [ext.strip() for ext in v.split(",")]
        return v


settings = Settings()  # type: ignore[call-arg]
