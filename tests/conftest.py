import pytest
from api.api_client import APIClient
from config.config import Config, load_env
from config.logger import get_logger

logger = get_logger("conftest")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="Environment to run tests against")

@pytest.fixture(scope="session", autouse=True)
def load_environment(request):
    env = request.config.getoption("--env")
    load_env(env)
    logger.info(f"Running against environment: {env or 'default (.env)'}")
    logger.info(f"Base URL: {Config.BASE_URL}")

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def created_post(client):
    payload = {
        "title": "Teardown test post",
        "body": "This will be deleted after the test",
        "userId": 1
    }
    response = client.post("/posts", payload)
    post = response.json()
    logger.info(f"Setup: created post with id {post['id']}")
    yield post
    logger.info(f"Teardown: deleting post {post['id']}")
    client.delete(f"/posts/{post['id']}")
