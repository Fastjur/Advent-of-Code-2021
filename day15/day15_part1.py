import numpy as np


def get_neighbours(u: (int, int), max_y: int, max_x: int) -> [(int, int)]:
    return [
               (y, u[1])
               for y in [u[0] - 1, u[0] + 1] if 0 <= y <= max_y
           ] + [
               (u[0], x)
               for x in [u[1] - 1, u[1] + 1] if 0 <= x <= max_x
           ]


def get_final_path(prev: {(int, int): int}, target: (int, int), source: (int, int)) -> [(int, int)]:
    S = []
    u = target
    if prev[u] is not None or u == source:
        while u is not None:
            S.append(u)
            u = prev[u]
    S.reverse()
    print("Final path:", S)
    return S


def main():
    lines = [[int(c) for c in l.strip()] for l in open("input.txt", "r").readlines()]
    print(lines)

    y_size = len(lines)
    x_size = len(lines[0])

    Q: {(int, int)} = {(y, x) for y in range(y_size) for x in range(x_size)}
    dist = {p: np.Inf for p in Q}
    prev = {p: None for p in Q}

    source = (0, 0)
    target = (y_size - 1, x_size - 1)
    dist[source] = 0

    print(Q)
    print(dist)
    print(prev)

    while Q:
        u_dist = np.Inf
        u = None
        for u2 in Q:
            if dist[u2] < u_dist:
                u_dist = dist[u2]
                u = u2
        Q.remove(u)

        if u == target:
            print("Final path cost:", dist[target])
            exit()

        for v in get_neighbours(u, y_size - 1, x_size - 1):
            if v in Q:
                alt = dist[u] + lines[v[0]][v[1]]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u


if __name__ == '__main__':
    main()
