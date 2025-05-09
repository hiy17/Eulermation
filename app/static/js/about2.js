document.addEventListener('DOMContentLoaded', function() {
    // Any JavaScript functionality can be added here
     // Set default light theme
     document.documentElement.setAttribute('data-theme', 'light');

     const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Function to toggle between light and dark theme
    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);

        // Update the button text
        themeToggle.textContent = newTheme === 'dark' ? '🌙' : '☀️';

        // Store the theme preference in local storage
        localStorage.setItem('theme', newTheme);
    }

    // Event listener for the theme toggle button
    themeToggle.addEventListener('click', toggleTheme);

    // Check for saved theme preference in local storage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggle.textContent = savedTheme === 'dark' ? '🌙' : '☀️';
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        // If no theme is saved, check the user's system preference
        document.documentElement.setAttribute('data-theme', 'dark');
        themeToggle.textContent = '🌙';
    }
});

window.addEventListener('scroll', function () {
const header = document.querySelector('header');
if (window.scrollY > 10) {
    header.classList.add('scrolled');
} else {
    header.classList.remove('scrolled');
}
});
