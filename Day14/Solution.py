
def main():
    rockLocations,xBounds, yBounds = parse()
    print(sandyCave(rockLocations, xBounds, yBounds))
    

def sandyCave(rockLocation, xBounds, yBounds):
    totalSand = 0
    sandLocations = []
    while True:
        sand = fallingSand2(rockLocation, xBounds, yBounds)
        if sand == (500,0):
            totalSand +=1
            sandLocations.sort()
            return totalSand
        rockLocation.add(sand)
        sandLocations.append(sand)
        totalSand += 1


def fallingSand(rockLocation, xBounds, yBounds):
    falling = True
    sandOrigin = (500,0)
    sandLocation = sandOrigin
    while falling:
        falling = False
        for dx in [0,-1,1]:
            if (sandLocation[0]+dx, sandLocation[1]+1) not in rockLocation:
                falling = True
                sandLocation = (sandLocation[0]+dx, sandLocation[1]+1)
                if xBounds[0] > sandLocation[0] > xBounds[1] or sandLocation[1] > yBounds[1]:
                    return None
                break
    
    return sandLocation

def fallingSand2(rockLocation, xBounds, yBounds):
    falling = True
    sandOrigin = (500,0)
    sandLocation = sandOrigin
    while falling:
        falling = False
        for dx in [0,-1,1]:
            if (sandLocation[0]+dx, sandLocation[1]+1) not in rockLocation:
                falling = True
                sandLocation = (sandLocation[0]+dx, sandLocation[1]+1)
                
                if sandLocation[1] == (yBounds[1]+1):
                    falling = False
                break
    return sandLocation


def parse():
    lines = [l.strip() for l in open("./Day14/input.txt")]
    rockLocations = set()
    minX,maxX,minY,maxY = float('inf'),float('-inf'),float('inf'),float('-inf')
    
    for line in lines:
        coords = line.split('->')
        for i in range(1 ,len(coords)):
            coord = coords[i]
            pCoord = coords[i-1]
            fx,fy = intCoords(coord)
            ix,iy = intCoords(pCoord)
            minX,maxX,minY,maxY = calculateBounds(minX,maxX,minY,maxY,ix,iy,fx,fy)

            dx,dy = 0,0
            mag = 0
            if fx - ix == 0:
                dy = 1
                mag = abs(fy - iy)
                if fy < iy:
                    dy = -1
            else:
                dx = 1
                mag = abs(fx - ix)
                if fx < ix:
                    dx = -1

            tx,ty = ix,iy
            rockLocations.add((ix,iy))
            for _ in range(mag):
                ty += dy
                tx += dx
                rockLocations.add((tx, ty))
    
    return rockLocations,(minX,maxX),(minY,maxY)

def intCoords(coord):
    x,y = coord.split(',')
    return int(x), int(y)

def calculateBounds(minX,maxX,minY,maxY,ix,iy,fx,fy):

    maxX = max(maxX,ix,fx)
    maxY = max(maxY,iy,fy)
    minX = min(minX,ix,fx)
    minY = min(minY,iy,fy)
    return minX,maxX,minY,maxY

main()
        