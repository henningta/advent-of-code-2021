import numpy as np
import os


def get_diff(num, mean):
    diff = abs(num - mean)
    total = diff
    for i in range(diff):
        total += i
    return total


def get_total(numpers, value):
    total = 0
    for x in numpers:
        total += get_diff(x, value)
    return total


def solve(infile):
    nums = [int(x) for x in infile.readline()[:-1].split(',')]
    numpers = np.array(nums, np.int16)
    mean = round(np.mean(numpers))

    total = get_total(numpers, mean)

    lowest = total
    look_down = True
    look_up = True
    while look_down or look_up:
        check_lower = mean - 1
        check_upper = mean + 1

        total_lower = get_total(numpers, check_upper)
        total_upper = get_total(numpers, check_lower)

        if total_lower < lowest:
            lowest = total_lower
        else:
            look_down = False

        if total_upper < lowest:
            lowest = total_upper
        else:
            look_up = False

    return lowest


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
