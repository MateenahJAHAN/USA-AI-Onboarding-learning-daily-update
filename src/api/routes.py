"""
Flask Blueprint — API route definitions.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict

from flask import Blueprint, current_app, jsonify, request

api_bp = Blueprint("api", __name__)

# In-memory store for extraction jobs (swap for a database in production).
_jobs: Dict[str, Dict[str, Any]] = {}


# --------------------------------------------------------------------------
# Health check
# --------------------------------------------------------------------------

@api_bp.route("/health", methods=["GET"])
def health():
    """Liveness / readiness probe."""
    return jsonify({"status": "ok"})


# --------------------------------------------------------------------------
# Clinical extraction
# --------------------------------------------------------------------------

@api_bp.route("/extract", methods=["POST"])
def extract():
    """
    Accept unstructured clinical text and run the LLM agent to extract
    structured data.

    Request body (JSON):
        {
            "text": "Patient presents with ...",
            "context": { ... }          # optional MCP context payload
        }

    Returns:
        201 with a job_id that can be polled via GET /extract/<job_id>.
    """
    payload = request.get_json(silent=True) or {}
    clinical_text = payload.get("text", "").strip()

    if not clinical_text:
        return jsonify({"error": "Field 'text' is required and must not be empty."}), 400

    # --- Run the agent pipeline -------------------------------------------
    from src.agents.clinical_agent import ClinicalAgent
    from src.mcp.context import build_context

    api_key = current_app.config.get("OPENAI_API_KEY", "")
    context = build_context(payload.get("context"))
    agent = ClinicalAgent(api_key=api_key)
    result = agent.extract(clinical_text, context=context)

    # Store result
    job_id = str(uuid.uuid4())
    _jobs[job_id] = {"status": "completed", "result": result}

    return jsonify({"job_id": job_id, "status": "completed", "result": result}), 201


@api_bp.route("/extract/<job_id>", methods=["GET"])
def get_extraction(job_id: str):
    """Retrieve extraction results by job ID."""
    job = _jobs.get(job_id)
    if job is None:
        return jsonify({"error": "Job not found."}), 404
    return jsonify({"job_id": job_id, **job})


# --------------------------------------------------------------------------
# Agent trigger (generic)
# --------------------------------------------------------------------------

@api_bp.route("/agent/run", methods=["POST"])
def agent_run():
    """
    Generic endpoint to trigger the clinical AI agent.

    Request body (JSON):
        {
            "prompt": "Summarise the following lab report: ...",
            "system_message": "You are a clinical data extraction assistant.",
            "context": { ... }
        }
    """
    payload = request.get_json(silent=True) or {}
    prompt = payload.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Field 'prompt' is required."}), 400

    from src.agents.clinical_agent import ClinicalAgent
    from src.mcp.context import build_context

    api_key = current_app.config.get("OPENAI_API_KEY", "")
    context = build_context(payload.get("context"))
    system_message = payload.get("system_message")

    agent = ClinicalAgent(api_key=api_key)
    result = agent.run(prompt, context=context, system_message=system_message)

    return jsonify({"status": "completed", "result": result}), 200
