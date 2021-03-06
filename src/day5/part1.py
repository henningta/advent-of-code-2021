import numpy as np
import os


def build_lines(infile):
    board = np.zeros((999, 999), np.uint8)

    for line in infile:
        point1, point2 = line[:-1].split(' -> ')
        x1, y1 = [int(x) for x in point1.split(',')]
        x2, y2 = [int(x) for x in point2.split(',')]

        if x1 != x2 and y1 != y2:
            # not vertical or horizontal
            continue

        if x1 == x2:
            # vertical
            first = min(y1, y2)
            last = max(y1, y2)
            board[first:last + 1, x1] += 1
        else:
            # horizontal
            first = min(x1, x2)
            last = max(x1, x2)
            board[y1, first:last + 1] += 1

    return board


def solve(infile):
    board = build_lines(infile)
    return np.count_nonzero(board >= 2)


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
