import requests

endpoint = "http://localhost:8000/api/products/1/update/"


# resp = requests.get(endpoint, params={"abc": 123})
resp = requests.put(endpoint, json={"title": "Hey there"})

# print(resp.text)
print(resp.json())
