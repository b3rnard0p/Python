import requests

url = "https://sandbox.api.assinaturas.pagseguro.com/customers"

payload = {
    "reference_id": "1",
    "name": "Bernardo Paz de Freitas",
    "email": "bernardopazdefreitas727@gmail.com",
    "tax_id": "04290028071",
    "phones": [
        {
            "country": "55",
            "area": "55",
            "number": "999262364"
        }
    ],
    "birth_date": "2004-11-01",
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
                "encrypted": "FuEhudweE8IWn6I1w4wBvW6Q+cgDdaf2W6p892rcDUijvbgTCHWSACIYkt7PBnotuo9l8dezSPLqQB6SfrG3SrgJ0Z9UNcFrA5cjf5rOLkm+LDgMH9stCBmatssdE5p7xcWK2OYbE02gTGLS22ZvqA0onPMf3i2Zc7n60QoTVCDezdrjx3iFEwbPjSPeieA/Mada3efA2+QDpCdYuueRiFT67OwY3D7vmzfccGNrWRYG/FVhyPxHWBJG6T6LUqhdWrnwQSrq70E8++k94NRLcRuNDbdJvdmNj1ndf9Wf4OuzfTitN89YpS6CbIYmqsh9cTvM3Q4AqUnG+6+TCbyAdQ==",
                "holder": {
                    "name": "Bernardo Paz de Freitas",
                    "birth_date": "2004-11-01",
                    "tax_id": "04290028071",
                    "phone": {
                        "country": "55",
                        "area": "55",
                        "number": "999262364"
                    }
                }
            }
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer ecf9b8a3-3291-402d-8da4-992608e687a18a994d8f4923931df105ec8ed1bf1ba80985-164c-4037-806d-554b1e506a54"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)