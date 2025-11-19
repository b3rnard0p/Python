import requests

url = "https://sandbox.api.assinaturas.pagseguro.com/subscriptions"

payload = {
    "plan": {"id": "PLAN_3D9224C0-86FE-45D4-9503-B5BEF21D9C60"},
    "customer": {"id": "CUST_EF84FC90-3FA5-4965-9737-9C99E1FAC6F7"},
    "payment_method": [
        {
            "type": "CREDIT_CARD",
            "card": {
                    "id": "dAoqb0F32GLIBp01bes4jgz/g5ut65zSeWkdNYZ6FJuflD8mIJVL0bLvZRFMlls/FYbDQXknOen3LfkDH5wvra0SKGtIagfjJ58EHa6QkWI65aIniDGYwPL+YVcUiYvPKK4CXxnEUh+CEwByIP97zlhc4/z3WHcYYwpvIE2SJnPycCoweYn5NpYSbzzRtU0YVJUXPNIeDJMjThfiDnmZjXIio4iIOgPH6pZoAZ8km/12uzButvxZk3mWm8Gp3baUaFSMwL50gn7wKAAchIy7mS1hBPy0kQq39ogKFeZoTq4NPL4GRxTFFlKAKEJt8M9Z9/3sWlFvMIhZfpEqFpAkEA==",
                    "security_code": "123"
                    }
        }
    ],
    "amount": {"value": 99900, "currency": "BRL"},
    "best_invoice_date": {"day": 30},
    "reference_id": "1",
    "pro_rata": False
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ecf9b8a3-3291-402d-8da4-992608e687a18a994d8f4923931df105ec8ed1bf1ba80985-164c-4037-806d-554b1e506a54"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
