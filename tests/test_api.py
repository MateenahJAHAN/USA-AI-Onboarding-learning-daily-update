import os

from src.api.app import create_app


def _make_client():
    os.environ["CLINICAL_AGENT_MOCK"] = "1"
    app = create_app()
    return app.test_client()


def test_health_endpoint():
    client = _make_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_extract_requires_text():
    client = _make_client()
    response = client.post("/extract", json={})
    assert response.status_code == 400
