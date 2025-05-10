<p align="center">
  <img src="assets/logo.png" alt="Eulermation Logo" width="150"/>
</p>

<h1 align="center">Eulermation</h1>
<p align="center"><em>Euler Circuit Animation Generator</em></p>

---

## 🎯 Overview

**Eulermation** is an interactive web-based platform that helps users learn and explore **Euler circuits** through dynamic graph visualizations, downloadable animations, and real-life application examples. Designed for students, educators, and graph theory enthusiasts, Eulermation transforms abstract mathematical concepts into intuitive and visual experiences.

## 📚 Purpose

The purpose of Eulermation is to enhance the study and teaching of Euler circuits by providing:
- A hands-on environment for graph creation.
- Automatic generation of Eulerian circuits.
- Real-world applications that connect theory to practice.
- Downloadable MP4 animations to reinforce learning.

## 🔍 Scope

- Allows graph creation with **3 to 8 vertices**.
- Generates **one valid Euler circuit** if the graph meets Eulerian conditions.
- Provides **MP4 downloads** of animated circuit traversals.
- Offers up to **10 contextual real-world scenarios**.
- Fixed layout and styling; customization options are not supported.

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

| Name       | Role                     |
|------------|--------------------------|
| **Ace**     | Backend Developer        |
| **Elizabeth** | Frontend Developer     |
| **Jude**    | Project Manager / Full Stack Developer |
| **Rain**    | Frontend Developer       |

---

