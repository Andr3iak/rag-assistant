"""Точка входа FastAPI-приложение"""

from fastapi import FastAPI

app = FastAPI(
    title = "RAG-assistant",
    version = "0.1.0",
    description="AI-ассистент для работы с корпоративными документами",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Проверка работоспособности сервиса."""
    return {"status" : "ok"}

