const openBtn = document.getElementById("openPopup");
const closeBtn = document.querySelector(".close-btn");
const modal = document.getElementById("popupModal");

// Open popup
openBtn.addEventListener('click', () => {
  modal.style.display = "block";
});

// Close popup when X is clicked
closeBtn.addEventListener('click', () => {
  modal.style.display = "none";
});

// Close popup when clicking outside modal content
window.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});
