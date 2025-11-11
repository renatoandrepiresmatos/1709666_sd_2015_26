from flask import Flask, jsonify, request

app = Flask(__name__)
payments = {}

@app.route('/payment/process', methods=['POST'])
def process_payment():
    data = request.json
    order_id = data.get("order_id")
    amount = data.get("amount")
    
    if order_id and amount:
        payments[order_id] = "Paid"
        return jsonify({"message": f"Payment of ${amount} for order {order_id} successful"})
    return jsonify({"error": "Invalid payment data"}), 400

@app.route('/payment/status/<int:order_id>', methods=['GET'])
def payment_status(order_id):
    status = payments.get(order_id, "Pending")
    return jsonify({"order_id": order_id, "payment_status": status})

if __name__ == '__main__':
    app.run(debug=True, port=5004)
