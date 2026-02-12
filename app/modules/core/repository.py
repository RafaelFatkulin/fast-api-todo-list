from typing import Generic, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.core.database import Base


ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    """Базовый репозиторий с CRUD операциями"""

    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self.model = model
        self.db = db

    async def get(self, obj_id: int) -> Optional[ModelType]:
        """Получить запись по ID"""
        result = await self.db.execute(
            select(self.model).where(self.model.__table__.c.id == obj_id)
        )
        return result.scalar_one_or_none()
