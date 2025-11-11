from flask import Flask, jsonify, request

app = Flask(__name__)
deliveries = {}

@app.route('/delivery/assign/<int:order_id>', methods=['POST'])
def assign_driver(order_id):
    deliveries[order_id] = "Out for Delivery"
    return jsonify({"message": f"Driver assigned to order {order_id}"})

@app.route('/delivery/status/<int:order_id>', methods=['GET'])
def delivery_status(order_id):
    status = deliveries.get(order_id, "Not Assigned")
    return jsonify({"order_id": order_id, "delivery_status": status})

if __name__ == '__main__':
    app.run(debug=True, port=5005)
