from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)


class Settings(BaseSettings):
    app_name: str = "RAG Assistant"
    app_env: Literal["local", "dev", "prod"] = "local"
    debug: bool = False
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",  # переменные в .env, которых нет в Settings,
    )


@lru_cache
def get_settings() -> Settings:
    """Возвращает singleton-экземпляр настроек приложения."""
    return Settings()
