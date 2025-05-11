from flask import Flask, jsonify, request, send_file, render_template, send_from_directory, session
import subprocess
import os
import shutil
import glob
import sys
import json
import networkx as nx

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.manim_engine.graph_utils import EulerianGraphGenerator
from app.api.gemini_api import generate_euler_examples


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
EULER_VIDEO_PATH = os.path.join(BASE_DIR, "static", "videos", "euler_circuits", "videos", "generate_animation", "1080p60", "EulerCircuitAnimator.mp4")
EULER_IMAGE_PATH = os.path.join(
    BASE_DIR,
    "static",
    "videos",
    "euler_circuits",
    "images",
    "generate_animation",
    "euler_circuit.png"  # use .png instead of .svg
)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = 'your-secure-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')


def setup_euler_artifacts(num_vertices):
    generator = EulerianGraphGenerator(num_vertices)
    euler_graph, euler_circuit = generator.generate_eulerian_graph()
    parse_euler_circuits = format_circuit(euler_circuit)

    if euler_graph is None:
        return
    
    session['parse_euler_circuits'] = parse_euler_circuits
    
    return euler_graph, euler_circuit

@app.route('/real_life_examples')
def generate_examples():
    euler_circuit = session.get('parse_euler_circuits')
    real_life_examples = generate_euler_examples(euler_circuit)

    try:
        examples_json = json.loads(real_life_examples)
    except Exception as e:
        return jsonify({"error": "Failed to parse real-life examples", "details": str(e)}), 500

    return jsonify({
        "real_life_examples": examples_json
    })


def build_euler_graph(eulerian_graph_json, euler_circuit_json):
    env = os.environ.copy()
    env["EULERIAN_GRAPH"] = eulerian_graph_json  # Serialized JSON graph
    env["EULERIAN_CIRCUIT"] = euler_circuit_json

    return {
        "command": [
            "manim",
            "-qh",
            "--media_dir", os.path.join(BASE_DIR, "static", "videos", "euler_circuits"),
            os.path.join(BASE_DIR, "manim_engine", "generate_animation.py"),
            "EulerCircuitAnimator",  # ✅ Scene class name
        ],
        
        "env": env
    }

def format_circuit(circuit_dict):
    # Get the edges of the first circuit in the dictionary
    for circuit_name, edges in circuit_dict.items():
        # Create a dictionary for easy lookup of edges
        edge_dict = {start: end for start, end in edges}
        
        # Start with the first vertex of the first edge
        start_vertex = edges[0][0]
        formatted_circuit = start_vertex
        current_vertex = start_vertex
        
        # Follow the edges and append to the formatted circuit
        visited_edges = set()  # To avoid revisiting the same edge
        
        while len(visited_edges) < len(edges):
            for i, (start, end) in enumerate(edges):
                if start == current_vertex and (start, end) not in visited_edges:
                    formatted_circuit += f"->{end}"
                    visited_edges.add((start, end))
                    current_vertex = end
                    break

        return formatted_circuit

@app.route('/render/eulerian_graph')
def render_euler_graph_animation():
    try:
        num_vertices = int(request.args.get("vertices", 6))
        if not (3 <= num_vertices <= 8):
            return "Invalid number of vertices", 400
    except ValueError:
        return "Invalid input", 400

    result = setup_euler_artifacts(num_vertices)

    if result is None:
        return "Failed to generate Eulerian graph", 500
    

    # euler_graph, _ = result  
    # euler_graph_json = json.dumps(nx.node_link_data(euler_graph))  # ✅ Serialize the graph

    euler_graph, euler_circuits = result
    string_euler_format = format_circuit(euler_circuits)

    print(f'Circuits at /render/eulerian_graph: {string_euler_format}')
    euler_graph_json = json.dumps(nx.node_link_data(euler_graph))
    euler_circuit_json = json.dumps({
        key: [list(edge) for edge in path]  # convert tuples to lists
        for key, path in euler_circuits.items()
    })

    output_dir = os.path.join(BASE_DIR, "static", "videos", "euler_circuits", "videos", "generate_animation", "1080p60")
    partials_dir = os.path.join(output_dir, "partial_movie_files", "EulerCircuitAnimator")

    os.makedirs(output_dir, exist_ok=True)

    for file in glob.glob(os.path.join(output_dir, "EulerCircuitAnimator*.mp4")):
        os.remove(file)

    if os.path.exists(partials_dir):
        shutil.rmtree(partials_dir)
        os.makedirs(partials_dir)

    result = build_euler_graph(euler_graph_json, euler_circuit_json)
    generate_euler_circuit_image(result)
    try:
        subprocess.run(result["command"], check=True, env=result["env"])
    except subprocess.CalledProcessError as e:
        print(f"Error running Manim: {e}")
        return f"Manim failed: {e}", 500


    return jsonify({
        "message": "Rendered",
        "euler_circuit": string_euler_format
    })


def generate_euler_circuit_image(result):
    svg_output_dir = os.path.join(
        BASE_DIR, "static", "videos", "euler_circuits", "images", "generate_animation"
    )
    os.makedirs(svg_output_dir, exist_ok=True)

    # Now, ensure Manim creates the PNG still frame correctly 
      
    png_file_path = os.path.join(svg_output_dir, "euler_circuit.png")  # Define the PNG path
    

    # Update Manim command to output PNG still frame
    svg_command = [
        "manim",
        "-s",  # Still frame
        "--format=png",  # Format as PNG
        "--media_dir", os.path.join(BASE_DIR, "static", "videos", "euler_circuits"),
        "--output_file", png_file_path,  # Ensure Manim outputs to the correct file
        os.path.join(BASE_DIR, "manim_engine", "generate_animation.py"),
        "EulerCircuitAnimator"
    ]

    try:
        subprocess.run(svg_command, check=True, env=result["env"])
        print(f"PNG generated and saved to: {png_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PNG: {e}")
        return f"Manim failed to generate PNG: {e}", 500



@app.route('/euler_animation')
def euler_animation():
    if os.path.exists(EULER_VIDEO_PATH):
        return send_file(EULER_VIDEO_PATH, mimetype='video/mp4')
    else:
        return "No video found", 404

@app.route('/euler_image')
def euler_image():
    if os.path.exists(EULER_IMAGE_PATH):
        return send_file(EULER_IMAGE_PATH, mimetype='image/png')

    else:
        return "No image found", 404






