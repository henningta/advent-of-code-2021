import os


def chars_match(str1, str2):
    if len(str1) != len(str2):
        return False
    for c in str1:
        if c not in str2:
            return False
    return True


def resolve_input(signals):
    tokens = {}

    sorted_signals = sorted(signals, key=len)
    # print(sorted_signals)

    signal1 = sorted_signals[0]
    signal7 = sorted_signals[1]
    signal4 = sorted_signals[2]
    signal8 = sorted_signals[9]

    # top segment must be the remaining segment in signal 7 minus signal 1
    top = signal7
    for c in signal1:
        top = top.replace(c, '')

    # looking for signal 3 and bottom segment
    signal3 = ''
    bottom = ''
    for signal in sorted_signals[3:6]:
        midAndBottom = signal.replace(top, '').replace(
            signal1[0], '').replace(signal1[1], '')
        if len(midAndBottom) == 2:
            if midAndBottom[0] in signal4:
                middle = midAndBottom[0]
                bottom = midAndBottom[1]
            else:
                middle = midAndBottom[1]
                bottom = midAndBottom[0]
            signal3 = signal
            break

    middle = signal3.replace(top, '').replace(
        bottom, '').replace(signal1[0], '').replace(signal1[1], '')

    # looking for signal 9 and top-left segment
    signal9 = ''
    topLeft = ''
    for signal in sorted_signals[6:9]:
        topLeft = signal.replace(top, '').replace(
            middle, '').replace(bottom, '').replace(signal1[0], '').replace(signal1[1], '')
        if len(topLeft) == 1:
            signal9 = signal
            break

    # looking for signal 0 and bottom-left
    signal0 = ''
    bottomLeft = ''
    for signal in sorted_signals[6:9]:
        if signal == signal9:
            continue
        bottomLeft = signal.replace(top, '').replace(topLeft, '').replace(
            bottom, '').replace(signal1[0], '').replace(signal1[1], '')
        if len(bottomLeft) == 1:
            signal0 = signal
            break

    # looking for signal 6 and top-right/bottom-right
    signal6 = ''
    topRight = ''
    bottomRight = ''
    for signal in sorted_signals[6:9]:
        if signal == signal9 or signal == signal0:
            continue
        signal6 = signal
        bottomRight = signal6.replace(top, '').replace(topLeft, '').replace(
            middle, '').replace(bottomLeft, '').replace(bottomRight, '').replace(bottom, '')
        topRight = signal1.replace(bottomRight, '')

    signal2 = top + topRight + middle + bottomLeft + bottom
    signal5 = top + topLeft + middle + bottomRight + bottom

    # print('signal 0 {}'.format(signal0))
    # print('signal 1 {}'.format(signal1))
    # print('signal 2 {}'.format(signal2))
    # print('signal 3 {}'.format(signal3))
    # print('signal 4 {}'.format(signal4))
    # print('signal 5 {}'.format(signal5))
    # print('signal 6 {}'.format(signal6))
    # print('signal 7 {}'.format(signal7))
    # print('signal 8 {}'.format(signal8))
    # print('signal 9 {}'.format(signal9))

    # print('top {}'.format(top))
    # print('topLeft {}'.format(topLeft))
    # print('topRight {}'.format(topRight))
    # print('middle {}'.format(middle))
    # print('bottomLeft {}'.format(bottomLeft))
    # print('bottomRight {}'.format(bottomRight))
    # print('bottom {}'.format(bottom))

    tokens = {
        signal0: 0,
        signal1: 1,
        signal2: 2,
        signal3: 3,
        signal4: 4,
        signal5: 5,
        signal6: 6,
        signal7: 7,
        signal8: 8,
        signal9: 9,
    }

    # print(tokens)

    return tokens


def solve(infile):
    total = 0

    for line in infile:
        first, second = line[:-1].split(' | ')
        split = second.split(' ')

        tokens = resolve_input(first.split())

        output_total = 0
        for i, output in enumerate(split):
            for key in tokens:
                if chars_match(output, key):
                    value = tokens[key]
                    break
            output_total += value * (10 ** (3 - i))

        # print(output_total)

        total += output_total

    return total


def main():
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'input.txt')

    with open(filepath, 'r') as infile:
        solved = solve(infile)
        print(solved)


if __name__ == '__main__':
    main()
