"""
Extraction Pipeline
====================
End-to-end orchestration that chains the document parser and the clinical
extractor agent into a single pipeline:

    raw document  →  parse  →  extract  →  structured JSON

Usage::

    from workflows.extraction_pipeline import run_extraction

    result = run_extraction(
        raw_text="Patient Jane Doe ...",
        fields=["patient_name", "age", "diagnoses"],
    )
"""

from typing import List, Optional

from agents.document_parser import DocumentParserAgent
from agents.clinical_extractor import ClinicalExtractorAgent
from mcp.context_manager import ContextManager
from src.utils import generate_job_id, get_logger

logger = get_logger(__name__)


def run_extraction(
    raw_text: str,
    fields: Optional[List[str]] = None,
    source_type: str = "text",
) -> dict:
    """
    Run the full extraction pipeline.

    Parameters
    ----------
    raw_text : str
        The raw clinical document (text or PDF placeholder).
    fields : list[str], optional
        Fields to extract.  Defaults to a clinical standard set.
    source_type : str
        ``"text"`` or ``"pdf"``.

    Returns
    -------
    dict
        ``{"job_id": ..., "status": ..., "data": {...}}``
    """
    if fields is None:
        fields = [
            "patient_name",
            "age",
            "sex",
            "symptoms",
            "vitals",
            "diagnoses",
            "medications",
            "medical_history",
        ]

    job_id = generate_job_id()
    logger.info("Starting extraction pipeline — job_id=%s", job_id)

    # 1. Parse / normalise the raw document
    parser = DocumentParserAgent()
    clean_text = parser.parse(raw_text, source_type=source_type)

    # 2. (Optional) Track context via MCP
    ctx = ContextManager()
    ctx.add_message("user", clean_text)

    # 3. Extract structured data via LLM agent
    extractor = ClinicalExtractorAgent()
    extracted = extractor.extract(clean_text, fields)

    logger.info("Pipeline complete — job_id=%s", job_id)
    return {
        "job_id": job_id,
        "status": "completed",
        "data": extracted,
    }
