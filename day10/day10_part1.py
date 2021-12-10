class CharQueue:
    matching_symbols = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }

    penalties = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    def __init__(self):
        self.queue = []

    def open(self, char: str):
        self.queue.append(char)

    def close(self, close_char: str) -> int:
        char = self.queue.pop()
        if char != self.matching_symbols[close_char]:
            return self.penalties[close_char]
        return 0


def check_line(line: [str]) -> int:
    queue: CharQueue = CharQueue()
    for char in line:
        is_opening = char in ['(', '[', '{', '<']
        if is_opening:
            queue.open(char)
        else:
            penalty = queue.close(char)
            if penalty > 0:
                return penalty
    return 0


if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = [[c for c in i.strip()] for i in f.readlines()]
    # print(lines)

    penalties = []
    for line in lines:
        print(line)
        penalty = check_line(line)
        penalties.append(penalty)
    print(sum(penalties))
