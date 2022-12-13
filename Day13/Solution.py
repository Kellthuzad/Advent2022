from functools import cmp_to_key
import math

def main():
    pairs = parse()
    print(comPAIRison(pairs))

    allPackets = [[[2]],[[6]]]
    for pair in pairs:
        allPackets.append(pair.left)
        allPackets.append(pair.right)
    allPackets = sorted(allPackets, key=cmp_to_key(lambda left,right: compare(left,right)), reverse=True)
    
    tracerPacketProd = 1
    for i,packet in enumerate(allPackets):
        if packet == [[2]] or packet == [[6]]:
            tracerPacketProd *= i+1
    print(tracerPacketProd)


def comPAIRison(pairs):
    score = 0

    for i in range(len(pairs)):
        val = compare(pairs[i].left, pairs[i].right)
        if val >= 0:
            score += (i +1)
    
    return score

def compare(left, right):
    if type(left) == int and type(right) == int:
            if left > right:
                return -1
            elif left < right:
                return 1
    elif type(left) == list and type(right) == list:
        i = 0
        while i < len(left) and i < len(right):
            val = compare(left[i], right[i])
            if val == -1:
                return -1
            if val == 1:
                return 1
            i += 1
        if i == len(left) and i < len(right):
            return 1
        elif i == len(right) and i < len(left):
            return -1
        else:
            return 0
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    else:
        return compare(left,[right])
    


def parse():
    lines = [l.strip() for l in open("./Day13/input.txt")]
    pairs = []
    for i in range(0,len(lines), 3):
        pairs.append(Pair(lines[i], lines[i+1]))
    return pairs


class Pair():
    def __init__(self, left, right):
        self.left = self.parse(left)
        self.right = self.parse(right)

    def parse(self, line):
        line = line[1:-1]
        outerList = []
        currentList = outerList
        listStack = [outerList]
        for s in line.split(','):
            tempNum = ''
            for c in s:
                if c == '[':
                    newList = []
                    currentList.append(newList)
                    listStack.append(currentList)
                    currentList = newList
                elif c == ']':
                    if tempNum != '':
                        currentList.append(int(tempNum))
                        tempNum = ''
                    currentList = listStack.pop()
                else:
                    tempNum += c
            if tempNum != '':
                currentList.append(int(tempNum))

        return outerList



main()