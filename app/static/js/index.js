const openBtn = document.getElementById("openPopup");
const closeBtn = document.querySelector(".close-btn");
const modal = document.getElementById("popupModal");

// Open popup
openBtn.addEventListener("click", () => {
  modal.style.display = "block";
});

// Close popup when X is clicked
closeBtn.addEventListener("click", () => {
  modal.style.display = "none";
});

// Close popup when clicking outside modal content
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const generateBtn = document.querySelector(".generate-btn");
  const graphPlaceholder = document.querySelector(".graph-placeholder");

  generateBtn.addEventListener("click", () => {
    // Clear previous content
    graphPlaceholder.innerHTML = "";

    // Create a loading spinner using JavaScript
    const spinner = document.createElement("div");
    spinner.style.border = "4px solid #f3f3f3"; // Light grey background
    spinner.style.borderTop = "4px solid #3498db"; // Blue color for the spinning part
    spinner.style.borderRadius = "50%";
    spinner.style.width = "50px";
    spinner.style.height = "50px";
    spinner.style.animation = "spin 2s linear infinite";
    spinner.style.margin = "0 auto"; // Center the spinner
    graphPlaceholder.appendChild(spinner);

    // Create the spinner animation using JavaScript
    const keyframes = document.createElement("style");
    keyframes.innerHTML = `
      @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
    `;
    document.head.appendChild(keyframes);

    // Simulate a delay (loading effect) before displaying the video placeholder
    setTimeout(() => {
      // Clear the spinner after 3 seconds
      graphPlaceholder.innerHTML = "";

      // Create an empty video element
      const video = document.createElement("video");
      video.setAttribute("controls", "true");
      video.setAttribute("width", "400");
      video.setAttribute("height", "300");

      // Add styled border and background
      video.setAttribute(
        "style",
        "background: #000; border: 2px solid rgb(188, 194, 188); border-radius: 10px; padding: 4px;"
      );

      // Placeholder content for accessibility (won’t display)
      video.innerHTML = "Video placeholder (no source yet)";

      // Append the video to the placeholder
      graphPlaceholder.appendChild(video);
    }, 3000); // Wait for 3 seconds before displaying the video placeholder
  });
});


