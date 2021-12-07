import numpy as np
import os

BOARD_SIZE = 999


def order_by_x(x1, y1, x2, y2):
    return (x1, y1, x2, y2) if x2 > x1 else (x2, y2, x1, y1)


def build_lines(infile):
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), np.uint8)

    for line in infile:
        point1, point2 = line[:-1].split(' -> ')
        x1, y1 = [int(x) for x in point1.split(',')]
        x2, y2 = [int(x) for x in point2.split(',')]

        if x1 == x2:
            # vertical
            first = min(y1, y2)
            last = max(y1, y2)
            board[first:last + 1, x1] += 1
        elif y1 == y2:
            # horizontal
            first = min(x1, x2)
            last = max(x1, x2)
            board[y1, first:last + 1] += 1
        else:
            # diagonal (45 degree)
            # let's always go left to right
            first_x, first_y, _, last_y = order_by_x(x1, y1, x2, y2)

            x = first_x

            if last_y > first_y:
                # sloping down
                for i in range(first_y, last_y + 1):
                    board[i, x] += 1
                    x += 1
            else:
                # sloping up
                for i in range(first_y, last_y - 1, -1):
                    board[i, x] += 1
                    x += 1

    return board


def solve(infile):
    board = build_lines(infile)
    # np.savetxt('test.txt', board, fmt='%i', delimiter='')
    return np.count_nonzero(board >= 2)


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
