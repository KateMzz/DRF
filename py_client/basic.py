import requests

endpoint = "http://localhost:8000/api/"


# resp = requests.get(endpoint, params={"abc": 123})
resp = requests.post(endpoint, json={"title": "hello"})

# print(resp.text)
print(resp.json())
