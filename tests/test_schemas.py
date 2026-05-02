from schemas.user_schema import USER_SCHEMA

def test_user_schema(client):
    response = client.get("/users/1")
    data = response.json()
    client.validate_schema(data, USER_SCHEMA)
