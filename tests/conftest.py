import pytest
from api.api_client import APIClient
from config.logger import get_logger

logger = get_logger("conftest")
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def created_post(client):
    payload = {
        "title": "Teardown test post",
        "body":  "This will be deleted after the test",
        "userId": 1
    }
    response = client.post("/posts", payload)
    post = response.json()
    logger.info(f"Setup: created post with id {post['id']}")

    yield post

    logger.info(f"Teardown: deleting post {post['id']}")
    client.delete(f"/posts/{post['id']}")
