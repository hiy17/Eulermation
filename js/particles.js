particlesJS("particles-js", {
  particles: {
    number: {
      value: 60,
      density: {
        enable: true,
        value_area: 800,
      },
    },
    color: { value: "#006400" }, 
    shape: {
      type: "circle",
      stroke: { width: 0, color: "#006400" }, 
    },
    opacity: {
      value: 0.7,
      random: false,
    },
    size: {
      value: 3,
      random: true,
    },
    line_linked: {
      enable: true,
      distance: 150,
      color: "#006400", 
      opacity: 0.7,
      width: 1,
    },
    move: {
      enable: true,
      speed: 2,
      direction: "none",
      straight: false,
    },
  },
  interactivity: {
    detect_on: "canvas",
    events: {
      onhover: {
        enable: true,
        mode: "repulse",
      },
    },
  },
  retina_detect: true,
});
