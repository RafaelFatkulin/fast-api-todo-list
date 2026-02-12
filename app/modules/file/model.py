from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import BigInteger, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.modules.core.model import BaseModel, SoftDeleteMixin, TimestampMixin


class FileType(str, PyEnum):
    """
    Типы файлов
    """

    IMAGE = "image"
    VIDEO = "video"
    DOCUMENT = "document"
    OTHER = "other"


class File(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    Универсальная модель файлов
    Можно привязать к любой сущности через entity_type и entity_id
    """

    __tablename__ = "files"

    # Информация о файле
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_type: Mapped[FileType] = mapped_column(Enum(FileType), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False)
    file_size: Mapped[int] = mapped_column(BigInteger, nullable=False)  # в байтах

    # Привязка к сущности (полиморфная связь)
    entity_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, index=True)
    entity_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, index=True)

    # Дополнительные поля для изображений
    width: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # Порядок отображения (для галерей)
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Метаданные
    alt_text: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
