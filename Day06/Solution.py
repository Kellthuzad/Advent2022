import urllib.request as Request

def main():
    lines = parse()
    print(f'Part 1: {walk(lines[0], 4)}')
    print(f'Part 2: {walk(lines[0], 14)}')

def walk(line, subLength):
    for i in range(subLength,len(line),1):
        if checkSubstring(line[i-subLength:i]):
            return i

def checkSubstring(sub):
    chars = set(sub)
    return len(chars) == len(sub)

def parse():
    lines = [l.strip() for l in open("./Day6/input.txt")]
    return lines

main()