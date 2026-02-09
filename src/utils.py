"""
Shared utility helpers used across the application.
"""

import logging
import uuid
from typing import Any

from flask import jsonify


def get_logger(name: str) -> logging.Logger:
    """Return a consistently-configured logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s — %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def generate_job_id(prefix: str = "ext") -> str:
    """Generate a short unique job identifier."""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def success_response(data: Any, status_code: int = 200):
    """Wrap data in a standard success envelope."""
    return jsonify({"status": "success", "data": data}), status_code


def error_response(message: str, status_code: int = 400):
    """Wrap an error message in a standard error envelope."""
    return jsonify({"status": "error", "message": message}), status_code
