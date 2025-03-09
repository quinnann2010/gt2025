from collections import deque, defaultdict

def path_exists(graph, start, end):
    if start == end:
        return True, [start]
    
    visited = set()
    queue = deque([(start, [start])])  
    
    while queue:
        current_node, path = queue.popleft()
        if current_node == end:
            return True, path
        
        visited.add(current_node)
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    
    return False, []

def build_graph():
    graph = defaultdict(list)
    edges = int(input("Enter number of edges: "))
    for _ in range(edges):
        u, v = input("Enter edge (from to): ").split()
        graph[u].append(v)
    return graph

if __name__ == "__main__":
    graph = build_graph()
    
    start = input("Start node: ").strip()
    end = input("End node: ").strip()
    
    if start not in graph:
        print(f"Error: Start node '{start}' does not exist in the graph.")
    elif end not in graph:
        print(f"Error: End node '{end}' does not exist in the graph.")
    else:
        exists, path = path_exists(graph, start, end)
        if exists:
            print(f"=> Path exists between {start} and {end}: {' -> '.join(path)}")
        else:
            print(f"=> No path exists between {start} and {end}.")
