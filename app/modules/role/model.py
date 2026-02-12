from typing import List, Optional

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.core.model import BaseModel, TimestampMixin
from app.modules.user.model import User

# Таблица связи many-to-many между Role и Permission
role_permissions = Table(
    "role_permissions",
    BaseModel.metadata,
    Column("role_id", Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True),
    Column(
        "permission_id", Integer, ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True
    ),
)


class Role(BaseModel, TimestampMixin):
    """
    Модель роли пользователя
    """

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Relationships
    users: Mapped[List["User"]] = relationship(
        "User", secondary="user_roles", back_populates="roles"
    )

    permissions: Mapped[List["Permission"]] = relationship(
        "Permission", secondary=role_permissions, back_populates="roles", lazy="selectin"
    )


class Permission(BaseModel, TimestampMixin):
    """
    Модель прав доступа
    """

    __tablename__ = "permissions"

    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    codename: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    # Relationships
    roles: Mapped[List["Role"]] = relationship(
        "Role", secondary=role_permissions, back_populates="permissions"
    )
