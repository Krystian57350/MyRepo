# 👕 TeeHub - T-Shirt Sales Website

A modern, responsive web application for selling t-shirts with HTML, CSS, Python (Flask), and JavaScript.

## Project Structure

```
tshirt-sales/
├── index.html          # Main HTML page
├── style.css           # Styling and responsive design
├── script.js           # Frontend JavaScript functionality
├── app.py              # Python Flask backend
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Features

✨ **Frontend:**
- Responsive design (works on desktop, tablet, mobile)
- Product catalog with 6 different t-shirt styles
- Shopping cart functionality
- Contact form
- Smooth scrolling navigation
- Modern UI with gradient effects

🐍 **Backend (Python Flask):**
- REST API for products
- Shopping cart management
- Checkout system with order confirmation
- Contact form processing
- Error handling

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory:**
```bash
cd tshirt-sales
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Flask application:**
```bash
python app.py
```

4. **Open your browser:**
Navigate to `http://localhost:5000`

## How to Use

### Frontend
- **Browse Products**: Scroll through the product catalog
- **Add to Cart**: Select size and click "Add to Cart"
- **Navigation**: Use the menu to jump to different sections
- **Contact Us**: Fill out the contact form to send a message

### API Endpoints

**Get all products:**
```
GET /api/products
```

**Get specific product:**
```
GET /api/products/<product_id>
```

**Add to cart:**
```
POST /api/cart/add
{
    "product_id": 1,
    "size": "M",
    "quantity": 1
}
```

**Get cart:**
```
GET /api/cart
```

**Checkout:**
```
POST /api/checkout
{
    "name": "John Doe",
    "email": "john@example.com",
    "address": "123 Main St"
}
```

**Clear cart:**
```
POST /api/cart/clear
```

**Contact:**
```
POST /api/contact
{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Your message here"
}
```

## Customization

### Add More Products
Edit the `products` list in `app.py` to add or modify products.

### Modify Colors
Change color variables in `style.css`:
```css
:root {
    --primary-color: #ff6b6b;
    --secondary-color: #333;
    /* ... other colors */
}
```

### Change Product Emojis
In `script.js`, modify the emoji property in the products array.

## Future Enhancements

- 🔐 User authentication and login
- 💳 Real payment integration (Stripe, PayPal)
- 📧 Email notifications for orders
- 📦 Order tracking system
- ⭐ Product reviews and ratings
- 🔍 Advanced search and filters
- 📱 Mobile app version

## Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3, Flask
- **Styling**: CSS Grid, Flexbox
- **API**: REST API

## License

MIT License - Feel free to use and modify this project!

## Support

For issues or questions, please contact support@teehub.com

---

Made with ❤️ by TeeHub Team
