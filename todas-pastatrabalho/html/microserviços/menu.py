from flask import Flask, jsonify, request

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Pizza", "price": 12.99},
    {"id": 2, "name": "Burger", "price": 8.99}
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/menu/add', methods=['POST'])
def add_menu_item():
    new_item = request.json
    menu.append(new_item)
    return jsonify({"message": "Item added", "menu": menu})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
