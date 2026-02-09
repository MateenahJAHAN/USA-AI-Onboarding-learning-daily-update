"""
Flask blueprint containing all API route definitions.

Endpoints
---------
GET   /health              — Health-check
POST  /extract             — Submit clinical text for structured extraction
GET   /extract/<job_id>    — Retrieve a previous extraction result
POST  /agent/invoke        — Directly invoke an LLM agent with a prompt
"""

from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from api.schemas import ExtractionRequest, AgentInvokeRequest
from agents.clinical_extractor import ClinicalExtractorAgent
from src.utils import generate_job_id, success_response, error_response, get_logger

logger = get_logger(__name__)

api_bp = Blueprint("api", __name__)

# In-memory results store (replace with a database in production)
_results: dict = {}


# ── Health ─────────────────────────────────────────────────────────────────

@api_bp.route("/health", methods=["GET"])
def health():
    """Return service health status."""
    return success_response({"status": "healthy", "version": "0.1.0"})


# ── Extraction ─────────────────────────────────────────────────────────────

@api_bp.route("/extract", methods=["POST"])
def extract():
    """
    Accept clinical free-text and return structured fields extracted by an
    LLM agent.
    """
    # Validate request body
    try:
        payload = ExtractionRequest(**request.get_json(force=True))
    except (ValidationError, TypeError) as exc:
        return error_response(str(exc), 422)

    # Run extraction agent
    agent = ClinicalExtractorAgent()
    extracted = agent.extract(payload.text, payload.extract_fields)

    job_id = generate_job_id()
    result = {"job_id": job_id, "status": "completed", "data": extracted}
    _results[job_id] = result

    logger.info("Extraction complete — job_id=%s", job_id)
    return success_response(result, 201)


@api_bp.route("/extract/<job_id>", methods=["GET"])
def get_extraction(job_id: str):
    """Retrieve a previously computed extraction result."""
    result = _results.get(job_id)
    if result is None:
        return error_response("Job not found", 404)
    return success_response(result)


# ── Agent invoke ───────────────────────────────────────────────────────────

@api_bp.route("/agent/invoke", methods=["POST"])
def invoke_agent():
    """Send an ad-hoc prompt to the LLM agent and return the response."""
    try:
        payload = AgentInvokeRequest(**request.get_json(force=True))
    except (ValidationError, TypeError) as exc:
        return error_response(str(exc), 422)

    agent = ClinicalExtractorAgent(
        model=payload.model,
        temperature=payload.temperature,
    )
    response_text = agent.invoke(payload.prompt)

    return success_response({"response": response_text})
