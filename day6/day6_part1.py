if __name__ == "__main__":
    f = open("input.txt", "r")
    state = [int(i) for i in f.readlines()[0].strip().split(",")]
    print("Initial state:", state)

    N = 256
    for day in range(1, N + 1):
        to_add = 0
        for i in range(len(state)):
            if state[i] == 0:
                state[i] = 6
                to_add = to_add + 1
            else:
                state[i] = state[i] - 1
        state = state + [8] * to_add
        print("Day:", day)

    print("Number of fish:", len(state))