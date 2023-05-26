import requests


product_id = input("What product id would you like to delete?\n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"
    # resp = requests.get(endpoint, params={"abc": 123})
    resp = requests.delete(endpoint)

    # print(resp.text)
    print(resp.status_code, resp.status_code==204)
