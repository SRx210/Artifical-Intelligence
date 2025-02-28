graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

def iterative_deepening(graph, start, goal, depth_limit):
    for depth in range(depth_limit + 1):
        open_list = [(start, 0)]
        close_list = []

        while open_list:
            node, node_depth = open_list.pop()

            if node_depth > depth:
                continue

            if node not in close_list:
                close_list.append(node)

            if node == goal:
                return close_list

            for neighbor in reversed(graph[node]):
                open_list.append((neighbor, node_depth + 1))

    return None

start = input("Enter start node: ")
goal = input("Enter goal node: ")
depth_limit = int(input("Enter the depth limit: "))

path = iterative_deepening(graph, start, goal, depth_limit)

if path:
    print(f"The path to {goal}: {path}")
else:
    print(f"The path to {goal} not found")
