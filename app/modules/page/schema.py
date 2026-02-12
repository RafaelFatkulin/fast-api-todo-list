# app/schemas/page.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PageBase(BaseModel):
    """Базовая схема страницы"""

    title: str = Field(..., max_length=255)
    slug: str = Field(..., max_length=255)
    content: str
    excerpt: Optional[str] = Field(None, max_length=500)
    is_published: bool = False
    menu_order: int = 0
    show_in_menu: bool = True


class PageCreate(PageBase):
    """Схема создания страницы"""

    pass


class PageUpdate(BaseModel):
    """Схема обновления страницы"""

    title: Optional[str] = Field(None, max_length=255)
    slug: Optional[str] = Field(None, max_length=255)
    content: Optional[str] = None
    excerpt: Optional[str] = Field(None, max_length=500)
    is_published: Optional[bool] = None
    menu_order: Optional[int] = None
    show_in_menu: Optional[bool] = None


class PageResponse(PageBase):
    """Схема ответа с данными страницы"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
