let amountBox = document.getElementById("totalPrice");
let itemsList = document.getElementById("itemsList");

let cartTotal = 0;
let cart = [];

class Item {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

function addItem(form) {
  let itemName = form.itemName.value;
  let itemPrice = form.itemPrice.value;
  cartTotal += parseFloat(itemPrice);
  let item = new Item(itemName, parseFloat(itemPrice));
  cart.push(item);

  refreshUI();

  return false;
}

function refreshUI() {
  // updates the total price heading
  amountBox.innerHTML = `Total Price: $${cartTotal.toLocaleString()} | Total # of items ${
    cart.length
  }`;
  // clearing old list
  itemsList.innerHTML = "";

  cart.forEach((item, index) => {
    // creates new item for list
    let itemElement = document.createElement("li");
    let itemDescription = document.createTextNode(
      `${index + 1}: ${item.name} - ${item.price.toLocaleString()}`
    );
    itemElement.appendChild(itemDescription);

    // creates delete button for each item list
    let itemDeleteButton = document.createElement("button");
    itemDeleteButton.type = "button";
    itemDeleteButton.innerText = "delete";
    itemDeleteButton.classList.add("btn", "btn-danger");
    itemElement.appendChild(itemDeleteButton);

    // style each list item and appends to list
    itemElement.classList.add(
      "list-group-item",
      "d-flex",
      "justify-content-between",
      "align-items-center"
    );
    itemsList.appendChild(itemElement);

    // updating list and total price for delete item button
    itemDeleteButton.addEventListener("click", () => {
      cartTotal -= item.price;
      cart.splice(index, 1);
      refreshUI();
    });
  });
}
