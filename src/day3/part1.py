import os


def solve(infile):
    totals_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totals_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    highest = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lowest = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for line in infile:
        for i, c in enumerate(line[:-1]):
            bit = int(c)
            if bit == 0:
                totals_0[i] += 1
            else:
                totals_1[i] += 1

    for i in range(len(totals_1)):
        if totals_1[i] >= totals_0[i]:
            highest[i] = 1
            lowest[i] = 0
        else:
            highest[i] = 0
            lowest[i] = 1

    gamma = 0
    epsilon = 0

    for i in range(len(highest)):
        power = len(highest) - i - 1
        gamma += highest[i] * (2 ** power)
        epsilon += lowest[i] * (2 ** power)

    return gamma * epsilon


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
