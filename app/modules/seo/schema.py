# app/schemas/seo.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SEOBase(BaseModel):
    """Базовая схема SEO"""

    meta_title: Optional[str] = Field(None, max_length=255)
    meta_description: Optional[str] = Field(None, max_length=500)
    meta_keywords: Optional[str] = Field(None, max_length=500)
    og_title: Optional[str] = Field(None, max_length=255)
    og_description: Optional[str] = Field(None, max_length=500)
    og_image: Optional[str] = Field(None, max_length=500)
    twitter_title: Optional[str] = Field(None, max_length=255)
    twitter_description: Optional[str] = Field(None, max_length=500)
    twitter_image: Optional[str] = Field(None, max_length=500)
    canonical_url: Optional[str] = Field(None, max_length=500)
    robots: Optional[str] = Field("index, follow", max_length=100)
    structured_data: Optional[str] = None


class SEOCreate(SEOBase):
    """Схема создания SEO"""

    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
    page_url: Optional[str] = None


class SEOUpdate(SEOBase):
    """Схема обновления SEO"""

    pass


class SEOResponse(SEOBase):
    """Схема ответа с данными SEO"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
    page_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
