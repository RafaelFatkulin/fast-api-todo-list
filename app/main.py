"""
Главный файл приложения
Точка входа, настройка CORS, роутеры
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan события приложения
    """
    print("🚀 Запуск приложения...")

    await init_db()
    print("✅ База данных инициализирована")

    # await init_base_data()
    print("✅ Базовые данные созданы")

    yield

    print("🛑 Остановка приложения...")
    await close_db()
    print("✅ Соединения закрыты")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="description",
    lifespan=lifespan,
    docs_url="/api/docs/" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(some_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "FastAPI System",
        "version": settings.VERSION,
        "docs": "/api/docs" if settings.DEBUG else "Disabled in production",
    }


@app.get("/health")
async def health_check():
    """Health Check Endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
