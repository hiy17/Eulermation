from manim import *
from networkx import *
import networkx as nx
import random
from itertools import product

class EulerianGraphGenerator:
    def __init__(self, num_vertices=6, max_attempts=100):
        """
        Initialize the graph generator.
        
        Parameters:
        - num_vertices (int): Number of vertices for the graph.
        - max_attempts (int): Maximum number of attempts for generating a valid Eulerian graph.
        """
        self.num_vertices = num_vertices
        self.max_attempts = max_attempts
        self.current_eulerian_graph = None

    def generate_valid_degrees(self):
        """Generate valid degree combinations for the graph."""
        valid_degrees = [2, 4, 6]
        all_combinations = list(product(valid_degrees, repeat=self.num_vertices))
        return [combo for combo in all_combinations if sum(combo) % 2 == 0]

    def assign_valid_vertex_degrees(self):
        """Assign valid degrees to each vertex."""
        valid_combinations = self.generate_valid_degrees()
        random.shuffle(valid_combinations)
        
        for combo in valid_combinations:
            if is_valid_degree_sequence_erdos_gallai(combo):
                return {chr(65 + i): combo[i] for i in range(self.num_vertices)}
        
        raise ValueError("No valid degree sequence found that is graphical.")

    def generate_eulerian_graph(self):
        """Generate an Eulerian graph with the assigned degrees."""
        attempt = 0
        while attempt < self.max_attempts:
            try:
                vertex_degrees = self.assign_valid_vertex_degrees()
                degree_sequence = list(vertex_degrees.values())

                # Use configuration model to generate a graph from degree sequence
                temp_graph = nx.configuration_model(degree_sequence)
                G = nx.Graph(temp_graph)  # Remove parallel edges
                G.remove_edges_from(nx.selfloop_edges(G))  # Remove self-loops

                # Relabel nodes to match A, B, C...
                mapping = {n: chr(65 + i) for i, n in enumerate(G.nodes)}
                G = nx.relabel_nodes(G, mapping)

                # Ensure graph has correct vertex set (may be incomplete after removals)
                if set(G.nodes) != set(vertex_degrees.keys()):
                    raise Exception("Graph does not have correct vertex labels.")

                # Check for connectivity and Eulerian property
                if not nx.is_connected(G):
                    raise Exception("Generated graph is not connected.")
                if not nx.is_eulerian(G):
                    raise Exception("Generated graph is not Eulerian.")

                # If graph is valid, store it and return
                self.current_eulerian_graph = G
                print("Graph generated at attemp no. : ", attempt+1)
                return G

            except Exception as e:
                print(f"Invalid graph generation count: {attempt + 1}: {e}")
                attempt += 1

        # If we exceed max attempts, raise an error
        raise Exception(f"Failed to generate a valid Eulerian graph after {self.max_attempts} attempts.")

    def generate_euler_circuits(self, num_circuits=5):
        """Generate Euler circuits from the Eulerian graph."""
        if self.current_eulerian_graph is None:
            print("No Eulerian graph generated.")
            return []

        circuits = []
        for _ in range(num_circuits):
            circuit = list(nx.eulerian_circuit(self.current_eulerian_graph))
            circuits.append(circuit)
        return circuits

