
from manim import *
import networkx as nx
import random
import string

class EulerianGraphGenerator:
    def __init__(self, num_vertices=4, max_attempts=100):
        self.num_vertices = num_vertices
        self.max_attempts = max_attempts
        self.eulerian_graph = None
        self.valid_degrees = [2, 4, 6]

    def generate_valid_degree_sequence(self):
        for _ in range(self.max_attempts):
            degree_sequence = [random.choice(self.valid_degrees) for _ in range(self.num_vertices)]
            if sum(degree_sequence) % 2 == 0 and nx.is_valid_degree_sequence_erdos_gallai(degree_sequence):
                return degree_sequence
        raise ValueError("Failed to find a valid degree sequence.")

    def generate_eulerian_graph(self):
        for attempt in range(1, self.max_attempts + 1):
            try:
                degree_sequence = self.generate_valid_degree_sequence()
                G = nx.expected_degree_graph(degree_sequence, selfloops=False)
                G = nx.Graph(G)  # Remove multiedges (if any)
                G.remove_edges_from(nx.selfloop_edges(G))  # Just in case

                if not nx.is_connected(G):
                    continue
                if not nx.is_eulerian(G):
                    continue

                # Relabel to A, B, C... after validation
                mapping = {n: chr(65 + i) for i, n in enumerate(G.nodes)}
                G = nx.relabel_nodes(G, mapping)

                self.eulerian_graph = G
                print(f"Graph generated at attempt no. {attempt}")
                print("Creating euler circuits....")
                euler_circuits, status = self.generate_euler_circuits(1)

                if status:
                    return G, euler_circuits

            except Exception as e:
                continue

        raise Exception("Failed to generate a valid Eulerian graph after max attempts.")
    
    # def generate_euler_circuits(self, num_circuits=1):
    #     status = True
    #     if self.eulerian_graph is None:
    #         print("No Eulerian graph generated.")
    #         status = False
    #         return {}, status

    #     circuits = {}
    #     for i in range(num_circuits):
    #         circuit = list(nx.eulerian_circuit(self.eulerian_graph))
    #         # Store each circuit in the dictionary with a unique key
    #         circuits[f"Circuit {i + 1}"] = circuit

    #     return circuits, status

    def generate_euler_circuits(self, num_circuits=1):
        status = True
        if self.eulerian_graph is None:
            print("No Eulerian graph generated.")
            status = False
            return {}, status

        circuits = {}
        nodes = list(self.eulerian_graph.nodes)
        for i in range(num_circuits):
            start_node = random.choice(nodes)
            circuit = list(nx.eulerian_circuit(self.eulerian_graph, source=start_node))
            circuits[f"Circuit {i + 1}"] = circuit

        return circuits, status


# class EulerCircuitAnimator(EulerianGraphGenerator, Scene):
#     def __init__(
#         self,
#         speed=0.5,
#         background_color=GREY,
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
#         EulerianGraphGenerator.__init__(self, **kwargs)
#         Scene.__init__(self, **kwargs)
#         # self.num_vertices = int(os.getenv("NUM_VERTICES", "4"))
#         # self.eulerian_graph = None
#         # self.euler_circuits = None

#     def construct(self):
#         # Manim frame setup
#         config.pixel_width = 1200
#         config.pixel_height = 1200
#         config.frame_width = 10
#         config.frame_height = 10

#         num_vertices = 5  # for example
#         generator = EulerianGraphGenerator(num_vertices)
#         graph, circuit_generated = generator.generate_eulerian_graph()

#         self.eulerian_graph = graph
#         self.euler_circuits = circuit_generated

    
#         if self.eulerian_graph is None or self.euler_circuits is None:
#             print("No Eulerian graph or circuits found!")
#             return

#         G_nx = self.eulerian_graph
#         circuit = self.euler_circuits

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

#         self.wait(2)
















# num_vertices = 5  # for example
# generator = EulerianGraphGenerator(num_vertices)








    # def display_euler_circuits(self, num_circuits=1):
    #     circuits = self.generate_euler_circuits(num_circuits)

    #     if not circuits:
    #         print("No Euler circuits generated.")
    #         return

    #     # Display the circuits as key-value pairs (Circuit -> list of edges)
    #     for circuit_name, circuit in circuits.items():
    #         print(f"\n{circuit_name}:")
    #         for edge in circuit:
    #             print(f"{edge[0]} -> {edge[1]}")



# # Example Usage
# euler_graph_gen = EulerianGraphGenerator()
# # euler_graph_gen.generate_eulerian_graph()
# euler_graph_gen.display_euler_circuits(num_circuits=1)



# # from manim import *
# # from networkx import *
# # import networkx as nx
# # import random
# # from itertools import product

# # class EulerianGraphGenerator:
# #     def __init__(self, num_vertices=6, max_attempts=100):
# #         """
# #         Initialize the graph generator.
        
# #         Parameters:
# #         - num_vertices (int): Number of vertices for the graph.
# #         - max_attempts (int): Maximum number of attempts for generating a valid Eulerian graph.
# #         """
# #         self.num_vertices = num_vertices
# #         self.max_attempts = max_attempts
# #         self.current_eulerian_graph = None

# #     def generate_valid_degrees(self):
# #         """Generate valid degree combinations for the graph."""
# #         valid_degrees = [2, 4, 6]
# #         all_combinations = list(product(valid_degrees, repeat=self.num_vertices))
# #         return [combo for combo in all_combinations if sum(combo) % 2 == 0]

# #     def assign_valid_vertex_degrees(self):
# #         """Assign valid degrees to each vertex."""
# #         valid_combinations = self.generate_valid_degrees()
# #         random.shuffle(valid_combinations)
        
# #         for combo in valid_combinations:
# #             if is_valid_degree_sequence_erdos_gallai(combo):
# #                 return {chr(65 + i): combo[i] for i in range(self.num_vertices)}
        
# #         raise ValueError("No valid degree sequence found that is graphical.")

# #     def generate_eulerian_graph(self):
# #         """Generate an Eulerian graph with the assigned degrees."""
# #         attempt = 0
# #         while attempt < self.max_attempts:
# #             try:
# #                 vertex_degrees = self.assign_valid_vertex_degrees()
# #                 degree_sequence = list(vertex_degrees.values())

# #                 # Use configuration model to generate a graph from degree sequence
# #                 temp_graph = nx.configuration_model(degree_sequence)
# #                 G = nx.Graph(temp_graph)  # Remove parallel edges
# #                 G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops

# #                 # Relabel nodes to match A, B, C...
# #                 mapping = {n: chr(65 + i) for i, n in enumerate(G.nodes)}
# #                 G = nx.relabel_nodes(G, mapping)

# #                 # Ensure graph has correct vertex set (may be incomplete after removals)
# #                 if set(G.nodes) != set(vertex_degrees.keys()):
# #                     raise Exception("Graph does not have correct vertex labels.")

# #                 # Check for connectivity and Eulerian property
# #                 if not nx.is_connected(G):
# #                     raise Exception("Generated graph is not connected.")
# #                 if not nx.is_eulerian(G):
# #                     raise Exception("Generated graph is not Eulerian.")

# #                 # If graph is valid, store it and return
# #                 self.current_eulerian_graph = G
# #                 print("Graph generated at attemp no. : ", attempt+1)
# #                 return G

# #             except Exception as e:
# #                 print(f"Invalid graph generation count: {attempt + 1}: {e}")
# #                 attempt += 1

# #         # If we exceed max attempts, raise an error
# #         raise Exception(f"Failed to generate a valid Eulerian graph after {self.max_attempts} attempts.")

# #     def generate_euler_circuits(self, num_circuits=5):
# #         """Generate Euler circuits from the Eulerian graph."""
# #         if self.current_eulerian_graph is None:
# #             print("No Eulerian graph generated.")
# #             return []

# #         circuits = []
# #         for _ in range(num_circuits):
# #             circuit = list(nx.eulerian_circuit(self.current_eulerian_graph))
# #             circuits.append(circuit)
# #         return circuits


# from manim import *
# import networkx as nx
# import random

# class EulerianGraphGenerator:
#     def __init__(self, num_vertices=6, max_attempts=100):
#         self.num_vertices = num_vertices
#         self.max_attempts = max_attempts
#         self.current_eulerian_graph = None
#         self.valid_degrees = [2, 4, 6]

#     def generate_valid_degree_sequence(self):
#         for _ in range(self.max_attempts):
#             degree_sequence = [random.choice(self.valid_degrees) for _ in range(self.num_vertices)]
#             if sum(degree_sequence) % 2 == 0 and nx.is_valid_degree_sequence_erdos_gallai(degree_sequence):
#                 return degree_sequence
#         raise ValueError("Failed to find a valid degree sequence.")

#     def generate_eulerian_graph(self):
#         for attempt in range(1, self.max_attempts + 1):
#             try:
#                 degree_sequence = self.generate_valid_degree_sequence()
#                 G = nx.expected_degree_graph(degree_sequence, selfloops=False)
#                 G = nx.Graph(G)  # Remove multiedges (if any)
#                 G.remove_edges_from(nx.selfloop_edges(G))  # Just in case

#                 if not nx.is_connected(G):
#                     continue
#                 if not nx.is_eulerian(G):
#                     continue

#                 # Relabel to A, B, C... after validation
#                 mapping = {n: chr(65 + i) for i, n in enumerate(G.nodes)}
#                 G = nx.relabel_nodes(G, mapping)

#                 self.current_eulerian_graph = G
#                 print(f"Graph generated at attempt no. {attempt}")
#                 return G

#             except Exception as e:
#                 continue

#         raise Exception("Failed to generate a valid Eulerian graph after max attempts.")

#     def generate_euler_circuits(self, num_circuits=5):
#         if self.current_eulerian_graph is None:
#             print("No Eulerian graph generated.")
#             return []

#         circuits = []
#         for _ in range(num_circuits):
#             circuit = list(nx.eulerian_circuit(self.current_eulerian_graph))
#             circuits.append(circuit)
#         return circuits

