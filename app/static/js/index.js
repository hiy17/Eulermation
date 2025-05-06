const openBtn = document.getElementById("openPopup");
const closeBtn = document.querySelector(".close-btn");
const modal = document.getElementById("popupModal");


function enableOpenBtn() {
  openBtn.disabled = false;
  openBtn.style.opacity = "1";
  openBtn.style.cursor = "pointer";
}

function disableOpenBtn() {
  openBtn.disabled = true;
  openBtn.style.opacity = "0.5";
  openBtn.style.cursor = "not-allowed";
}

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
    const MAX_VERTICES = 8;
  
    let currentAbortController = null;
  
    // Add keyframes for animations if not already present
    if (!document.getElementById("customKeyframes")) {
      const keyframes = document.createElement("style");
      keyframes.id = "customKeyframes";
      keyframes.innerHTML = `
        @keyframes rotateDots {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
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
  
    const showErrorMessage = (text) => {
      const errorMsg = document.createElement("p");
      errorMsg.textContent = text;
      errorMsg.style.color = "red";
      errorMsg.style.textAlign = "center";
      errorMsg.style.fontWeight = "600";
      errorMsg.style.animation = "bounceIn 0.5s ease";
  
      vertexInput.style.animation = "shakeInput 0.3s ease-out";
  
      graphPlaceholder.appendChild(errorMsg);
  
      vertexInput.addEventListener("animationend", () => {
        vertexInput.style.animation = "none";
      });
    };
  
    const handleGenerate = () => {
      disableOpenBtn(); 
      const value = parseInt(vertexInput.value);
      graphPlaceholder.innerHTML = "";
  
      // Abort previous session
      if (currentAbortController) {
        currentAbortController.abort();
      }
  
      if (isNaN(value) || value < MIN_VERTICES || value > MAX_VERTICES) {
        showErrorMessage(`Please enter a number between ${MIN_VERTICES} and ${MAX_VERTICES}.`);
        return;
      }
  
      const loading = createLoadingAnimation();
      graphPlaceholder.appendChild(loading);
  
      currentAbortController = new AbortController();
  
      fetch(`/render/eulerian_graph?vertices=${value}`, {
        signal: currentAbortController.signal,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Failed to render animation.");
          }
          return waitForVideo(currentAbortController.signal);
        })
        .then(() => {
          graphPlaceholder.innerHTML = "";
  
          const video = document.createElement("video");
          video.setAttribute("autoplay", "true");
          video.setAttribute("muted", "true"); // Required for autoplay to work
          video.setAttribute("playsinline", "true"); // Important for iOS Safari
          video.setAttribute("controls", "true");
          video.setAttribute("width", "400");
          video.setAttribute("height", "300");
          video.style.background = "#fff";
          video.style.border = "2px solid rgb(188, 194, 188)";
          video.style.borderRadius = "10px";
          video.style.padding = "0px";
          video.style.animation = "fadeIn 0.5s ease-out";
  
          const source = document.createElement("source");
          source.src = `/euler_animation?ts=${new Date().getTime()}`;
          source.type = "video/mp4";
          video.appendChild(source);
  
          graphPlaceholder.appendChild(video);
          video.load();
          enableOpenBtn(); // <-- Re-enable button after video is ready
        })
        .catch((error) => {
          if (error.name !== "AbortError") {
            graphPlaceholder.innerHTML = "";
            showErrorMessage("Error generating video. Try again.");
            console.error(error);
          }
          enableOpenBtn(); // <-- Ensure re-enable on error too
        });
    };
  
    vertexInput.addEventListener("input", handleGenerate);
  
    // Auto-generate animation if default is 3
    if (parseInt(vertexInput.value) === 3) {
      handleGenerate();
    }
  });
  
  const waitForVideo = (signal, retries = 20, interval = 1000) => {
    return new Promise((resolve, reject) => {
      const tryFetch = () => {
        if (signal.aborted) {
          reject(new DOMException("Aborted", "AbortError"));
          return;
        }
  
        fetch(`/euler_animation?ts=${new Date().getTime()}`)
          .then((response) => {
            if (signal.aborted) {
              reject(new DOMException("Aborted", "AbortError"));
              return;
            }
  
            if (response.ok) {
              resolve();
            } else if (retries > 0) {
              setTimeout(() => tryFetch(--retries), interval);
            } else {
              reject("Video not available after waiting.");
            }
          })
          .catch(() => {
            if (signal.aborted) {
              reject(new DOMException("Aborted", "AbortError"));
              return;
            }
  
            if (retries > 0) {
              setTimeout(() => tryFetch(--retries), interval);
            } else {
              reject("Failed to fetch video.");
            }
          });
      };
  
      tryFetch();
    });
  };
  

















// document.addEventListener("DOMContentLoaded", () => {
//   const graphPlaceholder = document.querySelector(".graph-placeholder");
//   const vertexInput = document.getElementById("vertices");

//   const MIN_VERTICES = 3;
//   const MAX_VERTICES = 8;

//   // Add keyframes for animations if not already present
//   if (!document.getElementById("customKeyframes")) {
//     const keyframes = document.createElement("style");
//     keyframes.id = "customKeyframes";
//     keyframes.innerHTML = `
//       @keyframes rotateDots {
//         0% {
//           transform: rotate(0deg);
//         }
//         100% {
//           transform: rotate(360deg);
//         }
//       }

//       @keyframes fadeIn {
//         from { opacity: 0; }
//         to { opacity: 1; }
//       }

//       @keyframes shakeInput {
//         0% { transform: translateX(0); }
//         25% { transform: translateX(-4px); }
//         50% { transform: translateX(4px); }
//         75% { transform: translateX(-4px); }
//         100% { transform: translateX(0); }
//       }

//       @keyframes bounceIn {
//         0% { transform: scale(0.6); opacity: 0; }
//         60% { transform: scale(1.1); opacity: 1; }
//         80% { transform: scale(0.95); }
//         100% { transform: scale(1); }
//       }
//     `;
//     document.head.appendChild(keyframes);
//   }

//   const createLoadingAnimation = () => {
//     const container = document.createElement("div");
//     container.style.position = "relative";
//     container.style.width = "50px";
//     container.style.height = "50px";
//     container.style.display = "flex";
//     container.style.justifyContent = "center";
//     container.style.alignItems = "center";
//     container.style.transformOrigin = "center";
//     container.style.animation = "rotateDots 2.5s linear infinite";

//     const createDot = (angle) => {
//       const dot = document.createElement("div");
//       dot.style.position = "absolute";
//       dot.style.width = "6px";
//       dot.style.height = "6px";
//       dot.style.backgroundColor = "#00412E";
//       dot.style.borderRadius = "50%";
//       dot.style.transform = `rotate(${angle}deg) translateX(18px)`;
//       container.appendChild(dot);
//     };

//     for (let i = 0; i < 8; i++) {
//       createDot(i * 45);
//     }

//     return container;
//   };

//   const showVideoPlaceholder = () => {
//     graphPlaceholder.innerHTML = "";

//     const video = document.createElement("video");
//     video.setAttribute("controls", "true");
//     video.setAttribute("width", "400");
//     video.setAttribute("height", "400");
//     video.style.background = "#000";
//     video.style.border = "2px solid rgb(188, 194, 188)";
//     video.style.borderRadius = "10px";
//     video.style.padding = "4px";
//     video.style.animation = "fadeIn 0.5s ease-out";
//     video.innerHTML = "Video placeholder (no source yet)";

//     graphPlaceholder.appendChild(video);
//   };

//   const showErrorMessage = (text) => {
//     const errorMsg = document.createElement("p");
//     errorMsg.textContent = text;
//     errorMsg.style.color = "red";
//     errorMsg.style.textAlign = "center";
//     errorMsg.style.fontWeight = "600";
//     errorMsg.style.animation = "bounceIn 0.5s ease";

//     // Add shake animation to the input field
//     vertexInput.style.animation = "shakeInput 0.3s ease-out"; // Reduced duration

//     graphPlaceholder.appendChild(errorMsg);

//     // Reset the input animation after it ends
//     vertexInput.addEventListener("animationend", () => {
//       vertexInput.style.animation = "none";
//     });
//   };


//   const handleGenerate = () => {
//     const value = parseInt(vertexInput.value);
//     graphPlaceholder.innerHTML = "";
  
//     if (isNaN(value) || value < MIN_VERTICES || value > MAX_VERTICES) {
//       showErrorMessage(`Please enter a number between ${MIN_VERTICES} and ${MAX_VERTICES}.`);
//       return;
//     }
  
//     const loading = createLoadingAnimation();
//     graphPlaceholder.appendChild(loading);
  
//     fetch(`/render/eulerian_graph?vertices=${value}`)
//       .then(response => {
//         if (!response.ok) {
//           throw new Error("Failed to render animation.");
//         }
  
//         return waitForVideo();
//       })
//       .then(() => {
//         graphPlaceholder.innerHTML = "";
  
//         const video = document.createElement("video");
//         video.setAttribute("controls", "true");
//         video.setAttribute("width", "400");
//         video.setAttribute("height", "300");
//         video.style.background = "#000";
//         video.style.border = "2px solid rgb(188, 194, 188)";
//         video.style.borderRadius = "10px";
//         video.style.padding = "4px";
//         video.style.animation = "fadeIn 0.5s ease-out";
  
//         const source = document.createElement("source");
//         source.src = `/animation?ts=${new Date().getTime()}`;
//         source.type = "video/mp4";
//         video.appendChild(source);
  
//         graphPlaceholder.appendChild(video);
//         video.load();
//       })
//       .catch(error => {
//         graphPlaceholder.innerHTML = "";
//         showErrorMessage("Error generating video. Try again.");
//         console.error(error);
//       });
//   };

  
  

//   vertexInput.addEventListener("input", handleGenerate); // Live error checking
//   // vertexInput.addEventListener("change", handleGenerate);

// });


// const waitForVideo = (retries = 20, interval = 1000) => {
//   return new Promise((resolve, reject) => {
//     const tryFetch = () => {
//       fetch(`/animation?ts=${new Date().getTime()}`)
//         .then(response => {
//           if (response.ok) {
//             resolve();
//           } else if (retries > 0) {
//             setTimeout(() => tryFetch(--retries), interval);
//           } else {
//             reject("Video not available after waiting.");
//           }
//         })
//         .catch(() => {
//           if (retries > 0) {
//             setTimeout(() => tryFetch(--retries), interval);
//           } else {
//             reject("Failed to fetch video.");
//           }
//         });
//     };
//     tryFetch();
//   });
// };
