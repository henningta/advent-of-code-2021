import numpy as np
import os

SIZE = 100


def solve(infile):
    valleys_sum = 0

    arr = np.full((SIZE + 2, SIZE + 2), np.inf)
    for i, line in enumerate(infile):
        parsed = [int(x) for x in line[:-1]]
        arr[i + 1, 1:-1] = parsed

    # slider = np.lib.stride_tricks.sliding_window_view(arr, (3, 3))

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            possible_valley = True

            window_flat = arr[i-1, j-1], arr[i-1, j], arr[i-1, j+1], \
                arr[i,   j-1], arr[i,   j], arr[i,   j+1], \
                arr[i+1, j-1], arr[i+1, j], arr[i+1, j+1]

            # make sure all other elements are higher values
            for elem in window_flat[:4]:
                if elem <= window_flat[4]:
                    possible_valley = False
                    break
            if possible_valley:
                for elem in window_flat[5:]:
                    if elem <= window_flat[4]:
                        possible_valley = False
                        break

            if possible_valley:
                valleys_sum += 1 + int(arr[i, j])

    return valleys_sum


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
