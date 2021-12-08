import numpy as np
import os


def solve(infile):
    nums = [int(x) for x in infile.readline()[:-1].split(',')]
    numpers = np.array(nums, np.int16)
    median = int(np.median(numpers))
    return np.sum(abs(numpers - median))


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
