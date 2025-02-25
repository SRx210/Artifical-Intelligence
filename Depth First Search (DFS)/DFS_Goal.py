graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def dfs_goal_node(graph, start, goal):
    open_list = [start]
    close_list = []

    if start == goal:
        print("Start node is same as goal node")
        return open_list

    if goal not in graph:
        print("Goal node doesnt exist")
        return None

    while open_list:
        node = open_list.pop()
        if node == goal:
            return close_list + [node]

        if node not in close_list:
            close_list.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in close_list:
                    open_list.append(neighbor)

    return None

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = dfs_goal_node(graph, start, goal)

if path:
    print(f"The path to {goal}: {path}")
else:
    print(f"No path found to {goal}")


