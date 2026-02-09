"""
Tests for the ClinicalAgent — unit-level (mocked LLM calls).
"""

import json
import sys
import os
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.agents.clinical_agent import ClinicalAgent


SAMPLE_LLM_RESPONSE = json.dumps(
    {
        "diagnoses": ["Type 2 Diabetes Mellitus"],
        "medications": ["Metformin 500mg PO BID"],
        "procedures": [],
        "lab_values": {"HbA1c": "7.2%", "glucose_fasting": "130 mg/dL"},
        "summary": "Patient diagnosed with T2DM, started on Metformin.",
    }
)


@patch("src.agents.clinical_agent.call_chat_completion", return_value=SAMPLE_LLM_RESPONSE)
def test_extract_returns_structured_data(mock_llm):
    agent = ClinicalAgent(api_key="test-key")
    result = agent.extract("Patient has elevated HbA1c of 7.2%.")
    assert "diagnoses" in result
    assert result["diagnoses"] == ["Type 2 Diabetes Mellitus"]
    mock_llm.assert_called_once()


@patch("src.agents.clinical_agent.call_chat_completion", return_value="plain text reply")
def test_extract_handles_non_json(mock_llm):
    agent = ClinicalAgent(api_key="test-key")
    result = agent.extract("Some clinical note.")
    assert "raw" in result
    assert result["summary"] == "plain text reply"


@patch("src.agents.clinical_agent.call_chat_completion", return_value=SAMPLE_LLM_RESPONSE)
def test_run_generic_prompt(mock_llm):
    agent = ClinicalAgent(api_key="test-key")
    result = agent.run("Summarise this report.")
    assert "diagnoses" in result
