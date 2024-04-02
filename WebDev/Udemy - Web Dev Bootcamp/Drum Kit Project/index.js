let drumButtonElement = document.querySelectorAll(".drum");

let crashSound = new Audio("sounds/crash.mp3");
let tomOneSound = new Audio("sounds/tom-1.mp3");
let tomTwoSound = new Audio("sounds/tom-2.mp3");
let tomThreeSound = new Audio("sounds/tom-3.mp3");
let tomFourSound = new Audio("sounds/tom-4.mp3");
let kickDrumSound = new Audio("sounds/kick-bass.mp3");
let snareSound = new Audio("sounds/snare.mp3");

// detecting mouse keyclicks
for (let i = 0; i < drumButtonElement.length; i++) {
  drumButtonElement[i].addEventListener("click", function () {
    makeSound(drumButtonElement[i].innerHTML);
  });
}

// detecting keyboard pressed keys
document.addEventListener("keydown", function (event) {
  makeSound(event.key);
});

function makeSound(event) {
  switch (event) {
    case "w":
      tomOneSound.play();
      break;
    case "a":
      tomTwoSound.play();
      break;
    case "s":
      tomThreeSound.play();
      break;
    case "d":
      tomFourSound.play();
      break;
    case "j":
      snareSound.play();
      break;
    case "k":
      crashSound.play();
      break;
    case "l":
      kickDrumSound.play();
      break;
    default:
      "";
      break;
  }
}
