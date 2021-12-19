import numpy as np

lines = open("input.txt", "r").readlines()
dots = [[int(i) for i in l.strip().split(",")] for l in lines if "," in l]
folds = [l.strip()[11:].split("=") for l in lines if "fold along" in l]

print(dots)
print(folds)

x_size = max([l[0] for l in dots])
y_size = max([l[1] for l in dots])
print(f"Map size: {x_size + 1} x {y_size + 1}")

paper = np.full((y_size + 1, x_size + 1), False)

for dot in dots:
    paper[dot[1]][dot[0]] = True


def print_paper():
    if x_size < 100 and y_size < 100:
        for y in paper:
            print("".join(["#" if x else "." for x in y]))

print("Original paper:")
print_paper()
print()

for (idx, fold) in enumerate(folds):
    line = int(fold[1])
    if fold[0] == "x":
        for x in range(line):
            for y in range(y_size + 1):
                x2 = x_size - x
                paper[y][x] = paper[y][x] or paper[y][x2]
        x_size = int(x_size / 2) - 1
        paper = paper[:, :(-x_size - 2)]
    elif fold[0] == "y":
        for y in range(line):
            for x in range(x_size + 1):
                y2 = y_size - y
                paper[y][x] = paper[y][x] or paper[y2][x]
        y_size = int(y_size / 2) - 1
        paper = paper[:-y_size - 2, :]
    else:
        raise Exception("Illegal State")
    print("After fold", fold)
    print_paper()
    print("Dots visible", np.count_nonzero(paper))
    print(f"New map size: {x_size + 1} x {y_size + 1}")
    print()

