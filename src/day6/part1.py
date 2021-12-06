import os

DAYS = 80


def simulate_day(lantern_fish):
    new_fish = 0
    for i, fish in enumerate(lantern_fish):
        if fish == 0:
            # spawn new fish
            new_fish += 1
            lantern_fish[i] = 6
        else:
            lantern_fish[i] -= 1

    return lantern_fish + ([8] * new_fish)


def solve(infile):
    lantern_fish = [int(x) for x in infile.readline()[:-1].split(',')]
    for _ in range(DAYS):
        lantern_fish = simulate_day(lantern_fish)
    return len(lantern_fish)


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
