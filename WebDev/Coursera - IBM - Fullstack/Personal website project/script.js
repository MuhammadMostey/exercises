document
  .getElementById("recommendation-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const recommendationText = document.getElementById(
      "recommendation-text"
    ).value;
    const yourName = document.getElementById("your-name").value; // Get the value of the input field "Your Name"

    // Check if the input field "Your Name" is empty, if not, concatenate it with the recommendation text
    const recommendation = yourName
      ? yourName + ": " + recommendationText
      : recommendationText;

    const recommendationsList = document.querySelector("#recommendations ul");
    const newRecommendation = document.createElement("li");
    newRecommendation.textContent = recommendation;
    recommendationsList.appendChild(newRecommendation);
    alert("Recommendation submitted successfully!");
  });

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
