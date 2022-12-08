import math

def main():
    trees = parse()

    print(visibleTrees(trees))
    print(scenicTrees(trees))

def visibleTrees(trees):
    answer = (len(trees) + len(trees[0])) * 2 - 4
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees)-1):
            if isVisible(row, col, trees):
                answer += 1
    return answer

def isVisible(y,x,trees):
    originalTree = trees[y][x]

    for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
        tempX = x + dx
        tempY = y + dy
        visible = True
        while 0 <= tempX < len(trees[0]) and 0 <= tempY < len(trees):
            if trees[tempY][tempX] >= originalTree:
                visible = False
                break
            tempX += dx
            tempY += dy
        if visible:
            return True
    
    return False

def scenicTrees(trees):
    answer = 0
    for row in range(1, len(trees)-1):
        for col in range(1, len(trees)-1):
            score = scenicScore(row, col, trees)
            answer = max(score, answer)
    return answer

def scenicScore(x,y, trees):
    originalTree = trees[y][x]
    directions = []
    for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
        tempX = x + dx
        tempY = y + dy
        total = 0
        while 0 <= tempX < len(trees[0]) and 0 <= tempY < len(trees):
            total += 1
            if trees[tempY][tempX] >= originalTree:
                break
            tempX += dx
            tempY += dy

        directions.append(total)
    
    return math.prod(directions)

def parse():
    lines = [l.strip() for l in open("./Day08/input.txt")]
    trees = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        trees.append(row)
    return trees

main()