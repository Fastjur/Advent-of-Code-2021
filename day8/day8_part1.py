if __name__ == "__main__":
    f = open("input.txt", "r")
    count = 0
    lines = f.readlines()
    for line in lines:
        digits = line.split(" | ")[1].strip().split(" ")
        print(digits)
        count = count + len(list(filter(lambda it: len(it) == 2 or len(it) == 4 or len(it) == 3 or len(it) == 7, digits)))
    print(count)