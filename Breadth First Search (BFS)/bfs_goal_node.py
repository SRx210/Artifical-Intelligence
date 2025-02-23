graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E', 'F'],
    'C' : ['G', 'H', 'E'],
    'D' : ['J'],
    'E' : ['K'],
    'F' : ['L'],
    'G' : ['M'],
    'H' : ['N'],
    'I' : ['O'],
    'J' : [],
    'K' : [],
    'L' : [],
    'M' : [],
    'N' : [],
    'O' : []
}

def bfs(graph, start, goal):
    open_list = [start]
    close_list = []
    
    if start == goal:
        print("Start node and goal node are the same. Please enter a valid goal node.")
        return open_list
    
    if goal not in graph:
        print(f"Goal node '{goal}' is not present in the graph. Please enter a valid goal node.")
        return None
    
    while open_list:
        node = open_list.pop(0)
        if node == goal:
            return close_list + [node]
        
        if node not in close_list:
            close_list.append(node)
            for neighbour in graph[node]:
                open_list.append(neighbour)
    
    return None

start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

path = bfs(graph, start_node, goal_node)

if path:
    print(f"Path to {goal_node}: {path}")

