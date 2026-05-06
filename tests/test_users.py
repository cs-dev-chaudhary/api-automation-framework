import requests
import pytest
import json
import os
import allure

def load_test_data():
    path = os.path.join(os.path.dirname(__file__), "..", "test_data", "users.json")
    with open(path) as f:
        return json.load(f)

test_data = load_test_data()


@pytest.mark.parametrize("user_id", test_data["valid_users"])
def test_get_multiple_users(client, user_id):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200

@pytest.mark.parametrize("user_id", test_data["valid_users"])
def test_valid_users_return_200(client, user_id):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200



@pytest.mark.smoke
@allure.title("Verify GET /users/1 returns 200")
@allure.description("Checks that the user endpoint is reachable and returns success")
def test_get_user_returns_200(client):
    with allure.step("Send GET request to /users/1"):
        response = client.get("/users/1")
    with allure.step("Verify status code is 200"):
        assert response.status_code == 200


@pytest.mark.smoke
def test_get_user_returns_data(client):
    response = client.get("/users/1")
    data = response.json()
    assert data["name"] == "Leanne Graham"

def test_get_user_correct_name(client):
    response = client.get("/users/1")
    data = response.json()
    assert data["name"] == "Leanne Graham"

@allure.title("Verify POST /posts creates a new post")
@allure.description("Sends a POST request with title, body and userId and expects 201")
def test_create_post(client):
    with allure.step("Prepare post payload"):
        payload = {
            "title": "My first post",
            "body": "Hello world",
            "userId": 1
        }
    with allure.step("Send POST request to /posts"):
        response = client.post("/posts", payload)
    with allure.step("Verify status code is 201"):
        assert response.status_code == 201


@pytest.mark.regression
def test_update_post(client):
    payload = {
        "title": "Updated title",
        "body": "Updated body",
        "userId": 1
    }
    response = client.put("/posts/1", payload)
    assert response.status_code == 200
    data = response.json()  
    assert data["title"] == "Updated title"
    assert data["body"] == "Updated body"   

def test_delete_post(client):
    response = client.delete("/posts/1")
    assert response.status_code == 200


def test_created_post_has_id(created_post):
    assert "id"    in created_post
    assert "title" in created_post
    assert "body"  in created_post

def test_response_time(client):
    response = client.get("/users/1")
    assert response.elapsed.total_seconds() < 2.0, f"Too slow: {response.elapsed.total_seconds():.2f}s"

@pytest.mark.regression
def test_get_nonexistent_user(client):
    response = client.get("/users/99999")
    assert response.status_code == 404

@pytest.mark.regression
def test_get_nonexistent_post(client):
    response = client.get("/posts/99999")
    assert response.status_code == 404

@pytest.mark.regression
def test_create_post_missing_title(client):
    payload = {
        "body":   "No title here",
        "userId": 1
    }
    response = client.post("/posts", payload)
    assert response.status_code == 201

def test_get_user_with_retry(client):
    response = client.get_with_retry("/users/1")
    assert response.status_code == 200

def test_retry_on_failure(client):
    response = client.get_with_retry("/nonexistent-endpoint-99999", retries=3)
    assert response.status_code == 404
