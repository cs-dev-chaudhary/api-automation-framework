from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://jsonplaceholder.typicode.com"

    @task(3)
    def get_user(self):
        self.client.get("/users/1")

    @task(2)
    def get_all_posts(self):
        self.client.get("/posts")

    @task(1)
    def create_post(self):
        payload = {
            "title": "Load test post",
            "body": "Testing under load",
            "userId": 1
        }
        self.client.post("/posts", json=payload)
