import math

def main():
    monkeys = parse()

    print((4792 - 97)/ (1000 - 20))
    print(MonkeyBusiness(monkeys))

def MonkeyBusiness(monkeys):
    loops = 0
    touchCounts = []
    while loops < 10000:
        for key, monkey in monkeys.items():
            for item in monkey.items:
                item = monkey.RunOp(item)
                item = item % 9699690
                recipent = monkey.TestItem(item)
                monkeys[recipent].items.append(item)
            monkey.items = []
        loops += 1
    
    
    for _, monkey in monkeys.items():
        touchCounts.append(monkey.touchCount)
    touchCounts = sorted(touchCounts, reverse=True)
    return math.prod(touchCounts[:2])


def parse():
    lines = [l.strip() for l in open("./Day11/input.txt")]
    monkeys = {}
    currentMonkey = 0

    for line in lines:
        splits = line.split()
        if line == '':
            continue
        if splits[0] == 'Monkey':
            monkeys[int(splits[1][0])] = Monkey()
            currentMonkey = int(splits[1][0])
        if 'Starting items:' in line:
            nums = []
            _, ints = line.split(':')
            for num in ints.split(','):
                nums.append(int(num))
            monkeys[currentMonkey].items = nums
        elif 'Operation:' in line:
            val = ''
            if '+' in line:
                _, val = line.split('+')
                monkeys[currentMonkey].operator = '+'
            else:
                _, val = line.split('*')
                monkeys[currentMonkey].operator = "*"
            monkeys[currentMonkey].opVal = val.strip()
        elif 'Test:' in line:
            monkeys[currentMonkey].testVal = int(splits[-1])
        elif 'If true:' in line:
            monkeys[currentMonkey].trueMonkey = int(splits[-1])
        elif 'If false:' in line:
            monkeys[currentMonkey].falseMonkey = int(splits[-1])


    return monkeys


class Monkey:
    def __init__(self):
        self.testVal = 0
        self.trueMonkey = 0
        self.falseMonkey = 0
        self.items = []
        self.operator = ''
        self.opVal = ''
        self.touchCount = 0

    def TestItem(self, item):
        if item % self.testVal == 0:
            return self.trueMonkey
        return self.falseMonkey

    def RunOp(self, item):
        self.touchCount += 1
        if self.opVal == 'old':
            return item * item
        intVal = int(self.opVal)
        if self.operator == '+':
            return item + intVal
        return item * intVal


main()