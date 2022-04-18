from fastapi.testclient import TestClient
from api_endpoints.api_endpoints import api_endpoints

client = TestClient(api_endpoints)


def test_create_user() -> None:
    response = client.post("/users")
    assert response.status_code == 200


def test_get_user() -> None:
    response = client.get("/users")
    assert response.status_code == 405
