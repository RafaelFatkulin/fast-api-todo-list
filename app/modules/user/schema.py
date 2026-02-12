from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Базовая схема пользователя"""

    email: EmailStr
    username: str = Field(..., min_length=3, max_length=100)
    full_name: Optional[str] = Field(None, max_length=255)


class UserCreate(UserBase):
    """Схема создания пользователя"""

    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Схема обновления пользователя"""

    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=100)
    full_name: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None


class UserChangePassword(BaseModel):
    """Схема смены пароля"""

    old_password: str
    new_password: str = Field(..., min_length=8, max_length=100)


class RoleInUser(BaseModel):
    """Схема роли внутри пользователя"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: Optional[str] = None


class UserResponse(UserBase):
    """Схема ответа с данными пользователя"""

    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    is_superuser: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    roles: List[RoleInUser] = []


class UserListResponse(BaseModel):
    """Схема пользователей с пагинацией"""

    items: List[UserResponse]
    total: int
    page: int
    size: int
    pages: int
