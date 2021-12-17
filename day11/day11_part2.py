f = open("input.txt", "r")
lines = [[int(j) for j in i.strip()] for i in f.readlines()]

max_y = len(lines) - 1
max_x = len(lines[0]) - 1
num_octopuses = (max_x + 1) * (max_y + 1)


def show_grid():
    for line in lines:
        print("".join(map(str, line)))
    print()


print("Before any steps:")
show_grid()


def get_valid_neighbours(point: (int, int)) -> {(int, int)}:
    neighbours: {(int, int)} = set()
    for y2 in range(-1, 2, 1):
        for x2 in range(-1, 2, 1):
            neighbour_y = y + y2
            neighbour_x = x + x2
            neighbour = (neighbour_y, neighbour_x)

            if neighbour == point:
                # If current, ignore
                continue

            if neighbour_y < 0 or neighbour_x < 0 or neighbour_y > max_y or neighbour_x > max_x:
                # If invalid neighbour, ignore
                continue

            neighbours.add(neighbour)
    return neighbours


flash_count = 0
N = 0
while True:
    N += 1
    prev_flash_count = flash_count
    should_flash: [(int, int)] = []
    for (y, line) in enumerate(lines):
        for (x, curr) in enumerate(line):
            lines[y][x] = curr + 1
            if curr + 1 == 10:
                should_flash.append((y, x))
    print("Should flash", should_flash)
    for flash in should_flash:
        flash_count += 1
        y = flash[0]
        x = flash[1]
        neighbours = get_valid_neighbours(flash)
        for neighbour in neighbours:
            lines[neighbour[0]][neighbour[1]] = lines[neighbour[0]][neighbour[1]] + 1
            if lines[neighbour[0]][neighbour[1]] == 10:
                should_flash.append(neighbour)

    for (y, line) in enumerate(lines):
        for (x, curr) in enumerate(line):
            if curr > 9:
                lines[y][x] = 0

    print(f"After step {N}:")
    show_grid()

    if flash_count - prev_flash_count == num_octopuses:
        print(f"Synchronised flash at {N}")
        exit()
