import requests

endpoint = "http://localhost:8000/api/products/123456787/"


# resp = requests.get(endpoint, params={"abc": 123})
resp = requests.post(endpoint)

# print(resp.text)
print(resp.json())
