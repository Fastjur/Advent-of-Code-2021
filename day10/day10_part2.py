from pprint import pprint
from typing import Union


class CharQueue:
    matching_symbols = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    matching_symbols_reversed = dict([(value, key) for key, value in matching_symbols.items()])

    penalties = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    def __init__(self):
        self.queue = []

    def open(self, char: str):
        self.queue.append(char)

    def close(self, close_char: str) -> int:
        char = self.queue.pop()
        if char != self.matching_symbols_reversed[close_char]:
            return self.penalties[close_char]
        return 0

    def is_incomplete(self):
        return len(self.queue) > 0

    def get_closing_char_penalties(self) -> [int]:
        closing_chars = []
        for char in reversed(self.queue):
            closing_chars.append(self.penalties[self.matching_symbols[char]])
        return closing_chars


def check_line(line: [str]) -> Union[bool, list]:
    queue: CharQueue = CharQueue()
    for char in line:
        is_opening = char in ['(', '[', '{', '<']
        if is_opening:
            queue.open(char)
        else:
            penalty = queue.close(char)
            if penalty > 0:
                return False

    if queue.is_incomplete():
        return queue.get_closing_char_penalties()

    return True


if __name__ == "__main__":
    f = open("input.txt", "r")
    lines = [[c for c in i.strip()] for i in f.readlines()]
    # print(lines)

    penalties = []
    for line in lines:
        res = check_line(line)
        if isinstance(res, list):
            final_penalty = 0
            for penalty in res:
                final_penalty = final_penalty * 5 + penalty
            penalties.append(final_penalty)
    penalties.sort()
    print(penalties[int(len(penalties) / 2)])