

from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.modules.core.repository import BaseRepository
from app.modules.role.model import Role
from app.modules.user.model import User


class UserRepository(BaseRepository[User]):
    """Репозиторий для работы с пользователями"""

    def __init__(self, db: AsyncSession):
        super().__init__(User, db)

    async def get_by_email(self, email: str) -> User | None:
        """Получить пользователя по email"""
        result = await self.db.execute(
            select(User)
            .where(User.email == email)
            .options(selectinload(User.roles))
        )
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str) -> Optional[User]:
        """Получить пользователя по username"""
        result = await self.db.execute(
            select(User)
            .where(User.username == username)
            .options(selectinload(User.roles))
        )
        return result.scalar_one_or_none()

    async def get_with_roles(self, user_id: int) -> Optional[User]:
        """Получить пользователя с ролями"""
        result = await self.db.execute(
            select(User)
            .where(User.id == user_id)
            .options(selectinload(User.roles).selectinload(Role.permissions))
        )
        return result.scalar_one_or_none()

    async def get_active_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """Получить список активных пользователей"""
        result = await self.db.execute(
            select(User)
            .where(User.is_active.is_(True))
            .where(User.deleted_at.is_(None))
            .offset(skip)
            .limit(limit)
            .options(selectinload(User.roles))
        )
        return list(result.scalars().all())

    async def check_user_has_permission(self, user_id: int, permission_codename: str) -> bool:
        """Проверить наличие права у пользователя"""
        user = await self.get_with_roles(user_id)
        if not user:
            return False

        if user.is_superuser:
            return True

        for role in user.roles:
            for permission in role.permissions:
                if permission.codename == permission_codename:
                    return True

        return False
