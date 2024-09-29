import requests
# 1, 5, 10
BASE_URL = "http://jsonplaceholder.typicode.com"

class APIHelper():
    def get_users(self):
        return requests.get(f"{BASE_URL}/users").json()
    
    def get_todos(self):
        return requests.get(f"{BASE_URL}/todos").json()
    
