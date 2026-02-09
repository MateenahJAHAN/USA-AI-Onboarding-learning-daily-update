"""
Clinical Agent — orchestrates prompt construction, LLM call, and response parsing.
"""

from __future__ import annotations

import json
import logging
from typing import Any, Dict, Optional

from src.agents.prompts import EXTRACTION_SYSTEM_PROMPT, EXTRACTION_USER_TEMPLATE
from src.integrations.openai_client import call_chat_completion

logger = logging.getLogger(__name__)


class ClinicalAgent:
    """
    An LLM-powered agent that extracts structured clinical data from
    unstructured text (PDFs, physician notes, lab reports).
    """

    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def extract(
        self,
        clinical_text: str,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Extract structured entities from *clinical_text*.

        Parameters
        ----------
        clinical_text : str
            Raw clinical note / PDF text.
        context : dict, optional
            MCP context block injected into the system prompt.

        Returns
        -------
        dict
            Parsed JSON with keys like ``diagnoses``, ``medications``, etc.
        """
        system_msg = EXTRACTION_SYSTEM_PROMPT
        if context:
            system_msg += f"\n\n### Context (MCP)\n```json\n{json.dumps(context, indent=2)}\n```"

        user_msg = EXTRACTION_USER_TEMPLATE.format(clinical_text=clinical_text)

        raw = call_chat_completion(
            api_key=self.api_key,
            model=self.model,
            system_message=system_msg,
            user_message=user_msg,
        )

        return self._parse_response(raw)

    def run(
        self,
        prompt: str,
        context: Optional[Dict[str, Any]] = None,
        system_message: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Generic agent invocation — send an arbitrary prompt to the LLM.

        Returns the raw assistant reply wrapped in a dict.
        """
        sys_msg = system_message or EXTRACTION_SYSTEM_PROMPT
        if context:
            sys_msg += f"\n\n### Context (MCP)\n```json\n{json.dumps(context, indent=2)}\n```"

        raw = call_chat_completion(
            api_key=self.api_key,
            model=self.model,
            system_message=sys_msg,
            user_message=prompt,
        )

        # Try to parse as JSON; fall back to plain text.
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            return {"response": raw}

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_response(raw: str) -> Dict[str, Any]:
        """Attempt to parse the LLM output as JSON."""
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            logger.warning("LLM response was not valid JSON — returning raw text.")
            return {
                "raw": raw,
                "diagnoses": [],
                "medications": [],
                "procedures": [],
                "lab_values": {},
                "summary": raw,
            }
