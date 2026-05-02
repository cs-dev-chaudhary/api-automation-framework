import requests
import pytest
import json
import os

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
def test_get_user_returns_200(client):
    response = client.get("/users/1")
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

def test_create_post(client):
    payload = {
        "title": "My first post",
        "body": "Hello world",
        "userId": 1
    }
    response = client.post("/posts",payload)
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
