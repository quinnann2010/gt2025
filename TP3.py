from collections import defaultdict, deque

class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def get_adj_matrix(self):
        matrix = [[0] * self.n for _ in range(self.n)]
        for src, neighbors in self.graph.items():
            for dest in neighbors:
                matrix[src - 1][dest - 1] = 1
        return matrix

    def count_weak_components(self):
        visited = set()
        components = 0

        undirected_graph = defaultdict(set)
        for src, neighbors in self.graph.items():
            for dest in neighbors:
                undirected_graph[src].add(dest)
                undirected_graph[dest].add(src)

        def bfs(node):
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for neighbor in undirected_graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        for node in range(1, self.n + 1):
            if node not in visited:
                components += 1
                visited.add(node)
                bfs(node)

        return components

    def count_strong_components(self):
        visited = set()
        finish_order = []

        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            finish_order.append(node)

        def get_transposed():
            transposed = Graph(self.n)
            for src, neighbors in self.graph.items():
                for dest in neighbors:
                    transposed.add_edge(dest, src)
            return transposed

        for node in range(1, self.n + 1):
            if node not in visited:
                dfs(node)

        transposed = get_transposed()
        visited.clear()
        components = 0

        def dfs_transposed(node):
            visited.add(node)
            for neighbor in transposed.graph[node]:
                if neighbor not in visited:
                    dfs_transposed(neighbor)

        while finish_order:
            node = finish_order.pop()
            if node not in visited:
                components += 1
                dfs_transposed(node)

        return components

def construct_adjacency_matrix(edges, n):
    adj_matrix = [[0] * n for _ in range(n)]
    for src, dest in edges:
        adj_matrix[src - 1][dest - 1] = 1
    return adj_matrix

def inorder_traversal(tree, node):
    if node not in tree:
        return []
    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []
    return left + [node] + right

if __name__ == "__main__":
    n = 8
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 5), (5, 7)]
    adj_matrix = construct_adjacency_matrix(edges, n)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)
    
    tree = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }
    x = int(input("Enter the node label to print subtree in Inorder: "))
    inorder_result = inorder_traversal(tree, x)
    print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")
