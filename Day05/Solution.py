import urllib.request as Request

def main():
    lines = [l.strip() for l in open("./Day5/input.txt")]
    commands = parse(lines)
    moveCrates2(commands)
    answer = ''
    for line in stacks:
        answer += line[0]
    print(answer)

stacks = [
    ['N', 'Q', 'L', 'S', 'C', 'Z','P','T'],
    ['G','C','H','V','T', 'P', 'L'],
    ['F','Z','C','D'],
    ['C','V','M','L','D','T','W','G'],
    ['C','W','P'],
    ['Z','S','T','C','D','J','F','P'],
    ['D','B', 'G','W','V'],
    ['W','H','Q','S', 'J', 'N'],
    ['V', 'L','S','F','Q','C','R']
]

def moveCrates(commands):
    for crateCount, fromStack, toStack in commands:
        for _ in range(crateCount):
            elem = stacks[fromStack].pop(0)
            stacks[toStack].insert(0, elem)


def moveCrates2(commands):
    for crateCount, fromStack, toStack in commands:
        elem = stacks[fromStack][:crateCount]
        stacks[toStack] = elem + stacks[toStack]
        del stacks[fromStack][:crateCount]

def parse(lines):
    commands = []
    for line in lines:
        _, cratos, _, fromStack, _, toStack = line.split()
        commands.append((int(cratos), int(fromStack) - 1, int(toStack) - 1))
    return commands

main()