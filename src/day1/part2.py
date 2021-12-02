import os


def solve(infile):
    incremented = 0

    # reset file cursor and read first line
    infile.seek(0, 0)

    # windows, baby
    window1 = int(infile.readline())
    window2 = int(infile.readline())
    window3 = int(infile.readline())

    last_window = window1 + window2 + window3

    # check each line after the first
    for line in infile:
        window1 = window2
        window2 = window3
        window3 = int(line)

        window = window1 + window2 + window3

        if window > last_window:
            incremented += 1
        last_window = window

    return incremented


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        incremented = solve(infile)
        print(incremented)


if __name__ == '__main__':
    main()
