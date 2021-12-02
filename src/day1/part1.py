import os


def solve(infile):
    incremented = 0

    # reset file cursor and read first line
    infile.seek(0, 0)
    last_line = int(infile.readline())

    # check each line after the first
    for line in infile:
        parsed_line = int(line)
        if parsed_line > last_line:
            incremented += 1
        last_line = parsed_line

    return incremented


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        incremented = solve(infile)
        print(incremented)


if __name__ == '__main__':
    main()
