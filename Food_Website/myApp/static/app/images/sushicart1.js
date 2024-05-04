const products = [
    { id: 1, name: "NigiriSushi", price: 250},
    { id: 2, name: "MakiSushi", price: 280},
    { id: 3, name: "Temaki Rolls", price: 150 },
    { id: 4, name: "Futamaki", price: 70 },
    { id: 5, name: "Hosomaki", price: 130 },
    { id: 6, name: "Chirashi", price: 50 },
    { id: 7, name: "Inari Sushi", price: 280 },
    { id: 8, name: "Uramaki", price: 100 },
    { id: 10, name: "Farmhouse", price: 950 },
    { id: 11, name: "Pannerpizza", price: 880 },
    // { id: 11, name: "Garlicbread", price: 150 },
    // { id: 12, name: "Chickenpizza", price: 70 },
    // { id: 13, name: "Chessy", price: 130 },
    // { id: 14, name: "Vegloaded", price: 50 },
    // { id: 15, name: "Tandoori", price: 280 },
    // { id: 16, name: "Margherita", price: 100 },
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
        saveCartToLocalStorage();
    }
}

function decreaseQuantity(itemId) {
    const item = cartItems.find((item) => item.id === itemId);
    if (item && item.quantity > 1) {
        item.quantity--;
        updateCart();
        saveCartToLocalStorage();
    }
}

function increaseQuantity(itemId) {
    const item = cartItems.find((item) => item.id === itemId);
    if (item) {
        item.quantity++;
        updateCart();
        saveCartToLocalStorage();
    }
}

function removeCartItem(itemId) {
    cartItems = cartItems.filter((item) => item.id !== itemId);
    updateCart();
    saveCartToLocalStorage();
}

function clearCart() {
    cartItems = [];
    updateCart();
    saveCartToLocalStorage();
}

function updateCart() {
    const cartList = document.getElementById("cart-items");
    cartList.innerHTML = "";

    let totalPayment = 0;

    cartItems.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
            <div class="cart-item">
                <div class="item-details">
                    <h4>${item.name}</h4>
                    <p>Price: $${item.price}</p>
                    <div class="quantity-controls" >
                        <button  onclick="decreaseQuantity(${item.id})">-</button>
                        <span>${item.quantity}</span>
                        <button onclick="increaseQuantity(${item.id})">+</button>
                    </div>
                    <button type="button" class="btn btn-dark btn-rounded" style="margin-top:10px;" onclick="removeCartItem(${item.id})">Remove</button>
                    <hr style="color:white;">
                </div>
            </div>
        `;
        cartList.appendChild(listItem);

        totalPayment += item.price * item.quantity;
    });

    const totalPaymentSpan = document.getElementById("total-payment");
    totalPaymentSpan.textContent = totalPayment;
}

function saveCartToLocalStorage() {
    localStorage.setItem("cartItems", JSON.stringify(cartItems));



}

function loadCartFromLocalStorage() {
    const savedCart = localStorage.getItem("cartItems");
    if (savedCart) {
        cartItems = JSON.parse(savedCart);
        updateCart();
    }
}

loadCartFromLocalStorage();
