import responses
import requests
import pytest

@responses.activate
def test_mocked_get_user():
    responses.add(
        method=responses.GET,
        url="https://jsonplaceholder.typicode.com/users/1",
        json={"id": 1, "name": "Fake User", "email": "fake@test.com"},
        status=200
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Fake User"

@responses.activate
def test_mocked_server_error():
    responses.add(
        method=responses.GET,
        url="https://jsonplaceholder.typicode.com/users/1",
        json={"error": "Internal Server Error"},
        status=500
    )

    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 500
