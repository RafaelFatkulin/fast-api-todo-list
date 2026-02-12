from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class PermissionBase(BaseModel):
    """Базовая схема права"""

    name: str = Field(..., max_length=100)
    codename: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class PermissionCreate(PermissionBase):
    """Схема создания права"""

    pass


class PermissionResponse(PermissionBase):
    """Схема ответа с данными права"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


class RoleBase(BaseModel):
    """Базовая схема роли"""

    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class RoleCreate(RoleBase):
    """Схема создания роли"""

    permission_ids: List[int] = []


class RoleUpdate(BaseModel):
    """Схема обновления роли"""

    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    permission_ids: Optional[List[int]] = None


class RoleResponse(RoleBase):
    """Схема ответа с данными роли"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    permissions: List[PermissionResponse] = []
