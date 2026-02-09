import os

from flask import Flask
from dotenv import load_dotenv

from src.api.routes import create_api_blueprint
from src.utils.logging import configure_logging
from src.workflows.extraction_flow import ExtractionWorkflow


def create_app() -> Flask:
    load_dotenv()
    configure_logging()

    app = Flask(__name__)

    workflow = ExtractionWorkflow()
    app.register_blueprint(create_api_blueprint(workflow))

    return app


def main() -> None:
    app = create_app()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    main()
