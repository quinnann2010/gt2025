from collections import defaultdict, deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    # Create adjacency matrix
    def get_adj_matrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]  # Initialize matrix with 0
        for src, neighbors in self.graph.items():
            for dest in neighbors:
                matrix[src - 1][dest - 1] = 1  # Adjusting for 0-based indexing
        return matrix

    # Count weakly connected components
    def count_weak_components(self):
        visited = set()
        components = 0

        # Convert directed graph to undirected graph
        undirected_graph = defaultdict(set)
        for src, neighbors in self.graph.items():
            for dest in neighbors:
                undirected_graph[src].add(dest)
                undirected_graph[dest].add(src)

        # BFS for traversal
        def bfs(node):
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for neighbor in undirected_graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        # Traverse all nodes
        for node in range(1, self.n + 1):
            if node not in visited:
                components += 1  # New component found
                visited.add(node)
                bfs(node)

        return components

    # Count strongly connected components using Kosaraju's algorithm
    def count_strong_components(self):
        visited = set()
        finish_order = []

        # First DFS to get finish order
        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            finish_order.append(node)

        # Get transposed graph
        def get_transposed():
            transposed = Graph(self.n)
            for src, neighbors in self.graph.items():
                for dest in neighbors:
                    transposed.add_edge(dest, src)
            return transposed

        # Get finishing order of nodes
        for node in range(1, self.n + 1):
            if node not in visited:
                dfs(node)

        # Transpose the graph
        transposed = get_transposed()

        # Second DFS on transposed graph
        visited.clear()
        components = 0

        def dfs_transposed(node):
            visited.add(node)
            for neighbor in transposed.graph[node]:
                if neighbor not in visited:
                    dfs_transposed(neighbor)

        # Process nodes in reverse finish order
        while finish_order:
            node = finish_order.pop()
            if node not in visited:
                components += 1  # New strongly connected component
                dfs_transposed(node)

        return components


# Example usage
n = 9
graph = Graph(n)
edges = [
    (1, 2), (1, 4), (2, 3), (2, 6), (5, 4), (5, 9), (5, 5),
    (6, 3), (6, 4), (7, 3), (7, 5), (7, 6), (7, 8), (8, 3), (8, 9)
]
for src, dest in edges:
    graph.add_edge(src, dest)

# Print adjacency matrix
adj_matrix = graph.get_adj_matrix()
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Count weak and strong components
weak_components = graph.count_weak_components()
strong_components = graph.count_strong_components()

print("\nNumber of Weakly Connected Components:", weak_components)
print("Number of Strongly Connected Components:", strong_components)