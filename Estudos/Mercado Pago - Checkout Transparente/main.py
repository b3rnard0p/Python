from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mercadopago
import uuid
import os

app = Flask(__name__, static_folder='.')
CORS(app)  # Permitir requisições do frontend

# Inicializar SDK do MercadoPago
sdk = mercadopago.SDK("TEST-3588662721380066-110610-c550c8fdad8bfe8a4b9874a24e103227-219788766")

@app.route('/process_payment', methods=['POST'])
def process_payment():
    try:
        # Receber dados do frontend
        data = request.get_json()
        
        print("=== DADOS RECEBIDOS ===")
        print(f"Token: {data.get('token')[:20]}..." if data.get('token') else "Token: None")
        print(f"Amount: {data.get('transaction_amount')}")
        print(f"Payment Method: {data.get('payment_method_id')}")
        print(f"Email: {data['payer']['email']}")
        
        # Configurar opções da requisição com chave de idempotência única
        request_options = mercadopago.config.RequestOptions()
        request_options.custom_headers = {
            'x-idempotency-key': str(uuid.uuid4())
        }
        
        # Preparar dados do pagamento
        payment_data = {
            "transaction_amount": float(data.get("transaction_amount")),
            "token": data.get("token"),
            "description": data.get("description"),
            "installments": int(data.get("installments")),
            "payment_method_id": data.get("payment_method_id"),
            "payer": {
                "email": data["payer"]["email"],
                "identification": {
                    "type": data["payer"]["identification"]["type"],
                    "number": data["payer"]["identification"]["number"]
                }
            }
        }
        
        # Criar pagamento
        payment_response = sdk.payment().create(payment_data, request_options)
        payment = payment_response["response"]
        
        print("=== RESPOSTA MERCADOPAGO ===")
        print("Status:", payment.get('status'))
        
        # Verificar se houve erro
        if payment.get('status') == 400 or 'error' in payment:
            print("Erro no pagamento:", payment)
            return jsonify({
                "status": "error",
                "error": payment.get('error', 'unknown'),
                "message": payment.get('message', 'Erro ao processar pagamento'),
                "details": payment
            }), 400
        
        print("Pagamento criado com sucesso:", payment.get('id'))
        
        return jsonify({
            "status": "success",
            "payment": payment
        }), 200
        
    except Exception as e:
        print("=== ERRO NA APLICAÇÃO ===")
        print("Erro ao processar pagamento:", str(e))
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("Servidor iniciado em http://localhost:5000")
    app.run(debug=True, port=5000)