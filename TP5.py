import heapq
import numpy as np

class GraphShortestPath:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.node_index_map = {node: idx for idx, node in enumerate(nodes)}
        self.graph = self.build_weighted_adj_matrix(edges)

    def build_weighted_adj_matrix(self, edges):
        size = len(self.nodes)
        matrix = np.full((size, size), float('inf'))
        np.fill_diagonal(matrix, 0)

        for start, end, weight in edges:
            i, j = self.node_index_map[start], self.node_index_map[end]
            matrix[i][j] = matrix[j][i] = weight

        return matrix

    def shortest_path(self, start_node, end_node):
        size = len(self.graph)
        distances = [float('inf')] * size
        previous_nodes = [None] * size
        priority_queue = []

        start_idx, end_idx = self.node_index_map[start_node], self.node_index_map[end_node]
        distances[start_idx] = 0
        heapq.heappush(priority_queue, (0, start_idx))

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == end_idx:
                break
            if current_distance > distances[current_node]:
                continue

            for neighbor_idx, weight in enumerate(self.graph[current_node]):
                if weight < float('inf'):
                    tentative_distance = current_distance + weight
                    if tentative_distance < distances[neighbor_idx]:
                        distances[neighbor_idx] = tentative_distance
                        previous_nodes[neighbor_idx] = current_node
                        heapq.heappush(priority_queue, (tentative_distance, neighbor_idx))

        path = []
        current = end_idx
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return [self.nodes[node] for node in path], distances[end_idx]

    def display_adj_matrix(self):
        print("Adjacency Matrix:")
        print("     " + " ".join(f"{node:>4}" for node in self.nodes))
        for i, row in enumerate(self.graph):
            row_str = " ".join(" inf" if val == float('inf') else f"{int(val):4d}" for val in row)
            print(f"{self.nodes[i]:>4} {row_str}")

if __name__ == "__main__":
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
    edges = [
        ('A', 'C', 1), ('A', 'B', 4), ('B', 'F', 3), ('C', 'D', 8), ('C', 'F', 7),
        ('D', 'H', 5), ('F', 'H', 1), ('F', 'E', 1), ('E', 'H', 2), ('H', 'G', 3),
        ('H', 'M', 7), ('H', 'L', 6), ('G', 'M', 4), ('M', 'L', 1), ('L', 'G', 4),
        ('L', 'E', 2)
    ]
    
    graph = GraphShortestPath(nodes, edges)
    graph.display_adj_matrix()
    
    try:
        start_node = input("\nEnter source node (A-M): ").strip().upper()
        end_node = input("Enter target node (A-M): ").strip().upper()

        if start_node not in graph.node_index_map or end_node not in graph.node_index_map:
            raise ValueError("Invalid node input")

        path, weight = graph.shortest_path(start_node, end_node)
        print(f"\nShortest path from {start_node} to {end_node}: {' -> '.join(path)}")
        print(f"Total path weight: {weight}")
    except ValueError as e:
        print(f"Error: {e}")
