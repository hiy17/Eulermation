from flask import Flask, jsonify, request, send_file, render_template, send_from_directory
import subprocess
import os
import shutil
import glob
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.manim_engine.graph_utils import EulerianGraphGenerator
import json
import networkx as nx

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
EULER_VIDEO_PATH = os.path.join(BASE_DIR, "static", "videos", "euler_graphs", "videos", "generate_animation", "1080p60", "AnimatedEulerianGraph.mp4")


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/popup')
def popup():
    return render_template('popup.html')

@app.route('/max')
def max_page():
    return render_template('max.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')






def setup_euler_artifacts(num_vertices):
    generator = EulerianGraphGenerator(num_vertices)
    
    # Unpack correctly
    euler_graph, (euler_circuits, success) = generator.generate_eulerian_graph()

    if euler_graph is None or not success:
        return

    return euler_graph, euler_circuits


def build_euler_graph(eulerian_graph_json, euler_circuits):
    env = os.environ.copy()
    env["EULERIAN_GRAPH"] = eulerian_graph_json  # Serialized JSON graph

    store_euler_circuits(euler_circuits)  
    

    return {
        "command": [
            "manim",
            "-qh",
            "--media_dir", os.path.join(BASE_DIR, "static", "videos", "euler_graphs"),
            os.path.join(BASE_DIR, "manim_engine", "generate_animation.py"),
            "AnimatedEulerianGraph",  # ✅ Scene class name
        ],
        "env": env
    }



euler_circuits_cache = {}
def store_euler_circuits(euler_circuits):
    global euler_circuits_cache
    assert isinstance(euler_circuits, dict), f"Expected dict, got {type(euler_circuits)}"
    euler_circuits_cache = euler_circuits



@app.route('/access/euler_circuits')
def return_euler_circuits():
    formatted_circuits = []
    print(euler_circuits_cache)

    for label, circuit in euler_circuits_cache.items():  # Now valid
        if not circuit:
            continue

        path = ' → '.join([edge[0] for edge in circuit] + [circuit[-1][1]])
        formatted_circuits.append(path)

    print(f'Formatted Circuits: {formatted_circuits}')
    return jsonify(formatted_circuits)


@app.route('/render/eulerian_graph')
def render_euler_graph_animation():
    try:
        num_vertices = int(request.args.get("vertices", 6))
        if not (3 <= num_vertices <= 8):
            return "Invalid number of vertices", 400
    except ValueError:
        return "Invalid input", 400

    euler_graph, euler_circuits = setup_euler_artifacts(num_vertices)

    # if result is None:
    #     return "Failed to generate Eulerian graph", 500

    # euler_graph, euler_circuits = result  
    euler_graph_json = json.dumps(nx.node_link_data(euler_graph))  # ✅ Serialize the graph

    output_dir = os.path.join(BASE_DIR, "static", "videos", "euler_graphs", "videos", "generate_animation", "1080p60")
    partials_dir = os.path.join(output_dir, "partial_movie_files", "AnimatedEulerianGraph")

    os.makedirs(output_dir, exist_ok=True)

    for file in glob.glob(os.path.join(output_dir, "AnimatedEulerianGraph*.mp4")):
        os.remove(file)

    if os.path.exists(partials_dir):
        shutil.rmtree(partials_dir)
        os.makedirs(partials_dir)

    result = build_euler_graph(euler_graph_json, euler_circuits)
    try:
        subprocess.run(result["command"], check=True, env=result["env"])
    except subprocess.CalledProcessError as e:
        print(f"Error running Manim: {e}")
        return f"Manim failed: {e}", 500

    # return_euler_circuits(euler_circuits)
    return "Rendered", 200

@app.route('/euler_animation')
def euler_animation():
    if os.path.exists(EULER_VIDEO_PATH):
        return send_file(EULER_VIDEO_PATH, mimetype='video/mp4')
    else:
        return "No video found", 404




if __name__ == "__main__":
    app.run(port=5000, debug=True)
















# def build_euler_graph(num_vertices):
#     env = os.environ.copy()
#     env["NUM_VERTICES"] = str(num_vertices)
#     return {
#         "command": [
#             "manim",
#             "-qh",
#             "--media_dir", os.path.join(BASE_DIR, "static", "videos", "euler_graphs"),
#             os.path.join(BASE_DIR, "manim_engine", "generate_animation.py"),
#             "AnimatedEulerianGraph",
#         ],
#         "env": env
#     }


# @app.route('/render/eulerian_graph')
# def render_animation():
#     try:
#         num_vertices = int(request.args.get("vertices", 6))
#         if not (3 <= num_vertices <= 8):
#             return "Invalid number of vertices", 400
#     except ValueError:
#         return "Invalid input", 400

#     euler_graph = setup_euler_artifacts(num_vertices)

#     output_dir = os.path.join(BASE_DIR, "static", "videos", "euler_graphs", "videos", "generate_animation", "1080p60")
#     partials_dir = os.path.join(output_dir, "partial_movie_files", "AnimatedEulerianGraph")

#     os.makedirs(output_dir, exist_ok=True)

#     # Clean old videos
#     for file in glob.glob(os.path.join(output_dir, "AnimatedEulerianGraph*.mp4")):
#         os.remove(file)

#     if os.path.exists(partials_dir):
#         shutil.rmtree(partials_dir)
#         os.makedirs(partials_dir)

#     result = build_euler_graph(euler_graph)
#     try:
#         subprocess.run(result["command"], check=True, env=result["env"])
#     except subprocess.CalledProcessError as e:
#         print(f"Error running Manim: {e}")
#         return f"Manim failed: {e}", 500

#     return "Rendered", 200