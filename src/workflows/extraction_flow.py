from __future__ import annotations

from typing import Any, Dict

from src.agents.clinical_agent import ClinicalAgent
from src.schemas.clinical import ClinicalExtraction


class ExtractionWorkflow:
    def __init__(self, agent: ClinicalAgent | None = None) -> None:
        self.agent = agent or ClinicalAgent()

    def run_from_text(self, text: str, metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        raw = self.agent.extract_structured_data(text)
        validated = ClinicalExtraction.model_validate(raw)
        output = validated.model_dump()
        if metadata:
            output["metadata"] = metadata
        return output
