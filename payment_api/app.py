from flask import Flask, jsonify

app = Flask(__name__)

payments = {
    1: {"order_id": 1, "amount": 1000, "status": "completed"},
    2: {"order_id": 2, "amount": 500, "status": "pending"}
}

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = payments.get(payment_id)
    if payment:
        return jsonify(payment)
    else:
        return jsonify({"error": "Payment not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)