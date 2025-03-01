graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def dfs_traversal(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                stack.append(neighbour)
    return visited

path = dfs_traversal(graph, 'A')

if path:
    print(f"Traversal: {path}")


