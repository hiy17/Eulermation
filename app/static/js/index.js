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
  const graphPlaceholder = document.querySelector(".graph-placeholder");
  const vertexInput = document.getElementById("vertices");

  const MIN_VERTICES = 3;
  const MAX_VERTICES = 10;

  // Add keyframes for animations if not already present
  if (!document.getElementById("customKeyframes")) {
    const keyframes = document.createElement("style");
    keyframes.id = "customKeyframes";
    keyframes.innerHTML = `
      @keyframes rotateDots {
        0% {
          transform: rotate(0deg);
        }
        100% {
          transform: rotate(360deg);
        }
      }

      @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }

      @keyframes shakeInput {
        0% { transform: translateX(0); }
        25% { transform: translateX(-4px); }
        50% { transform: translateX(4px); }
        75% { transform: translateX(-4px); }
        100% { transform: translateX(0); }
      }

      @keyframes bounceIn {
        0% { transform: scale(0.6); opacity: 0; }
        60% { transform: scale(1.1); opacity: 1; }
        80% { transform: scale(0.95); }
        100% { transform: scale(1); }
      }
    `;
    document.head.appendChild(keyframes);
  }

  const createLoadingAnimation = () => {
    const container = document.createElement("div");
    container.style.position = "relative";
    container.style.width = "50px";
    container.style.height = "50px";
    container.style.display = "flex";
    container.style.justifyContent = "center";
    container.style.alignItems = "center";
    container.style.transformOrigin = "center";
    container.style.animation = "rotateDots 2.5s linear infinite";

    const createDot = (angle) => {
      const dot = document.createElement("div");
      dot.style.position = "absolute";
      dot.style.width = "6px";
      dot.style.height = "6px";
      dot.style.backgroundColor = "#00412E";
      dot.style.borderRadius = "50%";
      dot.style.transform = `rotate(${angle}deg) translateX(18px)`;
      container.appendChild(dot);
    };

    for (let i = 0; i < 8; i++) {
      createDot(i * 45);
    }

    return container;
  };

  const showVideoPlaceholder = () => {
    graphPlaceholder.innerHTML = "";

    const video = document.createElement("video");
    video.setAttribute("controls", "true");
    video.setAttribute("width", "400");
    video.setAttribute("height", "300");
    video.style.background = "#000";
    video.style.border = "2px solid rgb(188, 194, 188)";
    video.style.borderRadius = "10px";
    video.style.padding = "4px";
    video.style.animation = "fadeIn 0.5s ease-out";
    video.innerHTML = "Video placeholder (no source yet)";

    graphPlaceholder.appendChild(video);
  };

  const showErrorMessage = (text) => {
    const errorMsg = document.createElement("p");
    errorMsg.textContent = text;
    errorMsg.style.color = "red";
    errorMsg.style.textAlign = "center";
    errorMsg.style.fontWeight = "600";
    errorMsg.style.animation = "bounceIn 0.5s ease";

    // Add shake animation to the input field
    vertexInput.style.animation = "shakeInput 0.3s ease-out"; // Reduced duration

    graphPlaceholder.appendChild(errorMsg);

    // Reset the input animation after it ends
    vertexInput.addEventListener("animationend", () => {
      vertexInput.style.animation = "none";
    });
  };

  const handleGenerate = () => {
    const value = parseInt(vertexInput.value);
    graphPlaceholder.innerHTML = "";

    if (isNaN(value) || value < MIN_VERTICES || value > MAX_VERTICES) {
      showErrorMessage(`Please enter a number between ${MIN_VERTICES} and ${MAX_VERTICES}.`);
      return;
    }

    graphPlaceholder.appendChild(createLoadingAnimation());
    setTimeout(showVideoPlaceholder, 3000); // Simulate loading time
  };

  vertexInput.addEventListener("input", handleGenerate); // Live error checking
});
