from collections import defaultdict

f = open("test.txt", "r")
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

        if neighbour.islower():
            if neighbour in path and visited_twice:
                continue
            if neighbour in path:
                visited_twice = True

        new_path = path.copy()
        visit_neighbour(neighbour, new_path, visited_twice)


visit_neighbour("start", [], False)
print(len(paths))
