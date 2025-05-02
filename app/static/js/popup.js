
document.querySelectorAll('.popup-sb').forEach(button => {
    button.addEventListener('click', function () {
      if (this.textContent.includes('▶')) {
        this.textContent = '⏸ Pause';
      } else {
        this.textContent = '▶ Show';
      }
    });
  });

  document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.getElementById("fullscreenButton"); // Renamed
    const modal = document.getElementById("fullscreenModalContainer"); // Renamed
    const closeBtn = modal.querySelector(".min-btn");
  
    if (openBtn && modal && closeBtn) {
      openBtn.addEventListener("click", function () {
        modal.style.display = "block";
      });
  
      closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
      });
  
      window.addEventListener("click", function (event) {
        if (event.target === modal) {
          modal.style.display = "none";
        }
      });
    }
  });
  
  document.querySelector('.zoom-button').addEventListener('click', function() {
    // Send message to parent window to open the modal
    window.parent.postMessage({ 
      type: 'OPEN_ZOOM_MODAL',
      content: document.querySelector('.animation-box').innerHTML 
    }, '*');
  });
  
  // Toggle show/pause buttons
  document.querySelectorAll('.popup-sb').forEach(button => {
    button.addEventListener('click', function() {
      if (this.textContent.includes('▶')) {
        this.textContent = '⏸ Pause';
      } else {
        this.textContent = '▶ Show';
      }
    });
  });