from __future__ import annotations

from typing import Dict, List


def get_tool_specs() -> List[Dict[str, object]]:
    return [
        {
            "name": "clinical_extraction",
            "description": "Extract structured clinical data from free-text notes.",
            "input_schema": {
                "type": "object",
                "properties": {"text": {"type": "string"}},
                "required": ["text"],
            },
        }
    ]
