
document.addEventListener('DOMContentLoaded', function() {
    const verticesInput = document.getElementById('vertices');
    const generateBtn = document.getElementById('generate-btn');
    const exampleBtn = document.getElementById('example-btn');
    const realLifeExampleSection = document.getElementById('real-life-example');
    const downloadBtn = document.getElementById('download-btn');
    const errorMessage = document.getElementById('error-message');
    const graphPlaceholder = document.getElementById('graph-placeholder');
    const animationContainer = document.getElementById('animation-container');
    const playButton = document.getElementById('play-button');
    const videPlaceholder = document.getElementById('video-placeholder');
    const videoControls = document.getElementById('video-controls');

    exampleBtnContent = exampleBtn.innerHTML;
    
    const circuitInfo = document.getElementById('circuit-info');
    const circuitPath = document.getElementById('circuit-path');
    const progressBar = document.getElementById('progress-bar');

    realLifeExampleSection.style.display = 'none'
    exampleBtn.disabled = true;
    exampleBtn.style.cursor = "not-allowed";
    downloadBtn.disabled = true;
    downloadBtn.style.cursor = "not-allowed";
    playButton.disabled = true;
    playButton.style.cursor = "not-allowed";

    realLifeExampleSection.style.display = 'none'
    exampleBtn.disabled = true;
    exampleBtn.style.cursor = "not-allowed";
    downloadBtn.disabled = true;
    downloadBtn.style.cursor = "not-allowed";
    playButton.disabled = true;
    playButton.style.cursor = "not-allowed";
    circuitInfo.style.display = 'none';
    
    // Set default light theme
    document.documentElement.setAttribute('data-theme', 'light');
    
    // Initially hide the error message
    errorMessage.style.display = 'none';

    const realLifeSection = document.getElementById('real-life-example');
const showAnotherBtn = document.getElementById('show-another-btn');
const exampleDescriptionTitle = document.getElementById('title-example-description');
const exampleDescription = document.getElementById('example-desc');

let exampleData = [];
let currentIndex = 0;
let hasFetchedExamples = false;

exampleBtn.addEventListener('click', () => {
    if (hasFetchedExamples) {
        const isVisible = realLifeSection.style.display === 'block';
        realLifeSection.style.display = isVisible ? 'none' : 'block';
        exampleBtn.innerHTML = isVisible ? 'Show Real Life Examples' : 'Hide';
        return;
    }

    exampleBtn.innerHTML = '';
    exampleBtn.disabled = true;
    exampleBtn.style.cursor = "not-allowed";
    exampleBtn.classList.add('loading-button');

    fetch('/real_life_examples')
        .then(response => response.json())
        .then(data => {
            exampleBtn.classList.remove('loading-button');
            exampleBtn.innerHTML = 'Hide';
            exampleBtn.disabled = false;
            exampleBtn.style.cursor = "pointer";
            realLifeSection.style.display = 'block';
            realLifeSection.scrollIntoView({ behavior: 'smooth' });

            if (data.real_life_examples) {
                exampleData = Object.entries(data.real_life_examples);
                currentIndex = 0;
                hasFetchedExamples = true;
                showExample(currentIndex);
            }
        })
        .catch(error => {
            console.error('Error fetching real-life examples:', error);
            exampleBtn.classList.remove('loading-button');
            exampleBtn.innerHTML = 'Hide';
            exampleBtn.disabled = false;
            exampleBtn.style.cursor = "pointer";
            realLifeSection.style.display = 'block';
            realLifeSection.scrollIntoView({ behavior: 'smooth' });

            const fallbackExamples = [
                ["Mail Delivery Route", "A mail carrier needs to traverse every street in a neighborhood exactly once to deliver mail efficiently, returning to the post office."],
                ["Street Sweeping Route", "A street sweeper needs to clean every street in a city district exactly once, minimizing wasted travel and returning to the depot."],
                ["Circuit Board Design", "Engineers use Euler circuits to design circuit boards where each connection needs to be traced exactly once to minimize manufacturing complexity."]
            ];

            exampleData = fallbackExamples;
            currentIndex = 0;
            hasFetchedExamples = true;
            showExample(currentIndex);
        });
});

function showExample(index) {
    const [category, story] = exampleData[index];
    exampleDescriptionTitle.textContent = category;
    exampleDescription.textContent = story;
}

showAnotherBtn.addEventListener('click', () => {
    if (!exampleData.length) {
        const fallbackExamples = [
            ["Mail Delivery Route", "A mail carrier needs to traverse every street in a neighborhood exactly once to deliver mail efficiently, returning to the post office."],
            ["Street Sweeping Route", "A street sweeper needs to clean every street in a city district exactly once, minimizing wasted travel and returning to the depot."],
            ["Circuit Board Design", "Engineers use Euler circuits to design circuit boards where each connection needs to be traced exactly once to minimize manufacturing complexity."]
        ];

        currentIndex = (currentIndex + 1) % fallbackExamples.length;
        const [category, story] = fallbackExamples[currentIndex];
        exampleDescriptionTitle.textContent = category;
        exampleDescription.textContent = story;
    } else {
        currentIndex = (currentIndex + 1) % exampleData.length;
        showExample(currentIndex);
    }

    const icon = showAnotherBtn.querySelector('.icon');
    icon.style.transition = 'transform 0.5s ease';
    icon.style.transform = 'rotate(180deg)';
    setTimeout(() => {
        icon.style.transform = 'rotate(0deg)';
    }, 500);
});

    

    // const realLifeSection = document.getElementById('real-life-example');
    // const showAnotherBtn = document.getElementById('show-another-btn');
    // const exampleImage = document.getElementById('example-image');
    // const exampleDescriptionTitle = document.getElementById('title-example-description');
    // const exampleDescription = document.getElementById('example-desc');

    // let exampleData = [];
    // let currentIndex = 0;
    // let hasFetchedExamples = false;

    // exampleBtn.addEventListener('click', () => {
    // // Toggle visibility if examples already fetched
    // if (hasFetchedExamples) {
    // const isVisible = realLifeSection.style.display === 'block';
    // realLifeSection.style.display = isVisible ? 'none' : 'block';
    // exampleBtn.innerHTML = isVisible ? 'Show Real Life Examples' : 'Hide';
    // return;
    // }

    // // Initial loading animation
    // exampleBtn.innerHTML = '';
    // exampleBtn.disabled = true;
    // exampleBtn.style.cursor = "not-allowed";
    // exampleBtn.classList.add('loading-button');

    // fetch('/real_life_examples')
    // .then(response => response.json())
    // .then(data => {
    //     exampleBtn.classList.remove('loading-button');
    //     exampleBtn.innerHTML = 'Hide';
    //     exampleBtn.disabled = false;
    //     exampleBtn.style.cursor = "pointer";
    //     realLifeSection.style.display = 'block';
    //     realLifeSection.scrollIntoView({ behavior: 'smooth' });

    //     if (data.real_life_examples) {
    //         exampleData = Object.entries(data.real_life_examples);
    //         currentIndex = 0;
    //         hasFetchedExamples = true;
    //         showExample(currentIndex);
    //     }
    // })
    // .catch(error => {
    //     console.error('Error fetching real-life examples:', error);
    //     exampleBtn.classList.remove('loading-button');
    //     exampleBtn.innerHTML = 'Hide';
    //     exampleBtn.disabled = false;
    //     exampleBtn.style.cursor = "pointer";
    //     realLifeSection.style.display = 'block';
    //     realLifeSection.scrollIntoView({ behavior: 'smooth' });

    //     const fallbackExamples = [
    //         ["Mail Delivery Route", "A mail carrier needs to traverse every street in a neighborhood exactly once to deliver mail efficiently, returning to the post office."],
    //         ["Street Sweeping Route", "A street sweeper needs to clean every street in a city district exactly once, minimizing wasted travel and returning to the depot."],
    //         ["Circuit Board Design", "Engineers use Euler circuits to design circuit boards where each connection needs to be traced exactly once to minimize manufacturing complexity."]
    //     ];

    //     exampleData = fallbackExamples;
    //     currentIndex = 0;
    //     hasFetchedExamples = true;
    //     showExample(currentIndex);
    // });
    // });

    // // Function to display the example
    // function showExample(index) {
    // const [category, story] = exampleData[index];
    // exampleDescriptionTitle.textContent = category;
    // exampleDescription.textContent = story;
    // }


    // showAnotherBtn.addEventListener('click', () => {
    // if (!exampleData.length) {
    // // Fallback examples if no data was fetched
    // const fallbackExamples = [
    //     ["Mail Delivery Route", "A mail carrier needs to traverse every street in a neighborhood exactly once to deliver mail efficiently, returning to the post office."],
    //     ["Street Sweeping Route", "A street sweeper needs to clean every street in a city district exactly once, minimizing wasted travel and returning to the depot."],
    //     ["Circuit Board Design", "Engineers use Euler circuits to design circuit boards where each connection needs to be traced exactly once to minimize manufacturing complexity."]
    // ];

    // currentIndex = (currentIndex + 1) % fallbackExamples.length;
    // const [category, story] = fallbackExamples[currentIndex];
    // exampleDescriptionTitle.textContent = category;
    // exampleDescription.textContent = story;
    // } else {
    // currentIndex = (currentIndex + 1) % exampleData.length;
    // showExample(currentIndex);
    // }

    // // Add animation to the button icon
    // const icon = showAnotherBtn.querySelector('.icon');
    // icon.style.transition = 'transform 0.5s ease';
    // icon.style.transform = 'rotate(180deg)';
    // setTimeout(() => {
    // icon.style.transform = 'rotate(0deg)';
    // }, 500);
    // });

    // function showExample(index) {
    // const [category, story] = exampleData[index];
    // exampleDescriptionTitle.textContent = category;
    // exampleDescription.textContent = story;

    // // Optional: update image
    // const imageMap = {
    // "Transportation": "transport.svg",
    // "Package Delivery": "delivery.svg",
    // "Tourism": "tourism.svg",
    // "Household Chores": "chores.svg",
    // "Work Tasks": "work.svg",
    // "School Schedule": "school.svg",
    // "Shopping": "shopping.svg",
    // "Social Visits": "social.svg",
    // "Sports": "sports.svg",
    // "Nature": "nature.svg"
    // };

    // const imageSrc = imageMap[category] || "placeholder.svg";
    // exampleImage.src = imageSrc;
    // exampleImage.alt = `${category} illustration`;
    // }


    
    generateBtn.addEventListener('click', function() {
        const value = parseInt(verticesInput.value);

        hasFetchedExamples = false;

        exampleBtn.innerHTML = exampleBtnContent;
        realLifeExampleSection.style.display = 'none'
        exampleBtn.disabled = true;
        exampleBtn.style.cursor = "not-allowed";
        
        
        downloadBtn.disabled = true;
        downloadBtn.style.cursor = "not-allowed";
        playButton.disabled = true;
        playButton.style.cursor = "not-allowed";
        verticesInput.disabled = true;
        verticesInput.style.cursor = "not-allowed";
        circuitInfo.style.display = 'none';


        if (isNaN(value) || value < 3 || value > 8) {
            errorMessage.style.display = 'block';
            return;
        }

        errorMessage.style.display = 'none';
        generateBtn.disabled = true;  
        generateBtn.innerHTML = 'Loading..'; 
        generateBtn.style.backgroundColor = "#e0e0e0"; 
        generateBtn.style.cursor = "not-allowed";

        graphPlaceholder.innerHTML = '<div class="loading"><div class="spinner"></div><p>Generating graph...</p></div>';
        animationContainer.querySelector('.video-placeholder').innerHTML = '<div class="loading"><div class="spinner"></div><p>Creating animation...</p></div>';

        // Abort any previous fetch
        if (window.currentAbortController) {
            window.currentAbortController.abort();
        }

        window.currentAbortController = new AbortController();

        fetch(`/render/eulerian_graph?vertices=${value}`, {
            signal: window.currentAbortController.signal,
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to start rendering.");
                }
                return response.json();  // Parse the JSON response
            })
            .then((data) => {
                const stringEulerFormat = data.euler_circuit;  // Access the string_euler_format from the response

                console.log('Euler Circuit:', stringEulerFormat);  // Do something with the string
                circuitInfo.style.display = 'block';
                animateCircuitPath(stringEulerFormat);

                return waitForVideo(window.currentAbortController.signal);
            })
            .then(() => {
                const video = document.createElement("video");
                video.setAttribute("controls", "true");
                video.setAttribute("autoplay", "true");
                video.setAttribute("muted", "true");
                video.setAttribute("playsinline", "true");
                video.setAttribute("width", "100%");
                video.setAttribute("height", "100%");
                video.setAttribute("style", "background: #fff; border: 1px solid var(--border); border-radius: 10px; padding: 0px;");

                videPlaceholder.style.background = '#ffffff';
                videoControls.style.display = 'none';

                const source = document.createElement("source");
                source.setAttribute("src", `/static/videos/euler_circuits/videos/generate_animation/1080p60/EulerCircuitAnimator.mp4?ts=${Date.now()}`);
                source.setAttribute("type", "video/mp4");
                video.appendChild(source);

                const placeholder = animationContainer.querySelector('.video-placeholder');
                placeholder.innerHTML = '';
                placeholder.appendChild(video);

                const img = document.createElement("img");
                img.setAttribute("src", `/euler_image?ts=${Date.now()}`);
                img.setAttribute("alt", "Euler Circuit Image");
                img.style.width = "80%";
                img.style.height = "220";

                graphPlaceholder.innerHTML = "";
                graphPlaceholder.appendChild(img);

                circuitInfo.style.display = 'block';
            })
            .finally(() => {
                generateBtn.disabled = false;
                generateBtn.style.color = "#ffffff";
                generateBtn.style.backgroundColor = "var(--primary)";
                generateBtn.innerHTML = 'Generate';
                generateBtn.style.cursor = "pointer";
                verticesInput.disabled = false;
                verticesInput.style.cursor = "pointer";
                downloadBtn.disabled = false;
                downloadBtn.style.cursor = "pointer";
                playButton.disabled = false;
                playButton.style.cursor = "pointer";
                exampleBtn.disabled = false;
                exampleBtn.style.cursor = "pointer";
            });
    });

    // Add this function before the waitForVideo function
    function animateCircuitPath(pathString) {
        // Clear previous content
        circuitPath.innerHTML = '';
        
        // Split the path string into nodes and arrows
        const nodes = pathString.split(' → ');
        
        // Create and append elements with staggered animation
        nodes.forEach((node, index) => {
            // Create node element
            const nodeElement = document.createElement('span');
            nodeElement.className = 'path-node';
            nodeElement.textContent = node;
            nodeElement.style.animationName = 'fadeInNode';
            nodeElement.style.animationDuration = '0.5s';
            nodeElement.style.animationFillMode = 'forwards';
            nodeElement.style.animationDelay = `${index * 0.15}s`;
            
            circuitPath.appendChild(nodeElement);
            
            // Add arrow except after the last node
            if (index < nodes.length - 1) {
                const arrowElement = document.createElement('span');
                arrowElement.className = 'path-arrow';
                arrowElement.textContent = '→';
                arrowElement.style.animationName = 'fadeInArrow';
                arrowElement.style.animationDuration = '0.5s';
                arrowElement.style.animationFillMode = 'forwards';
                arrowElement.style.animationDelay = `${index * 0.15 + 0.1}s`;
                
                circuitPath.appendChild(arrowElement);
            }
        });
        
        // Add a highlight effect to the first and last nodes after all animations
        setTimeout(() => {
            const firstNode = circuitPath.querySelector('.path-node');
            const lastNode = circuitPath.querySelectorAll('.path-node')[nodes.length - 1];
            
            if (firstNode && lastNode) {
                firstNode.classList.add('highlight-pulse');
                lastNode.classList.add('highlight-pulse');
            }
        }, nodes.length * 150 + 500);
    }


    // Polls the server until the video is available or retries are exhausted
    function waitForVideo(signal, retries = 20, interval = 1000) {
        return new Promise((resolve, reject) => {
            const tryFetch = () => {
                if (signal.aborted) {
                    reject(new DOMException("Aborted", "AbortError"));
                    return;
                }

                fetch(`/euler_animation?ts=${Date.now()}`)
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
    }

    downloadBtn.addEventListener('click', function () {
        // Add a button press animation
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'translateY(-2px)';
        }, 150);

        // Actual download logic
        const videoUrl = `/static/videos/euler_circuits/videos/generate_animation/1080p60/EulerCircuitAnimator.mp4?ts=${Date.now()}`;
        const link = document.createElement('a');
        link.href = videoUrl;
        link.download = 'EulerCircuitAnimator.mp4'; // Suggests the filename
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });


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

// Add scroll effect for header
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if (window.scrollY > 10) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});