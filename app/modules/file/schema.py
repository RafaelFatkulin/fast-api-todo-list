from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from app.modules.file.model import FileType


class FileBase(BaseModel):
    """Базовая схема файла"""

    alt_text: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    sort_order: int = 0


class FileCreate(FileBase):
    """Схема создания файла"""

    entity_type: Optional[str] = None
    entity_id: Optional[int] = None


class FileUpdate(BaseModel):
    """Схема обновления файла"""

    alt_text: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    sort_order: Optional[int] = None


class FileResponse(FileBase):
    """Схема ответа с данными файла"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    original_filename: str
    file_path: str
    file_type: FileType
    mime_type: str
    file_size: int
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    created_at: datetime

    @property
    def url(self) -> str:
        """URL для доступа к файлу"""
        return f"/uploads/{self.file_path}"
