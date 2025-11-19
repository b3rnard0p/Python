import requests

url = "https://sandbox.api.assinaturas.pagseguro.com/plans"

payload = {
    "reference_id": "1",
    "name": "Dama",
    "description": "Plano mensal Dama",
    "amount": {
        "value": 999,
        "currency": "BRL"
    },
    "interval": {
        "unit": "MONTH",
        "length": 1
    },
    "payment_method": ["CREDIT_CARD"],
    "editable": True
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ecf9b8a3-3291-402d-8da4-992608e687a18a994d8f4923931df105ec8ed1bf1ba80985-164c-4037-806d-554b1e506a54"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)