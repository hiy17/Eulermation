<p align="center">
  <img src="assets/logo.png" alt="Eulermation Logo" width="150"/>
</p>

<h1 align="center">Eulermation</h1>
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

_**To be added**_

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

