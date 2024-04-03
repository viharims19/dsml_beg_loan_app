import pytest
import json

from app import app


@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, the endpoint is working!!!"}


















