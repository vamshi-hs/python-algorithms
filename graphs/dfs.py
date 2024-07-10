def dfs_iterative(graph,start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end = ' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

def dfs_recursive(graph,vertex,visited=None):
    if visited is None:
        visited = set()

    visited.add(vertex)
    print(vertex, end = ' ')

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs_recursive(graph,neighbour,visited)
        

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': [],
        }
    print("Iterative: ")
    dfs_iterative(graph,'A')
    print()
    print("Recursive: ")
    dfs_recursive(graph,'A')
    
