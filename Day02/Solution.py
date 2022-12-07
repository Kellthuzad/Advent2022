def main():
    lines = [l.strip() for l in open("./Day2/input.txt")]
    output = 0
    for line in lines:
        output += ruleEvaluation2(line)

    print(output)


def ruleEvaluation(line):

    if 'A' in line:
        if 'X' in line:
            return 1+3
        elif 'Y' in line:
            return 2+6
        elif 'Z' in line:
            return 3+0
    elif 'B' in line:
        if 'X' in line:
            return 1+0
        elif 'Y' in line:
            return 2+3
        elif 'Z' in line:
            return 3+6
    elif 'C' in line:
        if 'X' in line:
            return 1+6
        elif 'Y' in line:
            return 2+0
        elif 'Z' in line:
            return 3+3


def ruleEvaluation2(line):

    if 'A' in line:
        if 'X' in line:
            return 3+0
        elif 'Y' in line:
            return 1+3
        elif 'Z' in line:
            return 2+6
    elif 'B' in line:
        if 'X' in line:
            return 1+0
        elif 'Y' in line:
            return 2+3
        elif 'Z' in line:
            return 3+6
    elif 'C' in line:
        if 'X' in line:
            return 2+0
        elif 'Y' in line:
            return 3+3
        elif 'Z' in line:
            return 1+6


main()