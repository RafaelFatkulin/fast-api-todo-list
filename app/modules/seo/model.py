from typing import Optional

from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.modules.core.model import BaseModel, TimestampMixin


class SEO(BaseModel, TimestampMixin):
    """
    Модель SEO параметров
    Можно привязать как к конкретной сущности, так и к странице
    """

    __tablename__ = "seo"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Привязка к сущности или странице
    entity_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, index=True)
    entity_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, index=True)
    page_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, index=True)

    # SEO поля
    meta_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    meta_description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Open Graph
    og_title: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    og_description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    og_image: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Дополнительно
    canonical_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    robots: Mapped[Optional[str]] = mapped_column(
        String(100), nullable=True, default="index, follow"
    )

    # Structured Data (JSON-LD)
    structured_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
