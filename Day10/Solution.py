
def main():
    lines = parse()
    cycleVals = cycle(240, lines)
    Part2(cycleVals)
    
def Part1(cycleVals):
    answer = 0
    for x in range(20, 260, 40):
        answer += cycleVals[x] * x
    return answer

def Part2(cycleVals):
    screen = []
    for i in range(6):
        screen.append([])
        for _ in range(40):
            screen[i].append(' ')

    cycle = 1
    while cycle <= 240:
        row = (cycle-1) // 40
        column = (cycle - 1) % 40
        
        if abs(cycleVals[cycle] - column) <= 1:
            screen[row][column] = '#'

        cycle += 1
    
    for line in screen:
        printable = ''
        print(printable.join(line))


def cycle(cycleCount, lines):
    cycle = 1
    X = 1
    cycleVals = {}
    index = 0
    while cycle <= cycleCount:
        index = index % len(lines)
        if 'a' == lines[index][0]:
            _, value = lines[index].split()
            cycleVals[cycle] = X
            cycle += 1
            cycleVals[cycle] = X
            cycle += 1
            X += int(value)
        else:
            cycleVals[cycle] = X
            cycle += 1
        index += 1
    
    return cycleVals
            

        






def parse():
    lines = [l.strip() for l in open("./Day10/input.txt")]
    return lines

main()
        