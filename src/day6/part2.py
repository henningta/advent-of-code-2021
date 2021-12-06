import os

DAYS = 256


def simulate_day(counts):
    # spawn new fish
    new_fish = counts[0]

    for i in range(1, 9):
        counts[i - 1] = counts[i]
    counts[6] += new_fish
    counts[8] = new_fish

    return counts


def solve(infile):
    lantern_fish = [int(x) for x in infile.readline()[:-1].split(',')]

    counts = dict.fromkeys(range(9), 0)
    for fish in lantern_fish:
        counts[fish] += 1

    for _ in range(DAYS):
        counts = simulate_day(counts)

    total = 0
    for i in counts:
        total += counts[i]
    return total


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
