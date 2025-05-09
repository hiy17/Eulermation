document.addEventListener('DOMContentLoaded', function () {
    // Tabs
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));

            button.classList.add('active');
            const tabId = button.getAttribute('data-tab');
            const target = document.getElementById(tabId);
            if (target) {
                target.classList.add('active');
            }
        });
    });

    // Set default theme (or load saved one)
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

        let themeToApply = 'light';
        if (savedTheme) {
            themeToApply = savedTheme;
        } else if (prefersDark) {
            themeToApply = 'dark';
        }

        document.documentElement.setAttribute('data-theme', themeToApply);
        themeToggle.textContent = themeToApply === 'dark' ? '🌙' : '☀️';

        themeToggle.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            themeToggle.textContent = newTheme === 'dark' ? '🌙' : '☀️';
            localStorage.setItem('theme', newTheme);
        });
    }
});

// Scroll header effect
window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    if (header) {
        if (window.scrollY > 10) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
});

// Video functions
function openVideo() {
    const videoPopup = document.getElementById('videoPopup');
    const videoFrame = document.getElementById('tutorialVideo');
    if (videoPopup && videoFrame) {
        videoFrame.src = "https://www.youtube.com/embed/o0cDpp6a7EY?autoplay=1";
        videoPopup.classList.add('active');
    }
}

function closeVideo() {
    const videoPopup = document.getElementById('videoPopup');
    const videoFrame = document.getElementById('tutorialVideo');
    if (videoPopup && videoFrame) {
        videoFrame.src = "";
        videoPopup.classList.remove('active');
    }
}

// Expose to global if needed
window.openVideo = openVideo;
window.closeVideo = closeVideo;