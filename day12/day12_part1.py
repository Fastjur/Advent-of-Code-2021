from collections import defaultdict

f = open("input.txt", "r")
paths = [l.strip().split("-") for l in f.readlines()]

graph = defaultdict(list)
for path in paths:
    a, b = path[0], path[1]
    graph[a].append(b)
    graph[b].append(a)

print(graph)

paths = []


def visit_neighbour(node, path):
    path.append(node)
    if node == "end":
        paths.append(path)
        return

    neighbours = graph[node]
    for neighbour in neighbours:
        new_path = path.copy()
        if neighbour == "start":
            continue
        if neighbour.islower() and neighbour in path:
            continue
        visit_neighbour(neighbour, new_path)


visit_neighbour("start", [])
print(len(paths))
