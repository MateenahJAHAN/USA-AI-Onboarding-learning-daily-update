# Clinical AI Agent Prototypes for USA AI

## Description
This repository contains professional prototypes for extracting structured data
from unstructured clinical inputs (including PDFs) using LLM agents. The
projects demonstrate end-to-end workflows that combine data ingestion, LLM
orchestration, and API delivery to support clinical documentation and analytics
use cases.

## Key Features
- Flask API Development
- LLM Workflow Orchestration
- Model Context Protocol (MCP) Implementation

## Tech Stack
- Python
- Flask
- OpenAI API (or similar LLM provider)
- Model Context Protocol (MCP)

## Refactored Code Structure (File Plan)
Replace the "Day 1/Day 2/Day 3" folders with a product-style layout:

```
/src
  /api
    app.py                # Flask entry point
    routes.py             # API routes / blueprints
  /agents
    clinical_agent.py     # LLM agent wrapper
    prompts/              # Prompt templates
  /workflows
    extraction_flow.py    # Orchestrated LLM pipeline
  /mcp
    server.py             # MCP server wiring
    tools.py              # MCP tool definitions
  /schemas
    clinical.py           # Pydantic schemas for outputs
  /utils
    pdf_loader.py         # PDF text extraction utilities
    logging.py
/data
  /samples                # Sample PDFs or JSON fixtures
/tests
  test_api.py
  test_agents.py
/docs
  architecture.md
```

### Suggested migration examples
- `day 7/flask_api.py` -> `src/api/app.py`
- `Day 8/day_8_openai_api.py` -> `src/agents/clinical_agent.py`
- `Day-4/day4_python_api.py` -> `src/workflows/extraction_flow.py`
- `day 6/flask loan api builder` -> `src/api/`
- `day 8/day_8_github_api.py` -> `docs/` (reference examples)

## Template: main `app.py` (Flask API Entry Point)
Use this as a starting point for a production-style Flask entry point that
invokes an LLM agent:

```python
from flask import Flask, jsonify, request
from agents.clinical_agent import ClinicalAgent


def create_app() -> Flask:
    app = Flask(__name__)
    agent = ClinicalAgent()

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/extract", methods=["POST"])
    def extract():
        payload = request.get_json(silent=True) or {}
        text = payload.get("text", "").strip()

        if not text:
            return jsonify({"error": "text is required"}), 400

        # The agent returns a structured JSON payload
        result = agent.extract_structured_data(text)
        return jsonify(result), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=False)
```

---
If you want, I can help convert existing scripts into this structure and add a
minimal `ClinicalAgent` implementation with OpenAI API calls.
