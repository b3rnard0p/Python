import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-3245968722028908-110312-2525e70b32695b1f700211c8f6e99981-2958197716")

    payment_data = {
        "items": [
            {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99}
        ]
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    print(payment)
    link_iniciar_pagamento = payment.get("sandbox_init_point")
    return link_iniciar_pagamento