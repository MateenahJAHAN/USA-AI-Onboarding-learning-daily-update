# Clinical AI Agent Prototypes for USA AI

> Prototypes for extracting structured data from unstructured clinical inputs (PDFs, free-text notes) using LLM-powered Agents, RESTful APIs, and the Model Context Protocol (MCP).

---

## Overview

This repository contains a collection of working prototypes that demonstrate how large-language-model (LLM) agents can be orchestrated behind lightweight APIs to process unstructured clinical documents — such as scanned PDFs, handwritten notes, and free-text medical records — and return clean, structured JSON suitable for downstream analytics, EHR integration, or regulatory reporting.

The codebase covers three core capability areas:

| Capability | What It Demonstrates |
|---|---|
| **Flask API Development** | Production-style REST endpoints for receiving documents, triggering agent pipelines, and returning structured results. |
| **LLM Workflow Orchestration** | Multi-step agent chains that call OpenAI (GPT-3.5 / GPT-4) to parse, classify, and extract entities from clinical text. |
| **Model Context Protocol (MCP)** | An implementation of the emerging MCP standard for managing context windows, tool invocations, and agent-to-agent communication. |

---

## Key Features

### Flask API Development
- Full CRUD REST API built with Flask (and a FastAPI variant)
- Request validation, error handling, and JSON response formatting
- Modular route blueprints ready for production deployment
- Integration with external APIs (GitHub, OpenWeatherMap, JSONPlaceholder)

### LLM Workflow Orchestration
- OpenAI Chat Completions API integration (GPT-3.5-turbo / GPT-4)
- Configurable system prompts and temperature settings
- Multi-turn conversation management and context handling
- Simulated CRUD operations over LLM-generated content

### Model Context Protocol (MCP) Implementation
- Structured tool-use patterns for agent-to-agent communication
- Context window management for long clinical documents
- Extensible agent architecture for adding new extraction capabilities

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13+ |
| Web Framework | Flask, FastAPI |
| LLM Provider | OpenAI API (GPT-3.5-turbo, GPT-4) |
| Agent Protocol | Model Context Protocol (MCP) |
| HTTP Client | Requests |
| Data Validation | Pydantic |
| Environment Mgmt | python-dotenv |

---

## Project Structure

```
clinical-ai-agent-prototypes/
│
├── app.py                          # Application entry point — Flask server + agent trigger
│
├── src/
│   ├── __init__.py
│   ├── config.py                   # Centralised configuration & env-var loading
│   └── utils.py                    # Shared helpers (logging, response formatting)
│
├── api/
│   ├── __init__.py
│   ├── routes.py                   # Flask route definitions (blueprints)
│   └── schemas.py                  # Request / response schemas (Pydantic models)
│
├── agents/
│   ├── __init__.py
│   ├── base_agent.py               # Abstract base class for all agents
│   ├── clinical_extractor.py       # LLM agent: extracts structured data from clinical text
│   └── document_parser.py          # PDF / free-text pre-processing agent
│
├── mcp/
│   ├── __init__.py
│   ├── context_manager.py          # MCP context-window manager
│   └── tool_registry.py            # Tool definitions for agent invocations
│
├── workflows/
│   ├── __init__.py
│   └── extraction_pipeline.py      # End-to-end orchestration: ingest → parse → extract → respond
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py                 # API endpoint tests
│   └── test_agents.py              # Agent unit tests
│
├── notebooks/                      # Exploratory Jupyter notebooks (learning & experiments)
│   ├── python_fundamentals.ipynb
│   └── llm_experiments.ipynb
│
├── requirements.txt                # Pinned Python dependencies
├── .env.example                    # Template for environment variables
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

### Mapping from Original Structure

| Original (Day-based) | Refactored Location | Purpose |
|---|---|---|
| `day 7/flask_api.py` | `api/routes.py` | Flask CRUD API routes |
| `day 7/api_request.py` | `agents/document_parser.py` | HTTP request utilities |
| `Day 8/day_8_openai_api.py` | `agents/clinical_extractor.py` | OpenAI API integration |
| `DAY 10/openai_api_dcrud.py` | `agents/clinical_extractor.py` | LLM CRUD operations |
| `DAY 10/github_*.py` | `workflows/extraction_pipeline.py` | API orchestration patterns |
| `day 11/main.py` | `app.py` | FastAPI entry point (adapted to Flask) |
| `day 12/chat_completion.py` | `agents/clinical_extractor.py` | Chat completion logic |
| `day 12/get_posts.py` | `api/routes.py` | External API consumption |
| `day 9/weather_kashmir.py` | `notebooks/` | API experimentation (reference) |
| `Day-4/day4_python_api.py` | `notebooks/` | Python fundamentals (reference) |
| `day 6/flask loan api builder` | `api/routes.py` | Flask app patterns |
| `*.ipynb` files | `notebooks/` | Jupyter experiments |

---

## Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Installation

```bash
# Clone the repository
git clone https://github.com/MateenahJAHAN/USA-AI-Onboarding-learning-daily-update.git
cd USA-AI-Onboarding-learning-daily-update

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Running the Application

```bash
# Start the Flask API server
python app.py

# The server will be available at http://127.0.0.1:5000
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health-check — returns server status |
| `POST` | `/extract` | Submit clinical text and receive structured JSON |
| `GET` | `/extract/<job_id>` | Retrieve results of a previous extraction |
| `POST` | `/agent/invoke` | Directly invoke an LLM agent with a prompt |

---

## Example Usage

```bash
# Health check
curl http://127.0.0.1:5000/health

# Submit clinical text for extraction
curl -X POST http://127.0.0.1:5000/extract \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Patient John Doe, 45M, presents with chest pain radiating to left arm. BP 140/90. History of hypertension.",
    "extract_fields": ["patient_name", "age", "sex", "symptoms", "vitals", "medical_history"]
  }'
```

**Sample Response:**

```json
{
  "job_id": "ext_abc123",
  "status": "completed",
  "data": {
    "patient_name": "John Doe",
    "age": 45,
    "sex": "M",
    "symptoms": ["chest pain", "radiating to left arm"],
    "vitals": {"blood_pressure": "140/90"},
    "medical_history": ["hypertension"]
  }
}
```

---

## Development

```bash
# Run tests
pytest tests/ -v

# Run linter
flake8 src/ api/ agents/ mcp/ workflows/
```

---

## Roadmap

- [ ] PDF ingestion with OCR (Tesseract / AWS Textract)
- [ ] Multi-agent pipeline with specialist extractors (medications, diagnoses, procedures)
- [ ] MCP-compliant tool registry for plug-and-play agent capabilities
- [ ] Deployment configuration (Docker, Gunicorn, AWS Lambda)
- [ ] Evaluation harness with clinical NER benchmarks

---

## License

This project is for demonstration and educational purposes.

---

## Author

**Mateenah Jahan**
AI Scientist candidate — building intelligent agents for clinical data extraction.
