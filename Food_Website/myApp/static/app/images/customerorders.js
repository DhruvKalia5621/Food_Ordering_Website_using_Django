
// Retrieve cart items from localStorage
const cartItemsJSON = localStorage.getItem('cartItems');
const cartItems = JSON.parse(cartItemsJSON) || [];

// Get the tbody element where we'll populate the cart items
const cartItemsTableBody = document.getElementById('cartItems');

// Populate the table with cart items
cartItems.forEach(item => {
    const row = document.createElement('tr');
    const customername = document.createElement('td');
    const customeremail = document.createElement('td');
    const idCell = document.createElement('td');
    const nameCell = document.createElement('td');
    const priceCell = document.createElement('td');

   
    customername.textContent = "dhruv";
    customeremail.textContent = "example.com";
    idCell.textContent = item.id;
    nameCell.textContent = item.name;
    priceCell.textContent = item.price;

   
    row.appendChild(customername);
    row.appendChild(customeremail);
    row.appendChild(idCell);
    row.appendChild(nameCell);
    row.appendChild(priceCell);

    cartItemsTableBody.appendChild(row);
});