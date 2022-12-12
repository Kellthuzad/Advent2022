import heapq


def main():
    grid, startingPoint, destinationPoint = parse()
    print(dijkstras(grid, startingPoint, destinationPoint))

def dijkstras(grid, startingPoint, destinationPoint):
    visited = set()
    paths = []
    for point in startingPoint:
       paths.append((0, point))

    while paths:
        steps, position = heapq.heappop(paths)
        row,col = position
        if row == destinationPoint[0] and col == destinationPoint[1]:
            return steps
        if (row,col) in visited:
            continue
        visited.add((row,col))
        moves = findAvailableMoves(grid, (row,col))
        for move in moves:
            heapq.heappush(paths, (steps + 1, move))



    

def findAvailableMoves(grid, current):
    possibleMoves = []
    upMoves = []
    currentLevel = grid[current[0]][current[1]]
    row, col = current
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        if 0 <= (row + dr) < len(grid) and 0 <= (col + dc) < len(grid[0]):
            if grid[row +dr][col + dc] - currentLevel == 1:
                upMoves.append((row +dr, col + dc))
            elif grid[row +dr][col + dc] - currentLevel <= 0:
                possibleMoves.append((row +dr, col + dc))
    if upMoves:
        return upMoves
    return possibleMoves



def parse():
    lines = [l.strip() for l in open("./Day12/input.txt")]
    grid = []
    startingPoints = []
    destinationPoint = None
    for row in range(len(lines)):
        grid.append([])
        for col in range(len(lines[row])):
            if lines[row][col] == 'S':
                startingPoints.append((row, col))
                grid[row].append(0)
            elif lines[row][col] == 'E':
                destinationPoint = (row, col)
                grid[row].append(25)
            else:
                val = ord(lines[row][col]) - ord('a')
                grid[row].append(val)
                if val == 0:
                    startingPoints.append((row,col))
        

    return grid, startingPoints, destinationPoint

main()
        