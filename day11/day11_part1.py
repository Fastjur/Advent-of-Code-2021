from pprint import pprint

f = open("test.txt", "r")
lines = [[int(j) for j in i.strip()] for i in f.readlines()]

max_y = len(lines) - 1
max_x = len(lines[0]) - 1


def show_grid():
    for line in lines:
        print("".join(map(str, line)))
    print()


print("Before any steps:")
show_grid()


def flash(should_flash: {(int, int)}, flashed: {(int, int)}, flash_count: int):
    new_should_flash: {(int, int)} = set()
    for (y, x) in should_flash:
        current = (y, x)
        lines[y][x] = 0
        flash_count = flash_count + 1
        flashed.add(current)
        for y2 in range(-1, 2, 1):
            for x2 in range(-1, 2, 1):
                neighbour_y = y + y2
                neighbour_x = x + x2
                neighbour = (neighbour_y, neighbour_x)

                if neighbour == current:
                    # If current, ignore
                    continue

                if neighbour_y < 0 or neighbour_x < 0 or neighbour_y > max_y or neighbour_x > max_x:
                    # If invalid neighbour, ignore
                    continue

                if neighbour in flashed:
                    # If neighbour already flashed, ignore
                    continue

                lines[neighbour_y][neighbour_x] = lines[neighbour_y][neighbour_x] + 1
                # print(neighbour, lines[neighbour_y][neighbour_x])

                if lines[neighbour_y][neighbour_x] > 9:
                    new_should_flash.add(neighbour)
    print("new should flash", new_should_flash)
    if len(new_should_flash) > 0:
        return flash_count + flash(new_should_flash, flashed, flash_count)
    return flash_count


N = 100
for i in range(1, N + 1):
    initial_flashes: {(int, int)} = set()
    flash_count = 0
    for (y, line) in enumerate(lines):
        for (x, octopus) in enumerate(line):
            lines[y][x] = octopus + 1
            if octopus + 1 > 9:
                flash_count = flash_count + 1
                initial_flashes.add((y, x))

    print("Initially:", initial_flashes)
    # print("After initial flashes:")
    # show_grid()

    res = flash(initial_flashes, initial_flashes, flash_count)
    print(f"After step {i}:")
    show_grid()
    print(res)
