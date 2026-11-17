import pytest
from app import app, read_root, get_version, get_status

def test_read_root():
    data = read_root()
    assert isinstance(data, dict)
    assert data["version"] == "2.0.0"
    assert "hostname_contenedor" in data

def test_get_version():
    data = get_version()
    assert isinstance(data, dict)
    assert data["version"] == "2.0.0"
    assert data["release"] == "v2.0.0"
    assert "mejoras" in data

def test_get_status():
    data = get_status()
    assert isinstance(data, dict)
    assert data["status"] == "activo"
    assert data["estado"] == "operativo v2"
    assert data["version"] == "2.0.0"

try:
    from fastapi.testclient import TestClient
    client = TestClient(app)

    def test_http_version():
        response = client.get("/version")
        assert response.status_code == 200
        assert response.json()["version"] == "2.0.0"

    def test_http_status():
        response = client.get("/status")
        assert response.status_code == 200
        assert response.json()["status"] == "activo"
except (ImportError, RuntimeError):
    pass
