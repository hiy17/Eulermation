import random
import networkx as nx

class EulerianGraphGenerator:
    def __init__(self, num_vertices=6, max_attempts=100):
        self.num_vertices = num_vertices
        self.max_attempts = max_attempts
        self.current_eulerian_graph = None
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
                print(f"Graph generated at attempt no. {attempt}")
                return G

            except Exception as e:
                continue

        raise Exception("Failed to generate a valid Eulerian graph after max attempts.")

    def generate_euler_circuits(self, num_circuits=5):
        if self.current_eulerian_graph is None:
            print("No Eulerian graph generated.")
            return []

        circuits = []
        for _ in range(num_circuits):
            circuit = list(nx.eulerian_circuit(self.current_eulerian_graph))
            circuits.append(circuit)
        return circuits

    def display_euler_circuits(self, num_circuits=1):
        circuits = self.generate_euler_circuits(num_circuits)

        if not circuits:
            print("No Euler circuits generated.")
            return

        for i, circuit in enumerate(circuits):
            print(f"\nEuler Circuit {i + 1}:")
            for edge in circuit:
                print(f"{edge[0]} -> {edge[1]}")

# Example Usage
euler_graph_gen = EulerianGraphGenerator()
euler_graph_gen.generate_eulerian_graph()
euler_graph_gen.display_euler_circuits(num_circuits=3)
