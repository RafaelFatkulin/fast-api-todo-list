from typing import Optional

from sqlalchemy import Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.modules.core.database import Base
from app.modules.core.model import IdMixin, TimestampMixin


class SiteSetting(Base, IdMixin, TimestampMixin):
    """
    Модель настроек сайта
    Хранит различные параметры: телефоны, email, соц.сети и т.д.
    """

    __tablename__ = "site_settings"

    # Уникальный ключ настройки
    key: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    # Значение настройки
    value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Метаданные
    label: Mapped[str] = mapped_column(String(255), nullable=False)  # Название для админки
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Группировка в админке
    group: Mapped[str] = mapped_column(String(100), default="general", nullable=False)

    # Тип поля (для генерации форм в админке)
    field_type: Mapped[str] = mapped_column(
        String(50), default="text", nullable=False
    )  # text, email, tel, textarea, url, etc.

    # Активность
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Порядок отображения
    sort_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
