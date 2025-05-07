# import os
# import sys
# import json
# import string
# import random
# import networkx as nx
# from manim import *

# class AnimatedEulerianGraph(Scene):
#     def __init__(
#         self,
#         speed=0.5,
#         background_color=WHITE,
#         vertex_color=YELLOW_C,
#         edge_color=GREEN_A,
#         label_color=BLACK,
#         layout_scale=3,
#         **kwargs
#     ):
#         super().__init__(**kwargs)
#         self.speed = speed
#         self.background_color = background_color
#         self.vertex_color = vertex_color
#         self.edge_color = edge_color
#         self.label_color = label_color
#         self.layout_scale = layout_scale

#         # Read and deserialize the Eulerian graph from environment
#         raw_graph = os.getenv("EULERIAN_GRAPH")
#         if raw_graph is None:
#             raise ValueError("EULERIAN_GRAPH environment variable is not set.")

#         try:
#             graph_data = json.loads(raw_graph)
#             self.eulerian_graph = nx.node_link_graph(graph_data)
#         except Exception as e:
#             raise ValueError(f"Failed to parse EULERIAN_GRAPH: {e}")

#     def construct(self):
#         config.pixel_width = 1300
#         config.pixel_height = 1200
#         config.frame_width = 10
#         config.frame_height = 9

#         G_nx = self.eulerian_graph
#         if G_nx is None or len(G_nx.nodes) == 0:
#             return

#         # Generate Eulerian circuit(s) to use in logic if needed
#         try:
#             self.euler_circuits = list(nx.eulerian_circuit(G_nx))
#         except:
#             self.euler_circuits = []

#         print(f"Eulerian Graph: {G_nx}")
#         print(f"Euler Circuits: {self.euler_circuits}")

#         vertices = list(G_nx.nodes)
#         edges = list(G_nx.edges)
#         layout = nx.circular_layout(G_nx)
#         positions = {v: layout[v] * self.layout_scale for v in vertices}
#         manim_positions = {v: [pos[0], pos[1], 0] for v, pos in positions.items()}

#         name_map = {v: string.ascii_uppercase[i] for i, v in enumerate(vertices)}

#         vertex_mobjects = {
#             v: Dot(point=manim_positions[v], radius=0.3, color=self.vertex_color).set_z_index(2)
#             for v in vertices
#         }

#         labels = {
#             v: Text(name_map[v], color=self.label_color).scale(0.5).move_to(manim_positions[v]).set_z_index(3)
#             for v in vertices
#         }

#         edge_objects = {}
#         for u, v in edges:
#             line = Line(manim_positions[u], manim_positions[v], color=self.edge_color)
#             edge_objects[(u, v)] = line
#             edge_objects[(v, u)] = line  # Bidirectional

#         self.camera.background_color = self.background_color

#         shown_vertices = set()
#         shown_edges = set()

#         def explore(v):
#             if v not in shown_vertices:
#                 self.play(Create(vertex_mobjects[v]), run_time=self.speed)
#                 self.add(labels[v])
#                 shown_vertices.add(v)
#                 self.wait(self.speed * 0.2)

#             neighbors = list(G_nx.neighbors(v))
#             random.shuffle(neighbors)

#             for neighbor in neighbors:
#                 if neighbor not in shown_vertices or (v, neighbor) not in shown_edges:
#                     start = vertex_mobjects[v].get_center()
#                     edge = edge_objects[(v, neighbor)]

#                     self.play(GrowFromPoint(edge, point=start), run_time=self.speed * 0.8)
#                     self.add(edge, vertex_mobjects[v], labels[v], vertex_mobjects[neighbor], labels[neighbor])

#                     shown_edges.add((v, neighbor))
#                     shown_edges.add((neighbor, v))
#                     self.wait(self.speed * 0.2)

#                     if neighbor not in shown_vertices:
#                         explore(neighbor)

#         # Start from the vertex labeled 'A'
#         start = next(v for v in vertices if name_map[v] == "A")

#         graph_group = VGroup(
#             *vertex_mobjects.values(),
#             *labels.values(),
#             *set(edge_objects.values())
#         )
#         graph_group.move_to(ORIGIN)
#         graph_group.scale_to_fit_height(config.frame_height * 0.8)

#         explore(start)

#         self.wait()

import os
import json
import networkx as nx
from networkx.readwrite import json_graph

from manim import *
import networkx as nx
import random
import sys
import os
import string
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# from app.manim_engine.graph_utils import EulerianGraphGenerator

# class EulerCircuitAnimator(Scene):
#     def __init__(
#         self,
#         speed=0.5,
#         background_color=WHITE,
#         vertex_color=GREEN,
#         edge_color=GREEN_A,
#         trail_color=RED,
#         label_color=BLACK,
#         layout_scale=2,
#         **kwargs
#     ):
#         super().__init__(**kwargs)
#         self.speed = speed
#         self.background_color = background_color
#         self.vertex_color = vertex_color
#         self.edge_color = edge_color
#         self.trail_color = trail_color
#         self.label_color = label_color
#         self.layout_scale = layout_scale
#         self.num_vertices = int(os.getenv("NUM_VERTICES", "4"))
#         self.eulerian_graph = None
#         self.euler_circuits = None

#     def construct(self):
#         config.pixel_width = 1200
#         config.pixel_height = 1200
#         config.frame_width = 10
#         config.frame_height = 10

#         # ✅ Deserialize graph from ENV
#         graph_json = os.getenv("EULERIAN_GRAPH")
#         if not graph_json:
#             print("No graph found in environment!")
#             return

#         data = json.loads(graph_json)
#         G_nx = json_graph.node_link_graph(data)

#         if not nx.is_eulerian(G_nx):
#             print("Provided graph is not Eulerian.")
#             return

#         self.eulerian_graph = G_nx
#         self.euler_circuits = list(nx.eulerian_circuit(G_nx))

#         if not self.eulerian_graph or not self.euler_circuits:
#             print("No Eulerian graph or circuits found!")
#             return
        
#         print(f"Circuit: {self.euler_circuits}")
#         print("Generating graph...")

#         circuit = list(nx.eulerian_circuit(G_nx))
#         vertices = list(G_nx.nodes)
#         layout = nx.circular_layout(G_nx)
#         positions = {v: layout[v] * self.layout_scale for v in vertices}
#         manim_positions = {v: [pos[0], pos[1], 0] for v, pos in positions.items()}
#         name_map = {v: string.ascii_uppercase[i] for i, v in enumerate(vertices)}

#         # Vertices
#         vertex_mobjects = {
#             v: Dot(point=manim_positions[v], radius=0.3, color=self.vertex_color).set_z_index(2)
#             for v in vertices
#         }

#         # Labels
#         labels = {
#             v: Text(name_map[v], color=self.label_color).scale(0.5).move_to(manim_positions[v]).set_z_index(3)
#             for v in vertices
#         }

#         # Edges (initially green)
#         edge_objects = {}
#         for u, v in G_nx.edges:
#             line = Line(manim_positions[u], manim_positions[v], color=self.edge_color).set_z_index(1)
#             edge_objects[(u, v)] = line
#             edge_objects[(v, u)] = line

#         self.camera.background_color = self.background_color

#         # Display graph
#         self.play(*[Create(dot) for dot in vertex_mobjects.values()], run_time=self.speed)
#         self.play(*[Write(label) for label in labels.values()], run_time=self.speed)
#         self.play(*[Create(line) for line in set(edge_objects.values())], run_time=self.speed)

#         self.wait(self.speed)

#         # Add Euler circuit text below graph
#         circuit_names = [name_map[u] for u, _ in circuit] + [name_map[circuit[0][0]]]  # include full cycle
#         circuit_str = " → ".join(circuit_names)
#         circuit_text = Text(f"Euler Circuit: {circuit_str}", font_size=24, color=WHITE)
#         circuit_text.next_to(ORIGIN, DOWN * 3)  # slightly below the graph
#         self.play(FadeIn(circuit_text))

#         # Animate the Euler circuit step by step
#         for u, v in circuit:
#             start = manim_positions[u]
#             end = manim_positions[v]

#             # Animation: red edge grows from u to v
#             trail = Line(start, end, color=self.trail_color, stroke_width=6).set_z_index(2)
#             self.play(GrowFromPoint(trail, point=start), run_time=self.speed)
#             self.add(trail)

#             self.wait(self.speed * 0.2)

#         self.wait(.5)
#         return self.euler_circuits


class EulerCircuitAnimator(Scene):
    def __init__(
        self,
        speed=.5,
        background_color=GREY,
        vertex_color=GREEN,
        edge_color=GREEN_A,
        trail_color=RED,
        label_color=BLACK,
        layout_scale=2,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.speed = speed
        self.background_color = background_color
        self.vertex_color = vertex_color
        self.edge_color = edge_color
        self.trail_color = trail_color
        self.label_color = label_color
        self.layout_scale = layout_scale
        self.num_vertices = int(os.getenv("NUM_VERTICES", "4"))
        self.eulerian_graph = None
        self.euler_circuits = None

    def construct(self):
        config.pixel_width = 1200
        config.pixel_height = 1200
        config.frame_width = 10
        config.frame_height = 10

        # Load graph
        graph_json = os.getenv("EULERIAN_GRAPH")
        circuit_json = os.getenv("EULERIAN_CIRCUIT")

        if not graph_json or not circuit_json:
            print("Missing graph or circuit data!")
            return

        G_nx = json_graph.node_link_graph(json.loads(graph_json))
        circuit_data = json.loads(circuit_json)

        # For now just use the first circuit
        if not circuit_data:
            print("No circuits available!")
            return

        circuit = list(circuit_data.values())[0]

        self.eulerian_graph = G_nx
        self.euler_circuits = circuit
        
        print(f"Circuit: {self.euler_circuits}")
        print("Generating graph...")

        
        vertices = list(G_nx.nodes)
        layout = nx.circular_layout(G_nx)
        positions = {v: layout[v] * self.layout_scale for v in vertices}
        manim_positions = {v: [pos[0], pos[1], 0] for v, pos in positions.items()}
        name_map = {v: string.ascii_uppercase[i] for i, v in enumerate(vertices)}

        # Vertices
        vertex_mobjects = {
            v: Dot(point=manim_positions[v], radius=0.3, color=self.vertex_color).set_z_index(2)
            for v in vertices
        }

        # Labels
        labels = {
            v: Text(name_map[v], color=self.label_color).scale(0.5).move_to(manim_positions[v]).set_z_index(3)
            for v in vertices
        }

        # Edges (initially green)
        edge_objects = {}
        for u, v in G_nx.edges:
            line = Line(manim_positions[u], manim_positions[v], color=self.edge_color).set_z_index(1)
            edge_objects[(u, v)] = line
            edge_objects[(v, u)] = line

        self.camera.background_color = self.background_color

        # Display graph
        self.play(*[Create(dot) for dot in vertex_mobjects.values()], run_time=self.speed)
        self.play(*[Write(label) for label in labels.values()], run_time=self.speed)
        self.play(*[Create(line) for line in set(edge_objects.values())], run_time=self.speed)

        self.wait(self.speed)

        # Add Euler circuit text below graph
        circuit_names = [name_map[u] for u, _ in circuit] + [name_map[circuit[0][0]]]  # include full cycle
        circuit_str = " → ".join(circuit_names)
        circuit_text = Text(f"Euler Circuit: {circuit_str}", font_size=24, color=WHITE)
        circuit_text.next_to(ORIGIN, DOWN * 3)  # slightly below the graph
        self.play(FadeIn(circuit_text))

        # Animate the Euler circuit step by step
        for u, v in circuit:
            start = manim_positions[u]
            end = manim_positions[v]

            # Animation: red edge grows from u to v
            trail = Line(start, end, color=self.trail_color, stroke_width=6).set_z_index(2)
            self.play(GrowFromPoint(trail, point=start), run_time=self.speed)
            self.add(trail)

            self.wait(self.speed * 0.2)

        self.wait(.5)
        return self.euler_circuits


























# class AnimatedEulerianGraph(Scene):

#     def __init__(
#         self,
#         speed=0.5,
#         background_color=DARK_GREY,
#         vertex_color=GREEN,
#         edge_color=GREEN_A,
#         label_color=BLACK,
#         layout_scale=2,  
#         **kwargs
#     ):
#         super().__init__(**kwargs)
#         self.speed = speed
#         self.background_color = background_color
#         self.vertex_color = vertex_color
#         self.edge_color = edge_color
#         self.label_color = label_color
#         self.layout_scale = layout_scale  # Store it
#         self.num_vertices = int(os.getenv("NUM_VERTICES", "6"))


#     def construct(self):
#         # Set the resolution to match your HTML video size
#         config.pixel_width = 1200
#         config.pixel_height = 1200

#         # Maintain the same aspect ratio (500 / 400 = 1.25)
#         config.frame_width = 10    # Logical width in scene units
#         config.frame_height = 10    # Logical height in scene units

#         print(f"[DEBUG] Resolution: {config.pixel_width}x{config.pixel_height}")
        
        
#         generator = EulerianGraphGenerator(num_vertices=self.num_vertices)
#         G_nx = generator.generate_eulerian_graph()
#         if G_nx is None:
#             return

#         vertices = list(G_nx.nodes)
#         edges = list(G_nx.edges)
#         layout = nx.circular_layout(G_nx)
#         # positions = {v: layout[v] *4  or v in vertices}
#         positions = {v: layout[v] * self.layout_scale for v in vertices}

#         manim_positions = {v: [pos[0], pos[1], 0] for v, pos in positions.items()}

#         # Assign letter labels (A, B, ...)
#         name_map = {v: string.ascii_uppercase[i] for i, v in enumerate(vertices)}

#         vertex_mobjects = {
#             v: Dot(point=manim_positions[v], radius=0.3, color=self.vertex_color).set_z_index(2)
#             for v in vertices
#         }

#         labels = {
#             v: Text(name_map[v], color=self.label_color).scale(0.5).move_to(manim_positions[v]).set_z_index(3)
#             for v in vertices
#         }

#         edge_objects = {}
#         for u, v in edges:
#             line = Line(manim_positions[u], manim_positions[v], color=self.edge_color)
#             edge_objects[(u, v)] = line
#             edge_objects[(v, u)] = line  # Bidirectional

#         self.camera.background_color = self.background_color

#         shown_vertices = set()
#         shown_edges = set()

#         def explore(v):
#             if v not in shown_vertices:
#                 self.play(Create(vertex_mobjects[v]), run_time=self.speed)
#                 self.add(labels[v])
#                 shown_vertices.add(v)
#                 self.wait(self.speed * 0.2)

#             neighbors = list(G_nx.neighbors(v))
#             random.shuffle(neighbors)

#             for neighbor in neighbors:
#                 if neighbor not in shown_vertices or (v, neighbor) not in shown_edges:
#                     start = vertex_mobjects[v].get_center()
#                     edge = edge_objects[(v, neighbor)]

#                     self.play(GrowFromPoint(edge, point=start), run_time=self.speed * 0.8)
#                     self.add(edge, vertex_mobjects[v], labels[v], vertex_mobjects[neighbor], labels[neighbor])

#                     shown_edges.add((v, neighbor))
#                     shown_edges.add((neighbor, v))
#                     self.wait(self.speed * 0.2)

#                     if neighbor not in shown_vertices:
#                         explore(neighbor)

#         # Start from the vertex labeled 'A'
#         start = next(v for v in vertices if name_map[v] == "A")

#         # Group everything for scaling and centering
#         graph_group = VGroup(
#             *vertex_mobjects.values(),
#             *labels.values(),
#             *set(edge_objects.values())  # Convert to set to avoid duplicates
#         )
#         graph_group.move_to(ORIGIN)
#         graph_group.scale_to_fit_height(config.frame_height * 0.8)  # Or scale_to_fit_width
        

#         # Start the animation
#         explore(start)
#         print(f"Frame width: {config.frame_width}, Frame height: {config.frame_height}")

#         self.wait()




