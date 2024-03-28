// // Solution 1
// let playerOneChoice = Math.floor(Math.random() * 6);
// let playerTwoChoice = Math.floor(Math.random() * 6);

// let playerOneImage = document.querySelector(".img1");
// let playerTwoImage = document.querySelector(".img2");

// let heading = document.querySelector("h1");

// let diceOneImgSrc = "./images/dice1.png";
// let diceTwoImgSrc = "./images/dice2.png";
// let diceThreeImgSrc = "./images/dice3.png";
// let diceFourImgSrc = "./images/dice4.png";
// let diceFiveImgSrc = "./images/dice5.png";
// let diceSixImgSrc = "./images/dice6.png";

// switch (playerOneChoice) {
//   case 0:
//     playerOneImage.setAttribute("src", diceOneImgSrc);
//     break;
//   case 1:
//     playerOneImage.setAttribute("src", diceTwoImgSrc);
//     break;
//   case 2:
//     playerOneImage.setAttribute("src", diceThreeImgSrc);
//     break;
//   case 3:
//     playerOneImage.setAttribute("src", diceFourImgSrc);
//     break;
//   case 4:
//     playerOneImage.setAttribute("src", diceFiveImgSrc);
//     break;
//   case 5:
//     playerOneImage.setAttribute("src", diceSixImgSrc);
//     break;
//   default:
//     playerOneImage.setAttribute("src", "");
//     break;
// }

// switch (playerTwoChoice) {
//   case 0:
//     playerTwoImage.setAttribute("src", diceOneImgSrc);
//     break;
//   case 1:
//     playerTwoImage.setAttribute("src", diceTwoImgSrc);
//     break;
//   case 2:
//     playerTwoImage.setAttribute("src", diceThreeImgSrc);
//     break;
//   case 3:
//     playerTwoImage.setAttribute("src", diceFourImgSrc);
//     break;
//   case 4:
//     playerTwoImage.setAttribute("src", diceFiveImgSrc);
//     break;
//   case 5:
//     playerTwoImage.setAttribute("src", diceSixImgSrc);
//     break;
//   default:
//     playerTwoImage.setAttribute("src", "");
//     break;
// }

// if (playerOneChoice > playerTwoChoice) {
//   heading.innerHTML = "🚩 Player 1 wins!";
// } else if (playerOneChoice < playerTwoChoice) {
//   heading.innerHTML = "Player 2 wins! 🚩";
// } else {
//   heading.innerHTML = "Draw!";
// }

// ------------------------------
// solution 2
let firstPlayerChoice = Math.floor(Math.random() * 6) + 1; // palyer 1: 1 - 6
let secondPlayerChoice = Math.floor(Math.random() * 6) + 1; // player 2: 1 - 6

// html image elements
let firstPlayerImageElement = document.querySelector(".img1");
let secondPlayerImageElement = document.querySelector(".img2");

// html heading element
let headingElement = document.querySelector("h1");

// image source depends on random number
let randomImageOne = "./images/" + "dice" + firstPlayerChoice + ".png";
let randomImageTwo = "./images/" + "dice" + secondPlayerChoice + ".png";

// setting source of each image to the random image source
firstPlayerImageElement.setAttribute("src", randomImageOne);
secondPlayerImageElement.setAttribute("src", randomImageTwo);

// updating heading weather palyer 1 or 2 wins or draw!
if (firstPlayerChoice > secondPlayerChoice) {
  headingElement.innerHTML = "🚩 Player 1 wins!";
} else if (firstPlayerChoice < secondPlayerChoice) {
  headingElement.innerHTML = "Player 2 wins! 🚩";
} else {
  headingElement.innerHTML = "Draw!";
}
