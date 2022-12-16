
def main():
    targetLine = 2000000
    sensorBeaconPairs, interference = parse(targetLine)
    # print(calculateSensorZone(sensorBeaconPairs, interference, targetLine))
    print(slicinAndDicin(sensorBeaconPairs))



def calculateSensorZone(sensorBeaconPairs, interference, targetLine):
    targetSet = set()
    for sensor, beacon in sensorBeaconPairs:
        dx = abs(sensor[0] - beacon[0])
        dy = abs(sensor[1] - beacon[1])
        distance = dx + dy
        populateTargetLine(sensor, distance, targetLine, targetSet, interference)
    return(len(targetSet))

def slicinAndDicin(pairs):

    for y in range(4000001):
        ranges = []
        for (sX, sY), (bX, bY) in pairs:
            distanceFromTargetLine = abs(y-sY)
            distance = abs(sX-bX) + abs(sY-bY)

            
            remainder = distance - distanceFromTargetLine
            if remainder < 0:
                continue

            ranges.append((sX - remainder, sX + remainder))
        ranges.sort()

        final = []
        currentMin, currentMax = ranges[0]
        for minX, maxX in ranges[1:]:
            if minX-1 <= currentMax:
                currentMax = max(currentMax, maxX)
            else:
                final.append((minX, maxX))
                currentMin, currentMax = minX, maxX
        final.append((currentMin, currentMax))

        if len(final) > 1:
            x = final[0][1]
            return x * 4000000 + y

def populateTargetLine(sensor, distance, targetLine, targetSet, interference):
    distanceFromTargetLine = abs(targetLine - sensor[1])
    if distanceFromTargetLine > distance:
        return
    
    remainder = distance - distanceFromTargetLine
    for i in range(sensor[0]-remainder, sensor[0]+remainder+1):
        if i not in interference:
            targetSet.add(i)


def parse(targetLine):
    lines = [l.strip() for l in open("./Day15/input.txt")]
    sensorBeaconPairs = []
    objectInterference = set()
    for line in lines:
        chunks = line.split()
        sX = int(chunks[2].strip(',').strip('x='))
        sY = int(chunks[3].strip(':').strip('y='))
        bX = int(chunks[8].strip(',').strip('x='))
        bY = int(chunks[9].strip(':').strip('y='))
        sensorBeaconPairs.append( ( (sX,sY),(bX,bY) ) )

        if sY == targetLine:
            objectInterference.add(sX)
        if bY == targetLine:
            objectInterference.add(bX)
    return sensorBeaconPairs, objectInterference

main()
        