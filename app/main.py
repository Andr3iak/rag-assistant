"""Точка входа FastAPI-приложение"""

from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="AI-ассистент для работы с корпоративными документами",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Проверка работоспособности сервиса."""
    return {"status": "ok"}
