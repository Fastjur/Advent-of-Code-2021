import re

f = open("input.txt", "r")
lines = f.readlines()
numbers = [int(i) for i in lines[0].split(",")]
print(numbers)

lines = lines[1:]

# Convert into 2d array of boards
n = 6
boards = [lines[i * n: (i + 1) * n][1:] for i in range((len(lines) + n - 1) // n)]

boards_left_to_win = list(range(len(boards)))

# Remove \n from rows, and preceding space if present
boards = [[re.sub(re.compile(r"^ ?(.*)\n?$"), '\\1', row) for row in board] for board in boards]

# Remove all double spaces and split into list and convert into int values
boards = [[[int(i) for i in re.sub(re.compile(r" +"), ' ', row).split(' ')] for row in board] for board in boards]

print(boards)


def check_board(board) -> bool:
    board_size = len(board)
    board_transposed = [*zip(*board)]
    for i in range(board_size):
        if all([num == -1 for num in board[i]]) or all([num == -1 for num in board_transposed[i]]):
            return True


def get_winning_board_index() -> (int, int):
    for drawn_number in numbers:
        for (board_idx, board) in enumerate(boards):
            for (row_idx, row) in enumerate(board):
                for (col_idx, col) in enumerate(row):
                    if col == drawn_number:
                        boards[board_idx][row_idx][col_idx] = -1
                        if check_board(boards[board_idx]):
                            return board_idx, drawn_number


idx = drawn_number = -1
while len(boards_left_to_win) > 1:
    (idx, drawn_number) = get_winning_board_index()
    try:
        boards_left_to_win.remove(idx)
        print(idx, drawn_number)
    except ValueError:
        pass

to_win_last = boards_left_to_win[0]

while idx != to_win_last:
    (idx, drawn_number) = get_winning_board_index()

res = drawn_number * sum([i for board in boards[idx] for i in board if i != -1])
print(res)