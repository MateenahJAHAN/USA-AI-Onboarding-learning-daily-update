"""
ClinicalExtractorAgent
======================
An LLM agent specialised in extracting structured clinical data from
unstructured free-text medical notes, discharge summaries, and similar
documents.

Usage::

    agent = ClinicalExtractorAgent()
    result = agent.extract(
        text="Patient Jane Doe, 62F, diagnosed with Type-2 diabetes ...",
        fields=["patient_name", "age", "sex", "diagnoses"],
    )
"""

import json
from typing import List, Optional

from agents.base_agent import BaseAgent
from src.utils import get_logger

logger = get_logger(__name__)

SYSTEM_PROMPT = (
    "You are a clinical data extraction agent. "
    "Given unstructured medical text, extract the requested fields and "
    "return ONLY valid JSON — no markdown fences, no commentary. "
    "If a field cannot be determined from the text, set its value to null."
)


class ClinicalExtractorAgent(BaseAgent):
    """Agent that converts free-text clinical notes into structured JSON."""

    def __init__(self, model: Optional[str] = None, temperature: Optional[float] = None):
        super().__init__(
            model=model,
            temperature=temperature if temperature is not None else 0.1,
            system_prompt=SYSTEM_PROMPT,
        )

    # ── core extraction ────────────────────────────────────────────────────

    def extract(self, text: str, fields: List[str]) -> dict:
        """
        Extract *fields* from *text* using the LLM.

        Parameters
        ----------
        text : str
            Raw clinical text (e.g. a discharge summary).
        fields : list[str]
            Names of the data elements to extract.

        Returns
        -------
        dict
            A mapping of field names to extracted values.
        """
        fields_csv = ", ".join(fields)
        prompt = (
            f"Extract the following fields from the clinical text below.\n"
            f"Fields: {fields_csv}\n\n"
            f"--- CLINICAL TEXT ---\n{text}\n--- END ---\n\n"
            f"Return ONLY a JSON object with those fields as keys."
        )
        raw = self.invoke(prompt)
        return self._parse_json(raw, fields)

    # ── invoke (satisfies abstract base) ───────────────────────────────────

    def invoke(self, prompt: str) -> str:
        """Send a single prompt to the LLM and return the raw reply."""
        messages = self._build_messages(prompt)
        return self._call_llm(messages)

    # ── internal helpers ───────────────────────────────────────────────────

    @staticmethod
    def _parse_json(raw: str, expected_fields: List[str]) -> dict:
        """Best-effort JSON parsing with fallback."""
        # Strip markdown code-fences if present
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[-1]
        if cleaned.endswith("```"):
            cleaned = cleaned.rsplit("```", 1)[0]

        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError:
            logger.warning("LLM returned non-JSON — wrapping raw text")
            data = {field: None for field in expected_fields}
            data["_raw"] = raw

        return data
