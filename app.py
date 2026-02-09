"""
app.py — Application Entry Point
=================================
Creates and runs the Flask application that exposes REST endpoints for
triggering LLM-powered clinical data extraction agents.

Usage::

    # Development
    python app.py

    # Production (Gunicorn)
    gunicorn "app:create_app()" --bind 0.0.0.0:5000 --workers 4
"""

from flask import Flask

from api.routes import api_bp
from src.config import config
from src.utils import get_logger

logger = get_logger(__name__)


def create_app() -> Flask:
    """
    Application factory — constructs and configures the Flask app.

    Returns
    -------
    Flask
        A fully configured Flask application instance.
    """
    app = Flask(__name__)

    # Load configuration
    app.config["SECRET_KEY"] = config.SECRET_KEY
    app.config["DEBUG"] = config.FLASK_DEBUG

    # Register blueprints
    app.register_blueprint(api_bp)

    logger.info(
        "Flask app created — env=%s, debug=%s",
        config.FLASK_ENV,
        config.FLASK_DEBUG,
    )
    return app


# ── run the dev server when executed directly ──────────────────────────────

if __name__ == "__main__":
    application = create_app()

    print("=" * 60)
    print("  Clinical AI Agent Prototypes — Flask API Server")
    print("=" * 60)
    print(f"  Host    : {config.HOST}")
    print(f"  Port    : {config.PORT}")
    print(f"  Debug   : {config.FLASK_DEBUG}")
    print(f"  Model   : {config.OPENAI_MODEL}")
    print("=" * 60)
    print()
    print("  Endpoints:")
    print("    GET   /health           — Health check")
    print("    POST  /extract          — Extract structured data from clinical text")
    print("    GET   /extract/<job_id> — Retrieve extraction results")
    print("    POST  /agent/invoke     — Invoke LLM agent with a prompt")
    print()

    application.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.FLASK_DEBUG,
    )
