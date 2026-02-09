"""
Tests for API routes — uses the Flask test client (no real LLM calls).
"""

import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "running"


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_extract_missing_text(client):
    resp = client.post("/extract", json={})
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_agent_run_missing_prompt(client):
    resp = client.post("/agent/run", json={})
    assert resp.status_code == 400
    assert "error" in resp.get_json()
