from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def send_post(self):
        headers = {'content-type': 'application/json'}
        self.client.post("/newnewback/api/buy", json={
            "name": "Jane Smith",
            "phone": "444-555-6666",
            "address": "456 Oak Ave, Townsville, Canada",
            "price": 15,
            "quantity": 2,
            "item_id": "handcream_19",
            "item_name": "닥터자르트 세라마이딘 크림"
        }, headers=headers)
