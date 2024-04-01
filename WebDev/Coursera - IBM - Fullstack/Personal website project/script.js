document
  .getElementById("recommendation-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const recommendationText = document.getElementById(
      "recommendation-text"
    ).value;
    const yourName = document.getElementById("your-name").value;

    const recommendation = yourName
      ? yourName + ": " + recommendationText
      : recommendationText;

    const recommendationsList = document.querySelector("#recommendations ul");
    const newRecommendation = document.createElement("li");
    newRecommendation.textContent = recommendation;
    recommendationsList.appendChild(newRecommendation);

    const modal = document.getElementById("modal");
    const modalMessage = document.getElementById("modal-message");
    modalMessage.textContent = "Recommendation submitted successfully!";
    modal.style.display = "block"; // Show the modal

    // Call displayCheckmark function to show the checkmark
    displayCheckmark();
  });

document.getElementById("modal-button").addEventListener("click", function () {
  document.getElementById("modal").style.display = "none"; // Hide the modal when OK button is clicked
});

document.querySelector(".close").addEventListener("click", function () {
  document.getElementById("modal").style.display = "none"; // Hide the modal when close button is clicked
});

// Display checkmark when modal message is set
function displayCheckmark() {
  document.querySelector(".checkmark").style.display = "block";
}

// Show or hide the scroll-to-top button based on the user's scroll position
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  var scrollToTopBtn = document.getElementById("scrollToTop");

  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
}

// Scroll to the top of the page when the button is clicked
document.getElementById("scrollToTop").addEventListener("click", function () {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
});
