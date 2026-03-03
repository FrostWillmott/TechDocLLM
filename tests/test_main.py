"""Unit tests for main FastAPI application."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint returns the expected message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_hello_endpoint():
    """Test hello endpoint with a name parameter."""
    response = client.get("/hello/John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello John"}


def test_hello_endpoint_with_special_characters():
    """Test hello endpoint with special characters in the name."""
    response = client.get("/hello/Иван")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Иван"}
