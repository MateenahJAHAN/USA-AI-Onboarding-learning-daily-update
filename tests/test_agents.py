"""
Unit tests for agent classes.

Run with:  pytest tests/test_agents.py -v
"""

import json
import pytest

from agents.clinical_extractor import ClinicalExtractorAgent
from agents.document_parser import DocumentParserAgent


# ---------------------------------------------------------------------------
# DocumentParserAgent
# ---------------------------------------------------------------------------

class TestDocumentParser:
    def test_normalise_whitespace(self):
        parser = DocumentParserAgent()
        raw = "Hello   world\r\n\r\n\r\nfoo"
        result = parser.parse(raw)
        assert "   " not in result
        assert "\r" not in result
        assert "\n\n\n" not in result

    def test_pdf_placeholder(self):
        parser = DocumentParserAgent()
        result = parser.parse("some content", source_type="pdf")
        assert result == "some content"


# ---------------------------------------------------------------------------
# ClinicalExtractorAgent — JSON parsing logic (no LLM call needed)
# ---------------------------------------------------------------------------

class TestClinicalExtractorParsing:
    def test_parse_valid_json(self):
        raw = '{"patient_name": "John", "age": 30}'
        result = ClinicalExtractorAgent._parse_json(raw, ["patient_name", "age"])
        assert result["patient_name"] == "John"

    def test_parse_fenced_json(self):
        raw = '```json\n{"name": "Jane"}\n```'
        result = ClinicalExtractorAgent._parse_json(raw, ["name"])
        assert result["name"] == "Jane"

    def test_parse_invalid_json(self):
        raw = "This is not JSON at all"
        result = ClinicalExtractorAgent._parse_json(raw, ["field_a"])
        assert result["field_a"] is None
        assert "_raw" in result
