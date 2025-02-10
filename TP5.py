import heapq
import numpy as np

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
node_index_map = {node: idx for idx, node in enumerate(nodes)}

edges = [
    ('A', 'C', 1), ('A', 'B', 4), ('B', 'F', 3), ('C', 'D', 8), ('C', 'F', 7),
    ('D', 'H', 5), ('F', 'H', 1), ('F', 'E', 1), ('E', 'H', 2), ('H', 'G', 3),
    ('H', 'M', 7), ('H', 'L', 6), ('G', 'M', 4), ('M', 'L', 1), ('L', 'G', 4),
    ('L', 'E', 2)
]

# Build adjacency matrix efficiently
def build_weighted_adj_matrix():
    size = len(nodes)
    matrix = np.full((size, size), float('inf'))
    np.fill_diagonal(matrix, 0)

    for start, end, weight in edges:
        i, j = node_index_map[start], node_index_map[end]
        matrix[i][j] = matrix[j][i] = weight

    return matrix

# Dijkstra's algorithm
def shortest_path(adj_matrix, start_node, end_node):
    size = len(adj_matrix)
    distances = [float('inf')] * size
    previous_nodes = [None] * size
    priority_queue = []

    start_idx, end_idx = node_index_map[start_node], node_index_map[end_node]
    distances[start_idx] = 0
    heapq.heappush(priority_queue, (0, start_idx))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end_idx:  # Exit early if the target is reached
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor_idx, weight in enumerate(adj_matrix[current_node]):
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

    return [nodes[node] for node in path], distances[end_idx]

# Display adjacency matrix
def display_adj_matrix(matrix):
    print("Adjacency Matrix:")
    print("     " + " ".join(f"{node:>4}" for node in nodes))
    for i, row in enumerate(matrix):
        row_str = " ".join(" inf" if val == float('inf') else f"{int(val):4d}" for val in row)
        print(f"{nodes[i]:>4} {row_str}")

# Main execution
if __name__ == "__main__":
    adj_matrix = build_weighted_adj_matrix()
    display_adj_matrix(adj_matrix)

    try:
        start_node = input("\nEnter source node (A-M): ").strip().upper()
        end_node = input("Enter target node (A-M): ").strip().upper()

        if start_node not in node_index_map or end_node not in node_index_map:
            raise ValueError("Invalid node input")

        path, weight = shortest_path(adj_matrix, start_node, end_node)
        print(f"\nShortest path from {start_node} to {end_node}: {' -> '.join(path)}")
        print(f"Total path weight: {weight}")

    except ValueError as e:
        print(f"Error: {e}")
