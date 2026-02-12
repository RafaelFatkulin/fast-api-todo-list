# app/schemas/site_settings.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SiteSettingBase(BaseModel):
    """Базовая схема настройки"""

    key: str = Field(..., max_length=100)
    value: Optional[str] = None
    label: str = Field(..., max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    group: str = Field("general", max_length=100)
    field_type: str = Field("text", max_length=50)
    is_active: bool = True
    sort_order: int = 0


class SiteSettingCreate(SiteSettingBase):
    """Схема создания настройки"""

    pass


class SiteSettingUpdate(BaseModel):
    """Схема обновления настройки"""

    value: Optional[str] = None
    label: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    group: Optional[str] = Field(None, max_length=100)
    field_type: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = None
    sort_order: Optional[int] = None


class SiteSettingResponse(SiteSettingBase):
    """Схема ответа с данными настройки"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime


class SiteSettingBulkUpdate(BaseModel):
    """Схема массового обновления настроек"""

    settings: dict[str, str]  # key: value
