from flask import Flask, request, send_file, render_template, send_from_directory
import subprocess
import os
import shutil
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

print(BASE_DIR)
print(TEMPLATE_DIR)
print(STATIC_DIR)

EULER_VIDEO_PATH = os.path.join(BASE_DIR, "static", "videos", "euler_graphs", "videos", "generate_animation", "1080p60", "AnimatedEulerianGraph.mp4")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


# @app.route('/')
# def home():
#     return render_template_string('''
#     <html>
#     <body>
#         <h1>Manim On-Demand</h1>

#         <label for="vertices">Number of Vertices (3–8):</label>
#         <input type="number" id="vertices" name="vertices" min="3" max="8" value="3">
#         <button onclick="generateAnimation()">Generate Animation</button>

#         <br><br>
#         <video id="video" width="400" height="400" controls autoplay loop>
#             <source id="videoSource" src="" type="video/mp4">
#             Your browser does not support the video tag.
#         </video>

#         <script>
#             function generateAnimation() {
#                 const numVertices = document.getElementById('vertices').value;
#                 fetch('/render/eulerian_graph?vertices=' + numVertices)
#                     .then(response => {
#                         if (response.ok) {
#                             console.log("Render complete, loading animation...");
#                             document.getElementById('videoSource').src = '/animation?' + new Date().getTime();
#                             document.getElementById('video').load();
#                         }
#                     });
#             }
#         </script>
#     </body>
#     </html>
#     ''')

@app.route('/')
def home():
    return render_template('index.html')  # <-- Use template file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')



def build_manim_command(num_vertices):
    env = os.environ.copy()
    env["NUM_VERTICES"] = str(num_vertices)
    return {
        "command": [
            "manim",
            "-qh",
            "--media_dir", os.path.join(BASE_DIR, "static", "videos", "euler_graphs"),
            os.path.join(BASE_DIR, "manim_engine", "generate_animation.py"),
            "AnimatedEulerianGraph",
        ],
        "env": env
    }

@app.route('/render/eulerian_graph')
def render_animation():
    try:
        num_vertices = int(request.args.get("vertices", 6))
        if not (3 <= num_vertices <= 8):
            return "Invalid number of vertices", 400
    except ValueError:
        return "Invalid input", 400

    output_dir = os.path.join(BASE_DIR, "static", "videos", "euler_graphs", "videos", "generate_animation", "1080p60")
    partials_dir = os.path.join(output_dir, "partial_movie_files", "AnimatedEulerianGraph")

    os.makedirs(output_dir, exist_ok=True)

    # Clean old videos
    for file in glob.glob(os.path.join(output_dir, "AnimatedEulerianGraph*.mp4")):
        os.remove(file)

    if os.path.exists(partials_dir):
        shutil.rmtree(partials_dir)
        os.makedirs(partials_dir)

    result = build_manim_command(num_vertices)
    try:
        subprocess.run(result["command"], check=True, env=result["env"])
    except subprocess.CalledProcessError as e:
        print(f"Error running Manim: {e}")
        return f"Manim failed: {e}", 500

    return "Rendered", 200

@app.route('/animation')
def animation():
    if os.path.exists(EULER_VIDEO_PATH):
        return send_file(EULER_VIDEO_PATH, mimetype='video/mp4')
    else:
        return "No video found", 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)



