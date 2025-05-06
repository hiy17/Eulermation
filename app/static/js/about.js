// Fade-in on scroll with enhanced animation effects
const faders = document.querySelectorAll('.about-paragraph, .mission-section, .team-section, .tech-section, .testimonials-section, .roadmap-section');

const appearOptions = {
  threshold: 0.1, // Percentage of the element that needs to be visible before the fade-in happens
  rootMargin: "0px 0px -50px 0px" // Offset for the scroll trigger
};

// Create an IntersectionObserver to handle the fade-in animations
const appearOnScroll = new IntersectionObserver(function (entries, observer) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return; // Only trigger animation if the element is in view

    // Add multiple classes to trigger various animations
    entry.target.classList.add('fade-in', 'scale-in', 'slide-up');
    
    // Unobserve the element once the animation has triggered to avoid triggering multiple times
    observer.unobserve(entry.target);
  });
}, appearOptions);

// Observe each element for the scroll animation
faders.forEach(fader => {
  appearOnScroll.observe(fader);
});
