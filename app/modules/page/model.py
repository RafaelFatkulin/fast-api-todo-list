from typing import Optional

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.modules.core.model import BaseModel, SoftDeleteMixin, TimestampMixin


class Page(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    Модель динамических страниц
    Например: Политика конфиденциальности, Cookie Policy и т.д.
    """

    __tablename__ = "pages"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Краткое описание для превью
    excerpt: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Статус публикации
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Порядок в меню
    menu_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    show_in_menu: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
