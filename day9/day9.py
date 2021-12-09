from pprint import pprint

if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = [[int(i) for i in j.strip()] for j in f.readlines()]
    max_y = len(lines)
    max_x = len(lines[0])


    def get_risk_level(y, x) -> int:
        curr = lines[y][x]
        lower_than_left = x == 0 or curr < lines[y][x - 1]
        lower_than_up = y == 0 or curr < lines[y - 1][x]
        lower_than_right = x == max_x - 1 or curr < lines[y][x + 1]
        lower_than_down = y == max_y - 1 or curr < lines[y + 1][x]
        if lower_than_left and lower_than_up and lower_than_right and lower_than_down:
            return curr + 1
        else:
            return 0


    Point = {
        'x': int,
        'y': int,
    }
    sum_risk_level = 0
    lowest_points: [Point] = []
    for y in range(max_y):
        for x in range(max_x):
            level = get_risk_level(y, x)
            sum_risk_level = sum_risk_level + level
            if level > 0:
                lowest_points.append({'x': x, 'y': y})


    def get_basin_size(curr_point: Point, visited: [Point], size: int) -> int:
        x = curr_point['x']
        y = curr_point['y']

        if y < 0 or x < 0 or y > max_y - 1 or x > max_x - 1 or lines[y][x] == 9 or curr_point in visited:
            return size

        size = size + 1
        visited.append(curr_point)

        next_down: Point = {'y': y + 1, 'x': x}
        next_up: Point = {'y': y - 1, 'x': x}
        next_left: Point = {'y': y, 'x': x - 1}
        next_right: Point = {'y': y, 'x': x + 1}

        size = get_basin_size(next_down, visited, size)
        size = get_basin_size(next_up, visited, size)
        size = get_basin_size(next_left, visited, size)
        size = get_basin_size(next_right, visited, size)
        return size

    basin_sizes = []
    for low_point in lowest_points:
        print(f"For low point {low_point}")
        basin_sizes.append(get_basin_size(low_point, [], 0))

    basin_sizes.sort(reverse=True)
    print(basin_sizes)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
