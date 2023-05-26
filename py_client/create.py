import requests

headers = {'Authorization': 'Bearer 63d89a3c102761bc1c42215af53579245ed69d19'}


endpoint = "http://localhost:8000/api/products/"


# resp = requests.get(endpoint, params={"abc": 123})
resp = requests.post(endpoint, json={'title': "here is the title "}, headers=headers)

# print(resp.text)
print(resp.json())
