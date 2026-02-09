from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

from openai import OpenAI


PROMPT_PATH = Path(__file__).resolve().parent / "prompts" / "clinical_extraction.md"


def _load_system_prompt() -> str:
    try:
        return PROMPT_PATH.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return "You are a clinical data extraction agent. Return JSON only."


class ClinicalAgent:
    def __init__(
        self,
        model: str | None = None,
        api_key: str | None = None,
        mock: bool | None = None,
    ) -> None:
        if mock is None:
            mock = os.getenv("CLINICAL_AGENT_MOCK", "").lower() in {"1", "true", "yes"}

        self.mock = mock
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.system_prompt = _load_system_prompt()

        if self.mock:
            self.client = None
            return

        resolved_key = api_key or os.getenv("OPENAI_API_KEY")
        if not resolved_key:
            raise RuntimeError("OPENAI_API_KEY is required for real LLM calls.")

        self.client = OpenAI(api_key=resolved_key)

    def extract_structured_data(self, text: str) -> Dict[str, Any]:
        if self.mock:
            return {
                "patient": {"name": None, "dob": None, "sex": None, "mrn": None},
                "diagnoses": [],
                "medications": [],
                "procedures": [],
                "allergies": [],
                "labs": [],
                "vitals": [],
                "encounter_date": None,
                "confidence": 0.0,
            }

        if not self.client:
            raise RuntimeError("OpenAI client is not initialized.")

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": text},
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.0,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content or "{}"
        try:
            return json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError("Model returned non-JSON content.") from exc
