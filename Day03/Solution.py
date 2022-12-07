import urllib.request as Request

def main():
    lines = [l.strip() for l in open("./Day3/input.txt")]
    output = 0
    sets= []
    for line in lines:
        char = findOverlap(line)
        sets.append(set(line))
        output += charValLookup(char)
    total = findBadges(sets)
    print(total)
    print(output)



def findBadges(sets):
    compare = sets[0]
    total = 0
    for i in range(0, len(sets), 3):
        intersection = sets[i] & sets[i+1] & sets[i+2]
        for char in intersection:
            total += charValLookup(char)
    return total


def findOverlap(line):
    list1 = set()
    list2 = set()
    for i in range(len(line)//2):
        list1.add(line[i])
        list2.add(line[-(i+1)])
    
    for i in list1.intersection(list2):
        return i

def charValLookup(char):
    if char >= 'a':
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27


main()