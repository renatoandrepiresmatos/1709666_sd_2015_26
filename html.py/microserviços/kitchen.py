from flask import Flask, jsonify, request

app = Flask(__name__)
kitchen_orders = {}

@app.route('/kitchen/process/<int:order_id>', methods=['POST'])
def process_order(order_id):
    kitchen_orders[order_id] = "Cooking"
    return jsonify({"message": f"Order {order_id} is being prepared"})

@app.route('/kitchen/complete/<int:order_id>', methods=['POST'])
def complete_order(order_id):
    if order_id in kitchen_orders:
        kitchen_orders[order_id] = "Ready"
        return jsonify({"message": f"Order {order_id} is ready"})
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)
