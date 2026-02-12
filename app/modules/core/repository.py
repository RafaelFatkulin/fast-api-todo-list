from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from sqlalchemy import func, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.core.model import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


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

    async def get_many(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[ModelType]:
        """Получить список записей c фильтрами"""
        query = select(self.model)

        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.where(getattr(self.model, key) == value)

        query = query.offset(skip).limit(limit)
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def count(self, filters: Optional[Dict[str, Any]] = None) -> int:
        """Получить количество записей c фильтрами"""
        query = select(func.count()).select_from(self.model)

        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    query = query.where(getattr(self.model, key) == value)

        result = await self.db.execute(query)
        return result.scalar_one()

    async def create(self, obj_in: Dict[str, Any]) -> ModelType:
        """Создать запись"""
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)
        return db_obj

    async def update(self, id: int, obj_in: Dict[str, Any]) -> Optional[ModelType]:
        """Обновить запись"""
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**obj_in)
            .returning(self.model)
        )
        result = await self.db.execute(stmt)
        await self.db.commit()
        return result.scalar_one_or_none()

    async def delete(self, id: int) -> bool:
        """Удалить запись"""
        obj = await self.db.get(self.model, id)
        if not obj:
            return False

        await self.db.delete(obj)
        await self.db.commit()
        return True
