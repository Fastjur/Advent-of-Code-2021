from collections import defaultdict
from pprint import pprint

f = open("test.txt", "r")
paths = [l.strip().split("-") for l in f.readlines()]

graph = defaultdict(list)
for path in paths:
    a, b = path[0], path[1]
    graph[a].append(b)
    graph[b].append(a)

nodes = dict.fromkeys(map(lambda p: p, graph), 0)
print(graph)

paths = []


def visit_neighbour(node, path, visited):
    path.append(node)

    if node == "end":
        paths.append(path)
        print(",".join(path))
        return

    neighbours = graph[node]
    for neighbour in neighbours:
        if neighbour == "start":
            continue

        if neighbour.islower():
            visited[neighbour] += 1
            count_visited_twice = 0
            for n in visited:
                if visited[n] > 1:
                    count_visited_twice += 1
            # if count_visited_twice > 1:
                

        new_path = path.copy()
        visit_neighbour(neighbour, new_path, visited)


visit_neighbour("start", [], nodes.copy())
print(len(paths))
