#Task3
graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C', 'E', 'G'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A'],
    'E': ['G', 'F', 'B'],
    'F': ['G', 'E'],
    'G': ['F', 'B']
}


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)
    return visited


def bfs(graph, start):
    visited = []
    queue = [start]
    visited.append(start)

    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited


print("DFS:", dfs(graph, 'A'))
print("BFS:", bfs(graph, 'A'))