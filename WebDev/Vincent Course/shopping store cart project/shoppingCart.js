class Item {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }
}

class Store {
  constructor(storeName) {
    this.cart = [];
    this.greetings = `Hello! Welcome to ${storeName} Store`;
    this.message = `
    Press a to add and item to the cart.
    Press r to remove an item from the cart.
    Press x to exit.
    `;
  }

  addToCart(item) {
    this.cart.push(item);
  }

  removeFromCart(index) {
    // let pickedIndex = this.cart.indexOf(item);
    this.cart.splice(index, 1);
  }

  calculateTotal() {
    let total = 0;
    this.cart.forEach((item) => {
      total += item.price;
    });
    return total;
  }

  displayCart() {
    // let i = 0;
    // let itemsListDetailedArray = [];

    // this.cart.forEach((itemIndex) => {
    //   itemsListDetailedArray.push(
    //     `${i} ${itemIndex.name} = ${itemIndex.price}`
    //   );
    //   // console.log(`${i} ${itemIndex.name} = ${itemIndex.price}`);
    //   i++;
    // });
    // // console.log(`Total Amount: ${this.calculateTotal()}`);
    // return itemsListDetailedArray;
    return this.cart;
  }
}

// initiating a new store
let pikachu = new Store("pikachu");
console.log(pikachu.greetings);

// to clear the form fields after submitting
// function clearForm() {
//   let form = document.getElementById("ItemsForm");
//   form.reset();
// }

console.log(itemsListDetailedArray);

function refreshUI() {}

function addItem(form) {
  // getting entered values to the input fields
  let itemName = form.itemName.value;
  let itemPrice = parseFloat(form.itemPrice.value);

  // creating a new Item object for the store
  let newItem = new Item(itemName, itemPrice);

  // adding new element to the cart
  pikachu.addToCart(newItem);

  // to avoid page to be refreshed
  return false;
}

//c
//c
//c
//c
//c
//c
//c
//c
//c
//c
// looping for prompting the user for command to manipulate the cart within the store.

// while (true) {
//   let displayCartToUser = pikachu.displayCart();
//   console.log(pikachu.message);
//   let command = prompt("Please Enter a Command: ").toLowerCase();

//   if (command == "a") {
//     let itemName = prompt("Please provide an Item Name: ");
//     let isNegativeAmount = true;
//     let itemPrice = 0;

//     while (isNegativeAmount) {
//       itemPrice = parseFloat(prompt("Please provide Item Price: "));
//       if (itemPrice > 0) {
//         isNegativeAmount = false;
//       }
//     }

//     let newItem = new Item(itemName, itemPrice);
//     pikachu.addToCart(newItem);

//     displayCartToUser;
//   } else if (command == "r") {
//     let itemIndexToRemove = parseInt(
//       prompt("Please provide the index number of the Item you want to remove: ")
//     );
//     pikachu.removeFromCart(itemIndexToRemove);
//     displayCartToUser;
//   } else if (command == "x") {
//     break;
//   } else {
//     console.log("Please try again! Enter a valid command code. ");
//   }
// }

/*
    Notes:
    - within classes methods are created w/o function keyword
    - toLowerCase() is used to turn to lower.
    - parseInt(), parseFloat(), 123.toString() : to type cast. 
    - constructor()
*/
