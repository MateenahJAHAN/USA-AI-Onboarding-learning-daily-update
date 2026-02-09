"""
Centralised configuration — loads environment variables once.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    """Immutable application configuration."""

    openai_api_key: str
    flask_env: str
    flask_port: int
    log_level: str

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------
    @classmethod
    def from_env(cls, dotenv_path: str | None = None) -> "Config":
        """Load configuration from environment variables (and .env file)."""
        load_dotenv(dotenv_path or os.path.join(os.getcwd(), ".env"))

        return cls(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
            flask_env=os.getenv("FLASK_ENV", "development"),
            flask_port=int(os.getenv("FLASK_PORT", "5000")),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
        )
