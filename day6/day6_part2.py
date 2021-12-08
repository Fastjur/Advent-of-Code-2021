if __name__ == "__main__":
    f = open("input.txt", "r")
    initial_state = [int(i) for i in f.readlines()[0].strip().split(",")]
    print("Initial state:", initial_state)

    N = 256
    ages = [0] * 9
    for age in initial_state:
        ages[age] = ages[age] + 1
    print(ages)

    for day in range(1, N + 1):
        print("Day:", day)
        to_add = ages[0]
        for i in range(1, len(ages)):
            ages[i - 1] = ages[i]
        ages[8] = to_add
        ages[6] = ages[6] + to_add
    print(sum(ages))