import os


def check_lines(lines, index):
    list_0 = []
    list_1 = []

    for line in lines:
        bit = int(line[index])
        if bit == 0:
            list_0.append(line)
        else:
            list_1.append(line)

    if len(list_1) >= len(list_0):
        return list_1, list_0
    else:
        return list_0, list_1


def solve(infile):
    infile.seek(0, 0)

    more, less = check_lines(infile, 0)

    index = 1

    while index < 12:
        if len(more) > 1:
            more, _ = check_lines(more, index)

        if len(less) > 1:
            _, less = check_lines(less, index)

        index += 1

    oxygen_bits = more[0][:-1]
    co2_bits = less[0][:-1]

    oxygen = 0
    co2 = 0
    for i in range(12):
        power = 11 - i
        oxygen += int(oxygen_bits[i]) * (2 ** power)
        co2 += int(co2_bits[i]) * (2 ** power)

    return oxygen * co2


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
