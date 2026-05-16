import sqlite3
import pytest

@pytest.fixture
def db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE posts (id INTEGER, title TEXT, body TEXT)")
    yield conn
    conn.close()

def test_post_saved_to_database(client, db):
    payload = {
        "title": "DB test post",
        "body": "checking database",
        "userId": 1
    }
    response = client.post("/posts", payload)
    assert response.status_code == 201

    data = response.json()
    db.execute("INSERT INTO posts VALUES (?, ?, ?)", (data["id"], data["title"], data["body"]))
    db.commit()

    cursor = db.execute("SELECT * FROM posts WHERE id = ?", (data["id"],))
    row = cursor.fetchone()

    assert row is not None
    assert row[1] == "DB test post"
    assert row[2] == "checking database"
