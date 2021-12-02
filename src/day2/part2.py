import os


def solve(infile):
    position, depth, aim = 0, 0, 0

    for line in infile:
        split = line.split()
        direction = split[0]
        val = int(split[1])

        if direction == 'forward':
            position += val
            depth += aim * val
        elif direction == 'up':
            aim -= val
        else:
            aim += val

    return position * depth


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
