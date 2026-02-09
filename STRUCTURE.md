# Repository Refactoring Guide

> How to reorganise the daily-log folders into a professional, production-style project layout.

---

## Current Structure (Daily Logs)

```
USA-AI-Onboarding-learning-daily-update/
├── DAY 1 - README.md                        # Learning notes — API fundamentals
├── Day-2/
│   ├── database-relation-sql
│   ├── Day 2 ReadME -SQL-JSON
│   └── json.txt
├── Day-3/
│   └── day 3-README.md
├── Day-4/
│   ├── day4_python_api.py                    # Jupyter notebook (large, mixed content)
│   └── README.md
├── Day-5/
│   ├── edabit solution py
│   ├── random -user -py
│   └── README.md
├── day 6/
│   ├── flask loan api builder
│   ├── python -practice-py
│   └── README.md
├── day 7/
│   ├── flask_api.py                          # ← Flask CRUD API (key file)
│   ├── api_request.py                        # ← GET/POST demos with requests
│   └── ReadMe
├── Day 8/
│   ├── day_8_openai_api.py                   # ← OpenAI chat completion (key file)
│   ├── day_8_github_api.py                   # ← GitHub API GET
│   ├── day_8_jsonplaceholder_api.py          # ← JSONPlaceholder GET
│   ├── day_8_delete_post.py                  # ← DELETE request demo
│   ├── day_8_put_request.py                  # ← PUT request demo
│   └── README.md
├── day 9/
│   ├── weather_kashmir.py                    # ← OpenWeatherMap API
│   └── README.md
├── DAY 10/
│   ├── openai_api_dcrud.py                   # ← OpenAI CRUD simulation (key file)
│   ├── github_get_issue.py                   # ← GitHub issue GET
│   ├── github_post_issue.py                  # ← GitHub issue POST
│   ├── github_patch_issue.py                 # ← GitHub issue PATCH
│   ├── github_close_issue.py                 # ← GitHub issue CLOSE
│   └── README.md
├── day 11/
│   ├── main.py                               # ← FastAPI CRUD app (key file)
│   ├── sets_and_Tuples (1).ipynb
│   └── README.md
└── day 12/
    └── README.md/.py/ipynb/
        ├── chat_completion.py                # ← OpenAI via python-dotenv (key file)
        ├── get_posts.py                      # ← GET posts with env vars
        ├── Function,_dictionary,_oops (2).ipynb
        └── ReadMe
```

---

## Proposed Professional Structure

```
clinical-ai-agent-prototypes/
│
├── README.md                    # Professional project README
├── STRUCTURE.md                 # This file — refactoring guide
├── requirements.txt             # Pinned Python dependencies
├── .env.example                 # Template for environment variables
├── .gitignore                   # Ignore .env, __pycache__, .venv, etc.
│
├── src/                         # ── All production source code ──
│   │
│   ├── app.py                   # Flask entry point — registers blueprints, starts server
│   ├── config.py                # Loads env vars, defines Config dataclass
│   │
│   ├── api/                     # ── REST API layer ──
│   │   ├── __init__.py
│   │   ├── routes.py            # Blueprint with /health, /extract, /agent/run endpoints
│   │   └── schemas.py           # Pydantic models for request/response validation
│   │
│   ├── agents/                  # ── LLM Agent logic ──
│   │   ├── __init__.py
│   │   ├── clinical_agent.py    # Main agent class — orchestrates prompt → LLM → parse
│   │   └── prompts.py           # System & user prompt templates for clinical extraction
│   │
│   ├── mcp/                     # ── Model Context Protocol ──
│   │   ├── __init__.py
│   │   └── context.py           # Context builders: assemble patient data, lab ranges, etc.
│   │
│   └── integrations/            # ── External API wrappers ──
│       ├── __init__.py
│       ├── openai_client.py     # Thin wrapper around OpenAI Chat Completion
│       └── github_client.py     # GitHub issue CRUD helper
│
├── notebooks/                   # ── Jupyter explorations (cleaned up) ──
│   ├── dictionaries_and_functions.ipynb
│   ├── sets_and_tuples.ipynb
│   └── function_dictionary_oops.ipynb
│
├── tests/                       # ── Unit & integration tests ──
│   ├── __init__.py
│   ├── test_routes.py           # Test API endpoints with Flask test client
│   └── test_clinical_agent.py   # Test agent prompt construction and parsing
│
└── legacy/                      # ── Original scripts preserved for reference ──
    ├── day_07_flask_api.py
    ├── day_07_api_request.py
    ├── day_08_openai_api.py
    ├── day_08_github_api.py
    ├── day_08_jsonplaceholder_api.py
    ├── day_08_delete_post.py
    ├── day_08_put_request.py
    ├── day_09_weather_api.py
    ├── day_10_openai_crud.py
    ├── day_10_github_get_issue.py
    ├── day_10_github_post_issue.py
    ├── day_10_github_patch_issue.py
    ├── day_10_github_close_issue.py
    ├── day_11_fastapi_main.py
    ├── day_12_chat_completion.py
    └── day_12_get_posts.py
```

---

## File-by-File Migration Map

This table shows exactly where each existing file should be moved (or merged) in the new structure.

| Current Location | Destination | Action |
|---|---|---|
| `day 7/flask_api.py` | `legacy/day_07_flask_api.py` | Copy to legacy; core logic refactored into `src/api/routes.py` |
| `day 7/api_request.py` | `legacy/day_07_api_request.py` | Copy to legacy |
| `Day 8/day_8_openai_api.py` | `legacy/day_08_openai_api.py` | Copy to legacy; logic refactored into `src/integrations/openai_client.py` |
| `Day 8/day_8_github_api.py` | `legacy/day_08_github_api.py` | Copy to legacy |
| `Day 8/day_8_jsonplaceholder_api.py` | `legacy/day_08_jsonplaceholder_api.py` | Copy to legacy |
| `Day 8/day_8_delete_post.py` | `legacy/day_08_delete_post.py` | Copy to legacy |
| `Day 8/day_8_put_request.py` | `legacy/day_08_put_request.py` | Copy to legacy |
| `day 9/weather_kashmir.py` | `legacy/day_09_weather_api.py` | Copy to legacy |
| `DAY 10/openai_api_dcrud.py` | `legacy/day_10_openai_crud.py` | Copy to legacy; agent patterns extracted into `src/agents/clinical_agent.py` |
| `DAY 10/github_get_issue.py` | `legacy/day_10_github_get_issue.py` | Copy to legacy; merged into `src/integrations/github_client.py` |
| `DAY 10/github_post_issue.py` | `legacy/day_10_github_post_issue.py` | Copy to legacy |
| `DAY 10/github_patch_issue.py` | `legacy/day_10_github_patch_issue.py` | Copy to legacy |
| `DAY 10/github_close_issue.py` | `legacy/day_10_github_close_issue.py` | Copy to legacy |
| `day 11/main.py` | `legacy/day_11_fastapi_main.py` | Copy to legacy; Pydantic patterns reused in `src/api/schemas.py` |
| `day 12/.../chat_completion.py` | `legacy/day_12_chat_completion.py` | Copy to legacy; pattern used in `src/integrations/openai_client.py` |
| `day 12/.../get_posts.py` | `legacy/day_12_get_posts.py` | Copy to legacy |
| `day 11/sets_and_Tuples (1).ipynb` | `notebooks/sets_and_tuples.ipynb` | Rename and move |
| `DAY 10/Day_10_...ipynb` | `notebooks/dictionaries_and_functions.ipynb` | Rename and move |
| `day 12/.../Function,_dictionary,_oops (2).ipynb` | `notebooks/function_dictionary_oops.ipynb` | Rename and move |

---

## Step-by-Step Refactoring Commands

Run these commands from the repository root to create the new structure:

```bash
# 1. Create the directory skeleton
mkdir -p src/api src/agents src/mcp src/integrations
mkdir -p notebooks tests legacy

# 2. Create Python package __init__.py files
touch src/__init__.py src/api/__init__.py src/agents/__init__.py
touch src/mcp/__init__.py src/integrations/__init__.py
touch tests/__init__.py

# 3. Move scripts into legacy/ (preserving originals)
cp "day 7/flask_api.py"                         legacy/day_07_flask_api.py
cp "day 7/api_request.py"                       legacy/day_07_api_request.py
cp "Day 8/day_8_openai_api.py"                  legacy/day_08_openai_api.py
cp "Day 8/day_8_github_api.py"                  legacy/day_08_github_api.py
cp "Day 8/day_8_jsonplaceholder_api.py"         legacy/day_08_jsonplaceholder_api.py
cp "Day 8/day_8_delete_post.py"                 legacy/day_08_delete_post.py
cp "Day 8/day_8_put_request.py"                 legacy/day_08_put_request.py
cp "day 9/weather_kashmir.py"                   legacy/day_09_weather_api.py
cp "DAY 10/openai_api_dcrud.py"                 legacy/day_10_openai_crud.py
cp "DAY 10/github_get_issue.py"                 legacy/day_10_github_get_issue.py
cp "DAY 10/github_post_issue.py"                legacy/day_10_github_post_issue.py
cp "DAY 10/github_patch_issue.py"               legacy/day_10_github_patch_issue.py
cp "DAY 10/github_close_issue.py"               legacy/day_10_github_close_issue.py
cp "day 11/main.py"                             legacy/day_11_fastapi_main.py
cp "day 12 /README.md/.py/ipynb/chat_completion.py"  legacy/day_12_chat_completion.py
cp "day 12 /README.md/.py/ipynb/get_posts.py"        legacy/day_12_get_posts.py

# 4. Move notebooks
cp "day 11/sets_and_Tuples (1).ipynb"                        notebooks/sets_and_tuples.ipynb
cp "DAY 10/Day_10_–_Python_Dictionaries_and_function_Practice.ipynb" notebooks/dictionaries_and_functions.ipynb
cp "day 12 /README.md/.py/ipynb/Function,_dictionary,_oops (2).ipynb" notebooks/function_dictionary_oops.ipynb

# 5. Create config & env template
# (see file contents below)
```

---

## Key Principles Behind the Reorganisation

| Principle | How it is applied |
|---|---|
| **Separation of concerns** | API routes, agent logic, context management, and external integrations each live in their own module |
| **Single entry point** | `src/app.py` is the only file you run — it registers all blueprints and starts the server |
| **Configuration in one place** | `src/config.py` loads all env vars; no scattered `api_key = "..."` strings |
| **No secrets in code** | `.env.example` documents required variables; `.gitignore` excludes `.env` |
| **Legacy preservation** | Original daily scripts are kept in `legacy/` so nothing is lost |
| **Testability** | Business logic is in importable modules; `tests/` can import and exercise them directly |

---

## What Each New Module Does

### `src/app.py`
The Flask application factory. Creates the app, loads config, registers the API blueprint, and starts the dev server.

### `src/config.py`
Reads `.env` via `python-dotenv` and exposes a `Config` class with typed attributes (`OPENAI_API_KEY`, `FLASK_PORT`, etc.).

### `src/api/routes.py`
A Flask `Blueprint` that defines the HTTP endpoints (`/health`, `/extract`, `/agent/run`). Each route handler validates input, calls the agent layer, and returns JSON.

### `src/api/schemas.py`
Pydantic models (or dataclasses) for request and response payloads. Evolved from the `Item` model in the Day 11 FastAPI code.

### `src/agents/clinical_agent.py`
The core LLM agent. Takes raw clinical text, builds a prompt using `prompts.py`, calls the OpenAI client, and parses the structured response. Evolved from the Day 10 `openai_api_dcrud.py` patterns.

### `src/agents/prompts.py`
String templates for system and user messages. Keeps prompt engineering separate from orchestration logic.

### `src/mcp/context.py`
Builds MCP-compliant context blocks — structured JSON payloads containing patient demographics, lab reference ranges, medication formularies, etc. — that get injected into the agent's system prompt.

### `src/integrations/openai_client.py`
A thin wrapper around the OpenAI Python SDK. Handles authentication, retry logic, and response parsing. Consolidates patterns from Day 8 and Day 12 scripts.

### `src/integrations/github_client.py`
A reusable GitHub API client that supports GET, POST, PATCH, and CLOSE operations on issues. Consolidated from the four Day 10 scripts.
