graph = {
    'A' : ['B','C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : ['F'],
    'F' : []
}

def bfs(graph, start):
    open = [start]
    close = []
    while open:
        node = open.pop(0)
        if node not in close:
            close.append(node)
            for neighbour in graph[node]:
                open.append(neighbour)
    return close

print(bfs(graph, 'A'))
