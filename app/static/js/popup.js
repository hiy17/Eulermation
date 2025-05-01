
document.querySelectorAll('.popup-sb').forEach(button => {
    button.addEventListener('click', function () {
      if (this.textContent.includes('▶')) {
        this.textContent = '⏸ Pause';
      } else {
        this.textContent = '▶ Show';
      }
    });
  });