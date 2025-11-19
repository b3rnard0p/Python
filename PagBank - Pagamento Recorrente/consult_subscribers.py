import requests

url = "https://sandbox.api.assinaturas.pagseguro.com/customers"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer ecf9b8a3-3291-402d-8da4-992608e687a18a994d8f4923931df105ec8ed1bf1ba80985-164c-4037-806d-554b1e506a54"
}

response = requests.get(url, headers=headers)

print(response.text)