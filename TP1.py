from collections import deque

# Function: Check if path from start to end exists using BFS
def path_exists(graph, start, end):
    if start == end:
        return True

    visited = set()
    queue = deque([start])  

    while queue:
        current_node = queue.popleft()  
        if current_node == end:
            return True

        visited.add(current_node)  

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False

graph = {
    '1': ['2'],
    '2': ['5'],
    '3': ['6'],
    '4': ['6', '7'],
    '5': [],
    '6': ['7'],
    '7': []
}

start = input("Start node: ").strip()

end = input("End node: ").strip()

if start not in graph:
    print(f"Error: Start node '{start}' does not exist in the graph.")
elif end not in graph:
    print(f"Error: End node '{end}' does not exist in the graph.")
else:
    if path_exists(graph, start, end):
        print(f"=> Path exists between {start} and {end}.")
    else:
        print(f"=> No path exists between {start} and {end}.")
