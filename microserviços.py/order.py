from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
orders = []  # {'menu_item_id':<number>,'id':<number of the order in restaurant>}

@app.route('/order/create', methods=['POST'])
def create_order():
    order_data = request.json
    menu_response = requests.get("http://127.0.0.1:5001/menu").json()
    
    # Validate menu items
    if any(item["id"] == order_data["menu_item_id"] for item in menu_response):
        orders.append(order_data)
        return jsonify({"message": "Order placed", "order": order_data})
    return jsonify({"error": "Invalid menu item"}), 400

@app.route('/order/status/<int:order_id>', methods=['GET'])
def get_order_status(order_id):
    try:
        order = next((o for o in orders if o["id"] == order_id), None)
        if order:
            return jsonify({"status": order.get("status", "Pending")})
        return jsonify({"error": "Order not found"}), 404
    except:
        return jsonify({"error": "Order not found"}), 404
if __name__ == '__main__':
    app.run(debug=True, port=5002)

