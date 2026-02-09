# Clinical AI Agent Prototypes for USA AI

> Prototypes for extracting structured data from unstructured clinical inputs (PDFs, free-text notes) using LLM-powered agents, RESTful APIs, and the Model Context Protocol (MCP).

---

## Overview

This repository contains a collection of working prototypes that demonstrate how Large Language Models (LLMs) can be orchestrated as intelligent agents to process unstructured clinical data — such as scanned PDFs, lab reports, and physician notes — and transform them into structured, machine-readable outputs.

Each prototype explores a different layer of the system:

| Layer | What it proves |
|---|---|
| **Flask / FastAPI Services** | RESTful endpoints that accept clinical documents, validate payloads, and return structured JSON |
| **LLM Workflow Orchestration** | Prompt-driven pipelines that call OpenAI chat-completion models to extract, classify, and summarise clinical information |
| **Model Context Protocol (MCP)** | A standardised interface for feeding rich context (patient history, lab ranges, formulary data) into LLM agents at inference time |
| **Third-Party API Integration** | Patterns for authenticating with and consuming external APIs (GitHub, OpenWeather, JSONPlaceholder) that mirror how production agents would call EHR/FHIR endpoints |

---

## Key Features

### 1. Flask API Development
- Full CRUD REST API built with Flask (Create, Read, Update, Delete)
- FastAPI variant with Pydantic request validation
- Proper HTTP status codes, error handling, and JSON response formatting
- Patterns for request authentication using Bearer tokens

### 2. LLM Workflow Orchestration
- OpenAI Chat Completion integration (`gpt-3.5-turbo` / `gpt-4`)
- Prompt engineering for clinical data extraction
- Simulated CRUD lifecycle over LLM conversations (create, read, update context, reset)
- Environment-variable-based secret management with `python-dotenv`

### 3. Model Context Protocol (MCP) Implementation
- Context injection patterns for feeding structured medical data into LLM prompts
- System-message design for constraining agent behaviour to clinical domains
- Scalable architecture for adding new context sources (lab results, drug interactions, patient demographics)

### 4. External API Integration Patterns
- GitHub API: full issue lifecycle (GET, POST, PATCH, close) with token auth
- OpenWeatherMap API: real-time data retrieval and JSON parsing
- JSONPlaceholder: GET, POST, PUT, DELETE request demonstrations
- Reusable request helpers with error handling

---

## Tech Stack

| Category | Technologies |
|---|---|
| **Languages** | Python 3.10+ |
| **Web Frameworks** | Flask, FastAPI |
| **LLM APIs** | OpenAI API (GPT-3.5-Turbo, GPT-4) |
| **Protocols** | Model Context Protocol (MCP), REST / HTTP |
| **Data Validation** | Pydantic |
| **Auth & Secrets** | python-dotenv, Bearer token auth |
| **HTTP Clients** | `requests`, `httpx` |
| **Dev Tools** | Jupyter Notebook, Git, pip |

---

## Repository Structure

```
clinical-ai-agent-prototypes/
├── README.md
├── STRUCTURE.md              # Detailed refactoring guide (current → proposed)
├── requirements.txt
├── .env.example
│
├── src/
│   ├── app.py                # Main Flask entry point — starts the API server
│   ├── config.py             # Centralised configuration & env-var loading
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py         # Flask route definitions (Blueprints)
│   │   └── schemas.py        # Request / response schemas
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── clinical_agent.py # LLM agent for clinical data extraction
│   │   └── prompts.py        # System & user prompt templates
│   │
│   ├── mcp/
│   │   ├── __init__.py
│   │   └── context.py        # MCP context builders
│   │
│   └── integrations/
│       ├── __init__.py
│       ├── openai_client.py  # OpenAI API wrapper
│       └── github_client.py  # GitHub API helper (issue CRUD)
│
├── notebooks/
│   ├── dictionaries_and_functions.ipynb
│   ├── sets_and_tuples.ipynb
│   └── function_dictionary_oops.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   └── test_clinical_agent.py
│
└── legacy/                   # Original daily-log scripts (preserved for reference)
    ├── day_07_flask_api.py
    ├── day_08_openai_api.py
    ├── day_09_weather_api.py
    ├── day_10_github_crud.py
    ├── day_11_fastapi.py
    └── day_12_chat_completion.py
```

> See **[STRUCTURE.md](STRUCTURE.md)** for a detailed mapping from the current daily-log folders to the proposed professional layout.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/MateenahJAHAN/USA-AI-Onboarding-learning-daily-update.git
cd USA-AI-Onboarding-learning-daily-update

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run the Flask API server
python src/app.py
```

The API will be available at `http://127.0.0.1:5000/`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health-check / liveness probe |
| `POST` | `/extract` | Submit a clinical document for LLM-based extraction |
| `GET` | `/extract/<job_id>` | Retrieve extraction results |
| `POST` | `/agent/run` | Trigger the clinical AI agent pipeline |

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Your OpenAI API key |
| `FLASK_ENV` | No | `development` or `production` (default: `development`) |
| `FLASK_PORT` | No | Port for the Flask server (default: `5000`) |
| `LOG_LEVEL` | No | Logging verbosity (default: `INFO`) |

---

## How It Works

```
┌──────────────┐     POST /extract      ┌──────────────────┐
│  Client      │ ──────────────────────► │  Flask API       │
│  (PDF/text)  │                         │  src/api/routes  │
└──────────────┘                         └────────┬─────────┘
                                                  │
                                         ┌────────▼─────────┐
                                         │  MCP Context      │
                                         │  src/mcp/context  │
                                         └────────┬─────────┘
                                                  │  inject context
                                         ┌────────▼─────────┐
                                         │  Clinical Agent   │
                                         │  src/agents/      │
                                         └────────┬─────────┘
                                                  │  call LLM
                                         ┌────────▼─────────┐
                                         │  OpenAI API       │
                                         │  (GPT-4)          │
                                         └────────┬─────────┘
                                                  │
                                         ┌────────▼─────────┐
                                         │  Structured JSON  │
                                         │  Response         │
                                         └──────────────────┘
```

1. **Client** sends an unstructured clinical document (PDF text, physician note) via `POST /extract`.
2. **Flask API** validates the request and hands it to the agent pipeline.
3. **MCP Context Builder** assembles relevant medical context (lab reference ranges, patient history) into a structured prompt context block.
4. **Clinical Agent** constructs the final prompt, calls the OpenAI Chat Completion API, and parses the structured output.
5. **Structured JSON** (diagnosis codes, medication lists, extracted entities) is returned to the client.

---

## License

This project is provided for educational and demonstration purposes.

---

## Author

**Mateenah Jahan**
AI Scientist Candidate | LLM Agent Development | Clinical AI Prototyping
