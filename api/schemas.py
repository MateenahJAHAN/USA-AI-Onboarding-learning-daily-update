"""
Pydantic models for request validation and response serialisation.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Request schemas
# ---------------------------------------------------------------------------

class ExtractionRequest(BaseModel):
    """Payload sent to POST /extract."""

    text: str = Field(
        ...,
        min_length=1,
        description="Raw clinical text to process.",
    )
    extract_fields: List[str] = Field(
        default_factory=lambda: [
            "patient_name",
            "age",
            "sex",
            "symptoms",
            "vitals",
            "medical_history",
        ],
        description="List of field names to extract from the text.",
    )


class AgentInvokeRequest(BaseModel):
    """Payload sent to POST /agent/invoke."""

    prompt: str = Field(..., min_length=1, description="Prompt for the LLM agent.")
    model: Optional[str] = Field(None, description="Override the default model.")
    temperature: Optional[float] = Field(None, ge=0.0, le=2.0)


# ---------------------------------------------------------------------------
# Response schemas
# ---------------------------------------------------------------------------

class ExtractionResponse(BaseModel):
    """Response returned by POST /extract."""

    job_id: str
    status: str = "completed"
    data: dict


class HealthResponse(BaseModel):
    """Response returned by GET /health."""

    status: str = "healthy"
    version: str = "0.1.0"
