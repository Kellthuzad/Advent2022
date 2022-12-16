from copy import deepcopy

def main():
    valves, nonZeroValves = parse()

    #print(dfs(valves['AA'], valves, nonZeroValves, set(), 0, 0))
    print(dfs2(valves['AA'], valves['AA'],valves, nonZeroValves, set(), 0, 0, 0)) 

def dfs(currentValve, valves, nonZeroValves, openedValves, minute, totalReleasedPressure):
    releasePressures = [totalReleasedPressure]
    if minute > 30:
        return 0
    for valve in nonZeroValves:
        if valve in openedValves:
            continue
        minutesToOpen = distanceFromValve(currentValve, valve, valves) +1
        totalReleasedPressure += ((30 - (minute +minutesToOpen)) * valves[valve].flowRate)
        minute += minutesToOpen
        openedValves.add(valve)
        releasePressures.append(dfs(valves[valve], valves, nonZeroValves, openedValves, minute, totalReleasedPressure))
        openedValves.remove(valve)
        minute -= minutesToOpen
        totalReleasedPressure -= ((30 - (minute +minutesToOpen)) * valves[valve].flowRate)

    
    return max(releasePressures)


def dfs2(currentValve1, currentValve2, valves, nonZeroValves, openedValves, minute1, minute2, totalReleasedPressure):
    releasePressures = [totalReleasedPressure]
    if minute1 > 26 or minute2 > 26:
        return 0
    for valve1 in nonZeroValves:
        if valve1 in openedValves:
            continue
        for valve2 in nonZeroValves:
            if valve2 in openedValves or valve1 == valve2:
                continue
            minutesToOpen1 = distanceFromValve(currentValve1, valve1, valves) +1
            minutesToOpen2 = distanceFromValve(currentValve2, valve2, valves) +1

            totalReleasedPressure += ((26 - (minute1 +minutesToOpen1)) * valves[valve1].flowRate)
            totalReleasedPressure += ((26 - (minute2 +minutesToOpen2)) * valves[valve2].flowRate)
            minute1 += minutesToOpen1
            minute2 += minutesToOpen2
            openedValves.add(valve1)
            openedValves.add(valve2)
            releasePressures.append(dfs2(valves[valve1], valves[valve2], valves, nonZeroValves, openedValves, minute1, minute2, totalReleasedPressure))
            openedValves.remove(valve1)
            openedValves.remove(valve2)
            minute1 -= minutesToOpen1
            minute2 -= minutesToOpen2
            totalReleasedPressure -= ((26 - (minute1 +minutesToOpen1)) * valves[valve1].flowRate)
            totalReleasedPressure -= ((26 - (minute2 +minutesToOpen2)) * valves[valve2].flowRate)

    
    return max(releasePressures)

# didnt get to use. sadge.
def greedy(valves):
    currentValve = valves['AA']
    openedValves = set()
    minute = 0
    totalReleasedPressure = 0

    while minute <= 30:
        highestValue = (0,'',0)
        for valveName, valve in valves.items():
            if valveName in openedValves or valve.flowRate == 0:   
                continue
            minutesTaken = distanceFromValve(currentValve, valveName, valves) +1
            if minutesTaken + minutesTaken > 30:
                continue
            pressureValue = (valve.flowRate * (30 - (minute + minutesTaken)))/minutesTaken
            #pressureValue = valve.flowRate/minutesTaken
            if pressureValue > highestValue[0]:
                highestValue = (pressureValue, valveName, minutesTaken)
        
        if highestValue[0] == 0:
            return totalReleasedPressure
        
        _, valveName, minutesTaken = highestValue
        totalReleasedPressure += ((30 - (minute +minutesTaken)) * valves[valveName].flowRate)
        minute += minutesTaken
        openedValves.add(valveName)
        currentValve = valves[valveName]

    return totalReleasedPressure 

            


def distanceFromValve(origin, destination, valves):
    queue = [(origin, 1)]
    visited = set()
    visited.add(origin.name)
    while queue:
        currentValve, distance = queue.pop(0)
        for valve in currentValve.valves:
            if valve in visited:
                continue
            if valve != destination:
                visited.add(valve)
                queue.append((valves[valve], distance+1))
            else:
                return distance
            

def parse():
    lines = [l.strip() for l in open("./Day16/input.txt")]
    valves = {}
    nonZeroValves = []
    for line in lines:
        chunks = line.split()
        flowRate = int(chunks[4].strip(';').strip('rate='))
        valves[chunks[1]] = Valve(chunks[1], flowRate, chunks[9:])
        if flowRate > 0:
            nonZeroValves.append(chunks[1])

    return valves, nonZeroValves

class Valve:
    def __init__(self, name, flowRate, sources):
        self.name = name
        self.flowRate = flowRate
        self.valves = []
        for source in sources:
            self.valves.append(source.strip(','))



main()
        