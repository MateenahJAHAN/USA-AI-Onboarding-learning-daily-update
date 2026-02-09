"""
Tests for API endpoints.

Run with:  pytest tests/test_api.py -v
"""

import json
import pytest

from app import create_app


@pytest.fixture
def client():
    """Create a Flask test client."""
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    """GET /health returns 200 and status healthy."""
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "success"
    assert data["data"]["status"] == "healthy"


def test_extract_missing_body(client):
    """POST /extract with no body returns 422."""
    resp = client.post("/extract", content_type="application/json", data="{}")
    assert resp.status_code == 422


def test_extract_valid(client, mocker):
    """POST /extract with valid payload returns 201 and structured data."""
    # Mock the LLM call so tests don't need an API key
    mock_result = {"patient_name": "Jane Doe", "age": 42}
    mocker.patch(
        "agents.clinical_extractor.ClinicalExtractorAgent.extract",
        return_value=mock_result,
    )

    payload = {
        "text": "Patient Jane Doe, 42F, presents with headache.",
        "extract_fields": ["patient_name", "age"],
    }
    resp = client.post(
        "/extract",
        content_type="application/json",
        data=json.dumps(payload),
    )
    assert resp.status_code == 201
    body = resp.get_json()
    assert body["data"]["data"]["patient_name"] == "Jane Doe"
