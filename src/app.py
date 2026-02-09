"""
Clinical AI Agent Prototypes — Flask Application Entry Point.

This is the main entry point for the Flask API server.
It creates the app, loads configuration, registers blueprints,
and starts the development server.

Usage:
    python src/app.py
"""

import os
import sys

from flask import Flask, jsonify

# ---------------------------------------------------------------------------
# Application factory
# ---------------------------------------------------------------------------

def create_app() -> Flask:
    """Create and configure the Flask application."""

    app = Flask(__name__)

    # --- Configuration -------------------------------------------------------
    from src.config import Config

    config = Config.from_env()
    app.config["OPENAI_API_KEY"] = config.openai_api_key
    app.config["DEBUG"] = config.flask_env == "development"

    # --- Register blueprints -------------------------------------------------
    from src.api.routes import api_bp

    app.register_blueprint(api_bp)

    # --- Root health-check (convenience) -------------------------------------
    @app.route("/")
    def index():
        return jsonify(
            {
                "service": "Clinical AI Agent Prototypes",
                "status": "running",
                "version": "0.1.0",
            }
        )

    return app


# ---------------------------------------------------------------------------
# Dev-server entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Allow running with `python src/app.py` from the repo root.
    # Ensure the repo root is on sys.path so `from src.*` imports resolve.
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    from src.config import Config

    config = Config.from_env()

    app = create_app()

    print("=" * 60)
    print("  Clinical AI Agent Prototypes — Flask API Server")
    print("=" * 60)
    print(f"  Environment : {config.flask_env}")
    print(f"  Port        : {config.flask_port}")
    print(f"  OpenAI key  : {'configured' if config.openai_api_key else 'MISSING'}")
    print()
    print("  Endpoints:")
    print("    GET  /              — Service info / health check")
    print("    GET  /health        — Liveness probe")
    print("    POST /extract       — Submit clinical text for extraction")
    print("    GET  /extract/<id>  — Retrieve extraction results")
    print("    POST /agent/run     — Trigger the clinical AI agent")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=config.flask_port,
        debug=(config.flask_env == "development"),
    )
