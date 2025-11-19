import requests

url = "https://sandbox.api.assinaturas.pagseguro.com/subscriptions"

payload = {
    "plan": {"id": "PLAN_3D9224C0-86FE-45D4-9503-B5BEF21D9C60"},
    "customer": {
    "phones": [
        {
            "country": "55",
            "area": "55",
            "number": "99753928"
        }
    ],
    "name": "Fernanda Paz de Freitas",
    "email": "bernardopazdefreitas727@gmail.com",
    "tax_id": "73590931043",
    "birth_date": "2000-04-09",
    "address": {
        "street": "Silva Jardim",
        "number": "1554",
        "complement": "apto 302",
        "locality": "Nossa Senhora do Rosário",
        "city": "Santa Maria",
        "region_code": "RS",
        "postal_code": "97010490",
        "country": "BRA"
    },
    "billing_info": [
        {
            "type": "CREDIT_CARD",
            "card": {
                "encrypted": "bbaZDze16OiMq9d3bRoMW8PCQQ1ljcAguj5nV3MAs/pQ+a2tZBcYzgBGr67qfeEF583+TJCMprO0uRO+VGLiqiOrQFVYLbDaamIiuKBhdTkPbYrZx4PgKTGaMn/tDqpF/hvjqXPzCb+9h81a4CICrGzlSfzjJ31FbbOO3P/W1AnTZ/yoEVOc9ZgiL4FXB222p0EjjFTan591cKNdIE1sHWsmMGTU91OLynww8GssQDu4hD7GyEDKnbq3bRU0tTqQ7yvrM+vr1T/IyseOAXI6QfcPix17tCOXZvSHKvkh1QIE6wJjmYPkRhJPZo+yHc9zj3aKTmx0qdOOgSkjFQ2pag==",
                "holder": {
                    "name": "Fernanda Paz de Freitas",
                    "birth_date": "2000-04-09",
                    "tax_id": "73590931043",
                    "phone": {
                        "country": "55",
                        "area": "55",
                        "number": "99753928"
                    }
                }
            }
        }
    ]},
     "payment_method": [
        {
            "type": "CREDIT_CARD",
            "card": {
                    "id": "CARD_99196A46-99ED-43BE-8750-CC7A2B216A08",
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