def calculate_fuel(diff: int) -> int:
    return int(diff*(diff + 1)/2)


if __name__ == "__main__":
    f = open("input.txt", "r")
    initial_positions = [int(i) for i in f.readline().split(",")]

    max_pos = max(initial_positions)

    cheapest_position = None
    cheapest_fuel = None
    for i in range(max_pos):
        fuel = 0
        for pos in initial_positions:
            fuel = fuel + calculate_fuel(abs(pos - i))
        if cheapest_fuel is None or fuel < cheapest_fuel:
            cheapest_fuel = fuel
            cheapest_position = i

    print(cheapest_position, cheapest_fuel)