graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def dfs_optimal(graph, start, goal):
    open_list = [start]
    close_list = []
    if start == goal:
        print("Start node is the goal node ")
        return open_list

    if goal not in graph:
        print("Goal not found ")
        return None

    while open_list:
        path = open_list.pop()
        node = path[-1]

        if node not in close_list:
            close_list.append(node)

        for neighbour in graph[node]:
            new_path = list(path)
            new_path.append(neighbour)
            open_list.append(new_path)
            if neighbour == goal:
                return new_path;

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = dfs_optimal(graph, start, goal)

if path:
    print(f"The path to {goal}: {path}")
else:
    print(f"No path found to {goal}")