function fetchAndDisplayCircuits() {
  fetch('/access/euler_circuits')
    .then(response => {
      if (!response.ok) {
        return response.text().then(text => {
          console.error("Error fetching Euler circuits:", text);
          throw new Error("Failed to fetch Euler circuits");
        });
      }
      return response.json();
    })
    .then(data => {
      if (!data || data.length === 0) {
        console.log("No circuits received.");
        return;
      }

      console.log("Received Euler Circuits:", data);

      // Clear all previous displays
      document.querySelectorAll('.combo-box .circuit-display').forEach(div => div.remove());

      // Update each combo-box
      const comboBoxes = document.querySelectorAll('.combo-box');
      comboBoxes.forEach((comboBox, index) => {
        if (data[index]) {
          const displayDiv = document.createElement('div');
          displayDiv.className = 'circuit-display';
          displayDiv.textContent = data[index];
          comboBox.appendChild(displayDiv);
          comboBox.style.height = 'auto';
        }
      });
    })
    .catch(error => {
      console.error("Error in Euler circuit flow:", error);
    });
}

// Run once on load
document.addEventListener("DOMContentLoaded", function () {
  fetchAndDisplayCircuits();

  // Also respond to changes in vertex count (if the element exists in this document)
  const vertexInput = window.parent.document.querySelector('#vertices');
  if (vertexInput) {
    vertexInput.addEventListener('change', () => {
      fetchAndDisplayCircuits();
    });
  }
});
