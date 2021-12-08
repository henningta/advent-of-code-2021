import os


def solve(infile):
    total = 0

    for line in infile:
        _, second = line[:-1].split(' | ')
        split = second.split(' ')

        for token in split:
            if len(token) == 2 or len(token) == 3 or len(token) == 4 or len(token) == 7:
                total += 1

    return total


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
