graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

def depth_limited(graph, start, goal, depth_limit):
    open_list = [(start, 0)]
    close_list = []

    if start == goal:
        print("Start node is the same as the goal node")
        return [start]

    if goal not in graph:
        print("Enter a valid goal node")
        return None

    while open_list:
        node, depth = open_list.pop()

        if node not in close_list:
            close_list.append(node)

        if node == goal:
            return close_list

        if depth < depth_limit:
            for neighbor in reversed(graph[node]):
                open_list.append((neighbor, depth + 1))

    return None


start = input("Enter start node: ")
goal = input("Enter goal node: ")
depth_limit = int(input("Enter depth limit: "))

path = depth_limited(graph, start, goal, depth_limit)

if path:
    print(f"The path to {goal}: {path}")
else:
    print(f"The path to {goal} not found within depth limit {depth_limit}.")
