const products = [
    { id: 1, name: "sushi 1", price: 10 },
    { id: 2, name: "sushi 2", price: 20 },
    // Add more products here
];

let cartItems = [];

function addToCart(productId) {
    const product = products.find((item) => item.id === productId);
    if (product) {
        const existingCartItem = cartItems.find((item) => item.id === productId);
        if (existingCartItem) {
            existingCartItem.quantity++;
        } else {
            cartItems.push({ ...product, quantity: 1 });
        }
        updateCart();
    }
}

function decreaseQuantity(itemId) {
    const item = cartItems.find((item) => item.id === itemId);
    if (item && item.quantity > 1) {
        item.quantity--;
        updateCart();
    }
}

function increaseQuantity(itemId) {
    const item = cartItems.find((item) => item.id === itemId);
    if (item) {
        item.quantity++;
        updateCart();
    }
}

function removeCartItem(itemId) {
    cartItems = cartItems.filter((item) => item.id !== itemId);
    updateCart();
}

function updateCart() {
    const cartList = document.getElementById("cart-items");
    cartList.innerHTML = "";

    let totalPayment = 0;

    cartItems.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
            <span>${item.name} - $${item.price} - Quantity: ${item.quantity}</span>
            <button onclick="decreaseQuantity(${item.id})">-</button>
            <button onclick="increaseQuantity(${item.id})">+</button>
            <button onclick="removeCartItem(${item.id})">Remove</button>
        `;
        cartList.appendChild(listItem);

        totalPayment += item.price * item.quantity;
    });

    const totalPaymentSpan = document.getElementById("total-payment");
    totalPaymentSpan.textContent = totalPayment;
}

updateCart();
