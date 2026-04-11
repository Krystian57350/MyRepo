// Sample product data
const products = [
    {
        id: 1,
        name: "Classic Crew Neck",
        description: "Comfortable everyday essential",
        price: 19.99,
        emoji: "👕"
    },
    {
        id: 2,
        name: "Vintage Graphic",
        description: "Retro style with modern comfort",
        price: 24.99,
        emoji: "🎨"
    },
    {
        id: 3,
        name: "Premium Performance",
        description: "Moisture-wicking athletic fit",
        price: 29.99,
        emoji: "⚡"
    },
    {
        id: 4,
        name: "Oversized Fit",
        description: "Relaxed and trendy silhouette",
        price: 22.99,
        emoji: "📏"
    },
    {
        id: 5,
        name: "Henley Style",
        description: "Buttoned collar classic",
        price: 26.99,
        emoji: "🔘"
    },
    {
        id: 6,
        name: "V-Neck Essential",
        description: "Sleek and versatile look",
        price: 21.99,
        emoji: "✨"
    }
];

// Load products to the page
function loadProducts() {
    const productsGrid = document.getElementById('productsGrid');
    
    productsGrid.innerHTML = products.map(product => `
        <div class="product-card">
            <div class="product-image">${product.emoji}</div>
            <div class="product-info">
                <div class="product-name">${product.name}</div>
                <div class="product-description">${product.description}</div>
                <div class="product-price">$${product.price.toFixed(2)}</div>
                <div class="product-footer">
                    <select class="size-select">
                        <option value="">Size</option>
                        <option value="XS">XS</option>
                        <option value="S">S</option>
                        <option value="M">M</option>
                        <option value="L">L</option>
                        <option value="XL">XL</option>
                        <option value="XXL">XXL</option>
                    </select>
                    <button class="add-to-cart" onclick="addToCart(${product.id})">Add to Cart</button>
                </div>
            </div>
        </div>
    `).join('');
}

// Add to cart functionality
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        alert(`${product.name} added to cart! Price: $${product.price.toFixed(2)}`);
        // In a real app, this would add to an actual cart system
    }
}

// Handle contact form submission
document.addEventListener('DOMContentLoaded', function() {
    loadProducts();
    
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your message! We will get back to you soon.');
            contactForm.reset();
        });
    }

    // Smooth scrolling for navigation links
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
