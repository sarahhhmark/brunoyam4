def breadth_search(graph, start, visited=None, to_visit=None):
    if visited is None:
        visited, to_visit = [], []
    visited.append(start)
    for j in graph[start]:
        if j not in visited and j not in to_visit:
            to_visit.append(j)
    if set(graph.keys()) == set(visited):
        return visited
    return breadth_search(graph, start=to_visit[0], visited=visited, to_visit=to_visit[1:])

graph = {1: [7, 11, 13],
         2: [4, 6],
         3: [6, 12],
         4: [2, 13],
         5: [8, 9, 12],
         6: [2, 3, 12],
         7: [1],
         8: [5],
         9: [5, 13],
         10: [12],
         11: [1],
         12: [3, 5, 6, 10],
         13: [1, 4, 9]}

print(breadth_search(graph, 1))