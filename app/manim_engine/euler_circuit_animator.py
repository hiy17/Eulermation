import os
import json
import sys
from networkx.readwrite import json_graph
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from app.manim_engine.graph_utils import EulerianGraphGenerator

# Generate graph and circuit
generator = EulerianGraphGenerator(num_vertices=6)
graph, circuits = generator.generate_eulerian_graph()

# Convert to JSON strings
graph_json = json.dumps(json_graph.node_link_data(graph))
circuit_json = json.dumps(circuits)

# Set environment variables
os.environ["EULERIAN_GRAPH"] = graph_json
os.environ["EULERIAN_CIRCUIT"] = circuit_json
os.environ["NUM_VERTICES"] = "4"

# Launch Manim animation
os.system("manim -pqh app/manim_engine/generate_animation.py EulerCircuitAnimator")

