"""
Request / response schemas (Pydantic models).

These can be used for strict validation if you migrate to FastAPI,
or called manually for Flask request validation.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


# --------------------------------------------------------------------------
# Request schemas
# --------------------------------------------------------------------------

class ExtractionRequest(BaseModel):
    """Payload for POST /extract."""

    text: str = Field(..., min_length=1, description="Raw clinical text to process.")
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional MCP context payload (patient history, lab ranges, etc.).",
    )


class AgentRunRequest(BaseModel):
    """Payload for POST /agent/run."""

    prompt: str = Field(..., min_length=1, description="User prompt for the agent.")
    system_message: Optional[str] = Field(
        default=None,
        description="Override the default system message.",
    )
    context: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional MCP context payload.",
    )


# --------------------------------------------------------------------------
# Response schemas
# --------------------------------------------------------------------------

class ExtractionResult(BaseModel):
    """Structured output returned by the clinical agent."""

    diagnoses: List[str] = Field(default_factory=list)
    medications: List[str] = Field(default_factory=list)
    procedures: List[str] = Field(default_factory=list)
    lab_values: Dict[str, Any] = Field(default_factory=dict)
    summary: str = ""


class JobResponse(BaseModel):
    """Wrapper returned by the /extract endpoint."""

    job_id: str
    status: str
    result: Optional[ExtractionResult] = None
