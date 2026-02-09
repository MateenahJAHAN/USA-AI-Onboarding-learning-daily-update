# Clinical AI Agent Prototypes for USA AI

## Overview
This repository showcases clinical LLM agent prototypes that extract structured
data from unstructured clinical inputs (notes, forms, PDFs). It demonstrates
end-to-end workflows that combine ingestion, LLM orchestration, and API delivery
for clinical documentation and analytics use cases.

## Why this matters
- Reduce manual chart review and abstraction time.
- Produce consistent, structured outputs for downstream analytics.
- Enable rapid experimentation with clinical NLP pipelines.

## Key Features
- Flask API Development
- LLM Workflow Orchestration
- Model Context Protocol (MCP) Implementation

## Tech Stack
- Python
- Flask
- OpenAI API (or similar LLM provider)
- Model Context Protocol (MCP)

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_key_here"
python -m src.api.app
```

Example request:
```bash
curl -X POST http://localhost:8000/extract \
  -H "Content-Type: application/json" \
  -d '{"text":"Patient presents with chest pain and shortness of breath."}'
```

For local development without an API key:
```bash
export CLINICAL_AGENT_MOCK=1
python -m src.api.app
```

## Testing
```bash
pip install -r requirements-dev.txt
pytest
```

## High-Level Architecture
```
PDF/Note -> Text Extractor -> LLM Agent -> Schema Validation -> API Response
                               |-> MCP Tools (optional)
```

## Example API Contract (Illustrative)
Request:
```json
{
  "text": "Patient presents with chest pain and shortness of breath...",
  "metadata": {"source": "discharge_summary.pdf"}
}
```

Response:
```json
{
  "patient": {"name": "Jane Doe", "dob": "1978-04-03"},
  "diagnoses": ["Hypertension", "Type 2 diabetes"],
  "medications": [{"name": "Metformin", "dose": "500 mg"}],
  "confidence": 0.82
}
```

## Repository Layout
Primary implementation lives in `src/`. Legacy day-based learning logs are kept
in `/learning_logs/day-01` through `/learning_logs/day-12` for historical
context, but the production-ready code path is under `/src`.

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
/tests
  test_api.py
/docs
  architecture.md
/requirements.txt
/Dockerfile
```

### Suggested migration examples
- `day 7/flask_api.py` -> `src/api/app.py`
- `Day 8/day_8_openai_api.py` -> `src/agents/clinical_agent.py`
- `Day-4/day4_python_api.py` -> `src/workflows/extraction_flow.py`
- `day 6/flask loan api builder` -> `src/api/`
- `day 8/day_8_github_api.py` -> `docs/` (reference examples)

## Results / Metrics (Initial Evaluation Plan)
Evaluation set (proposed):
- 15 de-identified notes (5 discharge summaries, 5 progress notes,
  5 imaging summaries)

Metrics to report:
- Schema validity rate
- Field-level precision/recall/F1 for diagnoses and medications
- Extraction coverage for key fields (patient, meds, diagnoses)

Current results:
- TBD (pending evaluation harness and gold labels)

## Quality, Safety, and Reliability (Planned)
- Schema-first outputs (Pydantic) to reduce hallucinations.
- Prompt guardrails for clinical safety and consistency.
- Logging with redaction for PHI-sensitive data.

## Roadmap (Short-Term)
- Migrate day-based scripts into `/src` modules.
- Add evaluation harness and gold labels for metrics reporting.
- Expand MCP tool registry for retrieval and knowledge base lookups.
- Add CI for linting and tests.


