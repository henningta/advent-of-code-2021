import numpy as np
import os

CLEAN_BINGO = np.zeros((5, 5), np.uint8)


def build_boards(infile):
    boards = []

    board_lines = []
    for line in infile:
        parsed = [int(x) for x in line[:-1].split()]
        board_lines.append(parsed)

        if len(board_lines) == 5:
            board = np.array((board_lines, CLEAN_BINGO))
            # print(board)
            boards.append(board)
            board_lines = []
            infile.readline()

    return boards


def check_bingo(board):
    checked = board[1]
    bingo = False

    for row in checked:
        if np.all(row == 1):
            bingo = True
            break

    if not bingo:
        for col in checked.T:
            if np.all(col == 1):
                bingo = True
                break

    if bingo:
        actual = board[0]
        unmarked = np.where(checked == 0)
        unmarked_sum = np.sum(actual[unmarked])
        return True, unmarked_sum
    else:
        return False, None


def solve(infile):
    infile.seek(0, 0)

    # first line has the bingo numbers
    bingo_numbers = [int(x) for x in infile.readline()[:-1].split(',')]
    # print(bingo_numbers)

    # build bingo boards
    infile.readline()
    boards = build_boards(infile)
    # print(boards)

    bingo = False
    unmarked_sum = None
    number = None

    for i in range(len(bingo_numbers)):
        number = bingo_numbers[i]

        for board in boards:
            index = np.where(board[0] == number)

            if len(index[0] == 1):
                # number is in board
                y, x = index[0][0], index[1][0]
                board[1][y][x] = 1
                bingo, unmarked_sum = check_bingo(board)

                if bingo:
                    return unmarked_sum * number

    return None


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
