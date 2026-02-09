# Architecture Overview

## Pipeline
1. Input: clinical note text or a PDF file path.
2. Ingestion: PDF text extraction (pypdf) when needed.
3. LLM Agent: prompt-guided extraction into JSON.
4. Validation: Pydantic schema normalization.
5. API: Flask endpoint returns structured JSON.

## Key Components
- `src/api`: Flask app and routes.
- `src/agents`: OpenAI-backed clinical agent with prompt templates.
- `src/workflows`: orchestration layer and schema validation.
- `src/schemas`: structured output models.
- `src/utils`: PDF loader and logging helpers.

## Deployment Notes
- Run locally with `python -m src.api.app`.
- Containerized with the provided Dockerfile.
