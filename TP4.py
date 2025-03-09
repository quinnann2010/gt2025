import heapq

class GraphMST:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)

    def prim(self, root):
        mst_edges = []
        visited = [False] * self.num_nodes
        min_heap = [(0, root, -1)]  # (weight, current_node, parent_node)
        total_weight = 0

        while min_heap:
            weight, node, parent = heapq.heappop(min_heap)
            
            if visited[node]:
                continue
            
            visited[node] = True
            total_weight += weight
            if parent != -1:
                mst_edges.append((parent + 1, node + 1, weight))  # Convert to 1-based index
            
            for adj in range(self.num_nodes):
                if not visited[adj] and self.graph[node][adj] != float('inf'):
                    heapq.heappush(min_heap, (self.graph[node][adj], adj, node))
        
        return mst_edges, total_weight

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

    def kruskal(self, graph):
        num_nodes = len(graph)
        edges = []
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                if graph[i][j] != float('inf'):
                    edges.append((graph[i][j], i, j))  # (weight, node1, node2)
        
        edges.sort()
        uf = UnionFind(num_nodes)
        mst_edges = []
        total_weight = 0
        
        for weight, u, v in edges:
            if uf.union(u, v):
                mst_edges.append((u + 1, v + 1, weight))  # Convert to 1-based index
                total_weight += weight
        
        return mst_edges, total_weight

if __name__ == "__main__":
    graph = [
        [0, 4, float('inf'), float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
        [4, 0, 7, float('inf'), float('inf'), 5, float('inf'), float('inf'), float('inf')],
        [float('inf'), 7, 0, 1, float('inf'), 8, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), 1, 0, float('inf'), 6, 4, 3, float('inf')],
        [1, float('inf'), float('inf'), float('inf'), 0, 9, 10, float('inf'), float('inf')],
        [float('inf'), 5, 8, 6, 9, 0, float('inf'), float('inf'), 2],
        [2, float('inf'), float('inf'), 4, 10, float('inf'), 0, float('inf'), 8],
        [float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 8, 1, 0]
    ]

    while True:
        try:
            root_node = int(input("Enter the root node (1-9): ")) - 1
            if 0 <= root_node < len(graph):
                break
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    prim_mst = GraphMST(graph)
    mst_edges_prim, total_weight_prim = prim_mst.prim(root_node)
    print("\nPrim's Algorithm - MST edges and weights:")
    for edge in mst_edges_prim:
        print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
    print(f"Total weight of MST: {total_weight_prim}")
    
    uf = UnionFind(len(graph))
    mst_edges_kruskal, total_weight_kruskal = uf.kruskal(graph)
    print("\nKruskal's Algorithm - MST edges and weights:")
    for edge in mst_edges_kruskal:
        print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
    print(f"Total weight of MST: {total_weight_kruskal}")
