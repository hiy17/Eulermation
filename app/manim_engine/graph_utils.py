
from manim import *
import networkx as nx
import random

class EulerianGraphGenerator:
    def __init__(self, num_vertices=4, max_attempts=100):
        self.num_vertices = num_vertices
        self.max_attempts = max_attempts
        self.current_eulerian_graph = None
        self.euler_cicuits = None
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

                self.current_eulerian_graph = G
                self.euler_cicuits = self.generate_euler_circuits(5)
                print(f"Graph generated at attempt no. {attempt}")
                print(f"Euler Circuits: {self.euler_cicuits}")

                # if status:
                return G, self.euler_cicuits

            except Exception as e:
                continue

        raise Exception("Failed to generate a valid Eulerian graph after max attempts.")
    
    def generate_euler_circuits(self, num_circuits=1):
        status = True
        if self.current_eulerian_graph is None:
            print("No Eulerian graph generated.")
            status = False
            return {}, status

        circuits = {}
        for i in range(num_circuits):
            circuit = list(nx.eulerian_circuit(self.current_eulerian_graph))
            # Store each circuit in the dictionary with a unique key
            circuits[f"Circuit {i + 1}"] = circuit

        return circuits, status

    # def generate_euler_circuits(self, num_circuits=5):
    #     status = True
    #     if self.current_eulerian_graph is None:
    #         print("No Eulerian graph generated.")
    #         status = False
    #         return [], status  # Return list for frontend compatibility

    #     unique_circuits = set()
    #     all_vertices = list(self.current_eulerian_graph.nodes)

    #     for vertex in all_vertices:
    #         for _ in range(num_circuits):
    #             try:
    #                 circuit = list(nx.eulerian_circuit(self.current_eulerian_graph, source=vertex))
    #                 circuit_tuple = tuple(circuit)
    #                 unique_circuits.add(circuit_tuple)
    #             except nx.NetworkXError:
    #                 continue

    #     if not unique_circuits:
    #         return ["Maximum generation attempted."], status

    #     # Convert to readable string paths (like "0-1-2-0")
    #     circuit_paths = []
    #     for i, circuit in enumerate(unique_circuits):
    #         if i >= num_circuits:
    #             break
    #         nodes = [str(circuit[0][0])] + [str(edge[1]) for edge in circuit]
    #         path_str = "-".join(nodes)
    #         circuit_paths.append(path_str)

    #     return circuit_paths, status

    
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

