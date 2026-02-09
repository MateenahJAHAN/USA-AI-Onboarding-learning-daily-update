"""
Model Context Protocol (MCP) — context builders.

These helpers assemble structured context payloads that are injected into
the LLM agent's system prompt at inference time.  In a production system
these would pull data from EHR/FHIR APIs, lab databases, or formulary
services.
"""

from __future__ import annotations

from typing import Any, Dict, Optional


def build_context(raw: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    """
    Build an MCP-compliant context block from a raw dict.

    If *raw* is ``None`` or empty, returns ``None`` (no context injected).
    Otherwise, it normalises the payload and attaches default reference data.
    """
    if not raw:
        return None

    context: Dict[str, Any] = {
        "mcp_version": "0.1",
        "source": raw.get("source", "user_provided"),
    }

    # --- Patient demographics (if supplied) --------------------------------
    if "patient" in raw:
        context["patient"] = {
            "age": raw["patient"].get("age"),
            "sex": raw["patient"].get("sex"),
            "medical_history": raw["patient"].get("medical_history", []),
        }

    # --- Lab reference ranges (defaults) -----------------------------------
    context["lab_reference_ranges"] = raw.get(
        "lab_reference_ranges",
        {
            "hemoglobin": {"min": 12.0, "max": 17.5, "unit": "g/dL"},
            "WBC": {"min": 4.5, "max": 11.0, "unit": "x10^9/L"},
            "platelet": {"min": 150, "max": 400, "unit": "x10^9/L"},
            "creatinine": {"min": 0.6, "max": 1.2, "unit": "mg/dL"},
            "glucose_fasting": {"min": 70, "max": 100, "unit": "mg/dL"},
        },
    )

    # --- Pass through any extra keys ---------------------------------------
    for key, value in raw.items():
        if key not in ("source", "patient", "lab_reference_ranges"):
            context[key] = value

    return context
