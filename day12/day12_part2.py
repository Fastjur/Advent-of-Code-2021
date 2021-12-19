from collections import defaultdict

f = open("input.txt", "r")
paths = [l.strip().split("-") for l in f.readlines()]

graph = defaultdict(list)
for path in paths:
    a, b = path[0], path[1]
    graph[a].append(b)
    graph[b].append(a)

nodes = dict.fromkeys(map(lambda p: p, graph), 0)
print(graph)
print(nodes)

paths = []


def visit_neighbour(node, path, visited_twice):
    if node.islower():
        if node in path and visited_twice:
            return
        if node in path:
            visited_twice = True

    print(node)
    path.append(node)

    if node == "end":
        paths.append(path)
        print(",".join(path) + "\n")
        return

    neighbours = graph[node]
    for neighbour in neighbours:
        if neighbour == "start":
            continue
        new_path = path.copy()
        visit_neighbour(neighbour, new_path, visited_twice)



visit_neighbour("start", [], False)
print(len(paths))
