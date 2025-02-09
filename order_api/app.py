from flask import Flask, jsonify

app = Flask(__name__)

orders = {
    1: {"product": "Laptop", "user_id": 1},
    2: {"product": "Smartphone", "user_id": 2}
}

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)