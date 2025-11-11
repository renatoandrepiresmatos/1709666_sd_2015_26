from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/notify/order/<int:order_id>', methods=['POST'])
def notify_order(order_id):
    return jsonify({"message": f"Notification sent for order {order_id}"})

@app.route('/notify/kitchen/<int:order_id>', methods=['POST'])
def notify_kitchen(order_id):
    return jsonify({"message": f"Kitchen notified for order {order_id}"})

@app.route('/notify/delivery/<int:order_id>', methods=['POST'])
def notify_delivery(order_id):
    return jsonify({"message": f"Delivery team notified for order {order_id}"})

if __name__ == '__main__':
    app.run(debug=True, port=5006)
