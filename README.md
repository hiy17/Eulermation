<p align="center">
  <img src="/app/static/assets/eulermation_logo.png" alt="Eulermation Logo" width="150"/>
</p>
<p align="center"><em>Euler Circuit Animation Generator</em></p>

---

## 🎯 Overview

**Eulermation** is an interactive web-based platform that helps users learn and explore **Euler circuits** through dynamic graph visualizations, downloadable animations, and real-life application examples. Designed for students, educators, and graph theory enthusiasts, Eulermation transforms abstract mathematical concepts into intuitive and visual experiences.

## ⚙️ Key Features

### 🖥️ Graph Visualization Panel
- **Input Field**: Specify vertex count (3–8).
- **Interactive Display**: Labeled nodes (A–H) and dynamic edge rendering.
- **Live Updates**: Graph adjusts in real time as inputs change.

### 🎛️ Control Interface
- **Generate**: Creates a valid Eulerian graph.
- **Download**: Renders and saves an animation using Manim in MP4 format.
- **Real-Life Example**: Displays a real-world problem modeled on the current graph.
- **Show Another Example**: Cycles through additional applications of Euler circuits.

### 📖 Tutorial Section
- Step-by-step guides and interactive lessons on Euler circuits.
- Hands-on graph creation and visual circuit traversal.

### ℹ️ About Section
- Introduction to Eulermation’s mission and use cases.
- Credits to contributors and third-party technologies used.

## 🏗️ System Architecture

### Frontend
- **Technologies**: HTML, CSS, JavaScript
- **Functionality**: User interface for graph input, animation viewing, and feature interaction.

### Backend
- **Technologies**: Python, Flask
- **Responsibilities**:
  - Validate inputs and graph structure.
  - Generate Eulerian circuits.
  - Render animations with **Manim**.
  - Provide real-world examples using the **Gemini API**.

### Algorithm Engine
- Detects Eulerian graphs using standard conditions.
- Constructs a single Euler circuit.
- Optimized for small graphs (3–8 vertices).
- Generates frame-by-frame animations compiled to MP4.

### Data Handling
- **No persistent database**; session data stored temporarily.
- Old animation frames cleared to conserve storage.
- Future versions may support session or history storage.

## 🚀 Installation

# Via Command Prompt(CMD)

## Step 1: Clone the Repository

1. **Clone the GitHub repository** to your local machine using Git. Open a terminal and run:

    ```bash
    git clone https://github.com/hiy17/Eulermation.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd Eulermation
    ```

## Step 2: Set Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies and avoid conflicts with system-wide packages.

1. **Create a virtual environment**:

    On Windows:
    ```bash
    python -m venv venv
    ```

    On macOS/Linux:
    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment**:

    On Windows:
    ```bash
    .\venv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

    You should see `(venv)` at the beginning of the terminal prompt, indicating that the virtual environment is active.

## Step 3: Install Required Dependencies

1. **Install the required dependencies** listed in the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the libraries that your Flask app depends on, including Flask, Manim, and any other required packages.

## Step 4: Run the Flask Application

1. **Run the app** using the `run.py` file.

    On Windows:
    ```bash
    python run.py
    ```

    On macOS/Linux:
    ```bash
    python3 run.py
    ```

    This will start the Flask development server, and you should see output indicating that the server is running. By default, Flask will run on `http://127.0.0.1:5000`.

## Step 5: Access the App in Your Browser

1. Open a web browser and go to:

    ```
    http://127.0.0.1:5000
    ```

2. You should now be able to interact with your app and generate Euler circuit animations!

---

## Step 6: Troubleshooting (If Needed)

1. If you encounter errors during the installation or while running the app, double-check that you have the correct version of Python installed (based on your app’s dependencies).

    You can check the Python version with:

    ```bash
    python --version
    ```

    or for Python 3:

    ```bash
    python3 --version
    ```

2. If there are issues related to missing dependencies, ensure that the `requirements.txt` is up-to-date or try installing them manually using `pip`.

3. If you experience issues with your app not starting correctly, check the error messages in the terminal for guidance.

---

## 🧪 Usage

_**To be added**_

## 📸 Screenshots / Demo

_**To be added**_

## 👥 Contributors

| Name        | Role                                      |
|-------------|-------------------------------------------|
| [Ace](https://github.com/AcePenaflorida)          | Backend Developer                      |
| [Elizabeth](https://github.com/elizalindo) | Frontend Developer                     |
| [Jude](https://github.com/hiy17)        | Project Manager / Full Stack Developer |
| [Rain](https://github.com/rnlyra)        | Frontend Developer                     |

## 🙏 Acknowledgments

We would like to express our sincere gratitude to the following resources and communities that made this project possible:

- **[Manim](https://www.manim.community/)** – for powering the smooth and customizable graph animations.
- **[Flask](https://flask.palletsprojects.com/)** – for providing a lightweight and flexible backend framework.
- **[Gemini API](https://ai.google.dev/gemini-api)** – for generating insightful real-life applications of Euler circuits.
- **Graph Theory Enthusiast Community** – for the theoretical foundations and valuable open-source discussions.
- All educators, learners, and contributors who continue to inspire innovations in educational tools.

Special thanks to [Ma'am Fatima](https://github.com/marieemoiselle) for her invaluable guidance, encouragement, and thoughtful feedback throughout the development of Eulermation. Her support played a key role in shaping this project.

---

