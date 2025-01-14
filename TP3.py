# Step 1: Construct Adjacency Matrix
def construct_adjacency_matrix(edges, n):
    # Initialize an n x n matrix with 0s
    adj_matrix = [[0] * n for _ in range(n)]
    for src, dest in edges:
        adj_matrix[src - 1][dest - 1] = 1  # Adjust for 0-based indexing
    return adj_matrix


# Step 2: Perform Inorder Traversal
def inorder_traversal(tree, node):
    if node not in tree:
        return []

    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []

    return left + [node] + right


# Input Graph Data
edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 5), (5, 7)]
n = 8  # Number of nodes

# Construct Adjacency Matrix
adj_matrix = construct_adjacency_matrix(edges, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Convert Graph to Tree Representation (Adjacency List)
tree = {
    1: [2, 3],       # Node 1 has children 2 and 3
    2: [5, 6],       # Node 2 has children 5 and 6
    3: [4],          # Node 3 has child 4
    4: [8],          # Node 4 has child 8
    5: [7],          # Node 5 has child 7
    6: [],           # Node 6 is a leaf
    7: [],           # Node 7 is a leaf
    8: []            # Node 8 is a leaf
}

# Input: Node label (x)
x = int(input("Enter the node label to print subtree in Inorder: "))

# Perform Inorder Traversal
inorder_result = inorder_traversal(tree, x)
print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")