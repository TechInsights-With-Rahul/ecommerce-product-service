from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Health check endpoint for liveness probe
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200

# Simulated in-memory product storage
products = []

#@app.route('/products', methods=['POST'])
#def add_product():
#    data = request.get_json()
#    new_product = {
#        "id": len(products) + 1,
#        "name": data['name'],
#        "description": data.get('description'),
#        "price": data['price']
#    }
#    products.append(new_product)
#    return jsonify({"message": "Product added", "product": new_product}), 201

@app.route('/', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

