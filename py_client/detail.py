import requests

endpoint = "http://localhost:8000/api/products/3/"


# resp = requests.get(endpoint, params={"abc": 123})
resp = requests.get(endpoint)

# print(resp.text)
print(resp.json())
