def main():
    lines = [l.strip() for l in open("./Day4/input.txt")]

    workerPairs = makeRanges(lines)

    count = findOverlap(workerPairs)
    count2 = findOverlap2(workerPairs)

    print(f'Part 1: {count}')
    print(f'Part 2: {count}')
        
def findOverlap(workerPairs):
    count = 0
    for pair in workerPairs:
        if pair[0] <= pair[1] or pair[0] <= pair[1]:
            count += 1
    return count

def findOverlap2(workerPairs):
    count = 0
    for pair in workerPairs:
        if len(pair[0].intersection(pair[1])) > 0:
            count += 1
    return count


def makeRanges(lines):
    workerPairs = []
    for line in lines:
        ranges = line.split(',')

        pair1 = ranges[0].split('-')
        pair2 = ranges[1].split('-')
        firstTuple = set([*range(int(pair1[0]), int(pair1[1])+1)])
        secondTuple = set([*range(int(pair2[0]), int(pair2[1])+1)])
        workerPairs.append((firstTuple, secondTuple))
    
    return workerPairs




main()