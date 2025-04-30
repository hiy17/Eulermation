document.addEventListener("DOMContentLoaded", () => {
  // Modal functionality
  const openBtn = document.getElementById("openPopup");
  const closeBtn = document.querySelector(".close-btn");
  const modal = document.getElementById("popupModal");
  
  openBtn.addEventListener('click', () => {
    modal.style.display = "block";
  });
  
  closeBtn.addEventListener('click', () => {
    modal.style.animation = 'fadeOut 0.2s ease-out forwards';
    modal.querySelector('.modal-content').style.animation = 'popOut 0.2s ease-out forwards';
    
    // Remove modal after animation completes
    setTimeout(() => {
      modal.style.display = "none";
      // Reset animations for next open
      modal.style.animation = '';
      modal.querySelector('.modal-content').style.animation = '';
    }, 200);
  });
  
  window.addEventListener('click', (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });

  // Graph functionality
  const generateBtn = document.querySelector('.generate-btn');
  const circuitBtn = document.querySelector('.circuit-btn');
  const vertexInput = document.getElementById('vertices');
  let graph = {};

  function generateRandomGraph(vertexCount) {
    graph = {};
    for (let i = 0; i < vertexCount; i++) {
      graph[i] = [];
    }

    // Randomly add edges
    for (let i = 0; i < vertexCount; i++) {
      for (let j = i + 1; j < vertexCount; j++) {
        if (Math.random() > 0.5) {
          graph[i].push(j);
          graph[j].push(i);
        }
      }
    }
  }

  function isEulerian(g) {
    for (let vertex in g) {
      if (g[vertex].length % 2 !== 0) return false;
    }
    return true;
  }

  function findEulerCircuit(graph) {
    const g = JSON.parse(JSON.stringify(graph));
    const stack = [];
    const circuit = [];
    let current = Object.keys(g)[0];

    while (stack.length || g[current].length) {
      if (!g[current].length) {
        circuit.push(current);
        current = stack.pop();
      } else {
        stack.push(current);
        let next = g[current].pop();
        g[next] = g[next].filter(v => v !== parseInt(current));
        current = next;
      }
    }

    circuit.push(current);
    return circuit;
  }

  generateBtn.addEventListener("click", () => {
    const numVertices = parseInt(vertexInput.value);
    generateRandomGraph(numVertices);
    alert("Graph generated! Click 'Euler Circuit combinations' to view results.");
  });

  circuitBtn.addEventListener("click", () => {
    const modal = document.getElementById("popupModal");
    const iframe = modal.querySelector("iframe");
    const eulerian = isEulerian(graph);

    let resultHTML = "";

    if (!Object.keys(graph).length) {
      resultHTML = "<p style='color: red;'>Please generate a graph first.</p>";
    } else if (!eulerian) {
      resultHTML = "<p style='color: red;'>The graph is not Eulerian. No Euler circuits exist.</p>";
    } else {
      const circuit = findEulerCircuit(graph);
      resultHTML = `<p><strong>Euler Circuit:</strong> ${circuit.join(" → ")}</p>`;
    }

    iframe.contentWindow.postMessage({ html: resultHTML }, "*");
    modal.style.display = "block";
  });
});

function generateEulerianGraph(vertexCount) {
  let edges = [];
  let degree = new Array(vertexCount).fill(0);

  // Ensure graph is connected — build a cycle to start
  for (let i = 0; i < vertexCount; i++) {
    let next = (i + 1) % vertexCount;
    edges.push([i, next]);
    degree[i]++;
    degree[next]++;
  }

  // Add more random edges, ensuring even degrees
  while (true) {
    let oddVertices = degree.map((deg, idx) => deg % 2 !== 0 ? idx : -1).filter(x => x !== -1);
    if (oddVertices.length === 0) break;

    let [u, v] = [oddVertices[0], oddVertices[1]];
    if (!edges.find(([a, b]) => (a === u && b === v) || (a === v && b === u))) {
      edges.push([u, v]);
      degree[u]++;
      degree[v]++;
    }
  }

  return edges;
}