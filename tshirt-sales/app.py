from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__, template_folder='.', static_folder='.')

# Product database
products = [
    {
        'id': 1,
        'name': 'Classic Crew Neck',
        'description': 'Comfortable everyday essential',
        'price': 19.99,
        'stock': 50
    },
    {
        'id': 2,
        'name': 'Vintage Graphic',
        'description': 'Retro style with modern comfort',
        'price': 24.99,
        'stock': 35
    },
    {
        'id': 3,
        'name': 'Premium Performance',
        'description': 'Moisture-wicking athletic fit',
        'price': 29.99,
        'stock': 28
    },
    {
        'id': 4,
        'name': 'Oversized Fit',
        'description': 'Relaxed and trendy silhouette',
        'price': 22.99,
        'stock': 42
    },
    {
        'id': 5,
        'name': 'Henley Style',
        'description': 'Buttoned collar classic',
        'price': 26.99,
        'stock': 31
    },
    {
        'id': 6,
        'name': 'V-Neck Essential',
        'description': 'Sleek and versatile look',
        'price': 21.99,
        'stock': 45
    }
]

# Shopping cart storage (in-memory for demo)
shopping_cart = []

# Route to serve the main page
@app.route('/')
def index():
    return open('index.html').read()

# API route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# API route to get a specific product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# API route to add item to cart
@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        product_id = data.get('product_id')
        size = data.get('size', 'M')
        quantity = data.get('quantity', 1)
        
        product = next((p for p in products if p['id'] == product_id), None)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        cart_item = {
            'product_id': product_id,
            'name': product['name'],
            'price': product['price'],
            'size': size,
            'quantity': quantity,
            'total': product['price'] * quantity
        }
        
        shopping_cart.append(cart_item)
        return jsonify({
            'success': True,
            'message': f"{product['name']} added to cart",
            'cart_size': len(shopping_cart)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API route to get cart
@app.route('/api/cart', methods=['GET'])
def get_cart():
    total = sum(item['total'] for item in shopping_cart)
    return jsonify({
        'items': shopping_cart,
        'total': total,
        'count': len(shopping_cart)
    })

# API route to clear cart
@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    global shopping_cart
    shopping_cart = []
    return jsonify({'success': True, 'message': 'Cart cleared'})

# API route to process checkout
@app.route('/api/checkout', methods=['POST'])
def checkout():
    try:
        data = request.get_json()
        
        if not shopping_cart:
            return jsonify({'error': 'Cart is empty'}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'address']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Calculate total
        total = sum(item['total'] for item in shopping_cart)
        
        # Create order
        order = {
            'order_id': f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'customer': data.get('name'),
            'email': data.get('email'),
            'address': data.get('address'),
            'items': shopping_cart.copy(),
            'total': total,
            'status': 'confirmed',
            'timestamp': datetime.now().isoformat()
        }
        
        # Clear the cart after successful checkout
        shopping_cart.clear()
        
        return jsonify({
            'success': True,
            'message': 'Order placed successfully',
            'order': order
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# API route for contact form
@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # In a real app, you'd send an email here
        contact_message = {
            'name': data.get('name'),
            'email': data.get('email'),
            'message': data.get('message'),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify({
            'success': True,
            'message': 'Thank you for contacting us. We will get back to you soon.'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Page not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🚀 T-Shirt Sales Server is running!")
    print("📍 Open your browser and go to http://localhost:5000")
    app.run(debug=True, host='localhost', port=5000)
