
def main():
    global root
    lines = parse()

    assembleDirectory(lines)
    rootsize = calculateSizes(root)
    calculateDirToDelete()
    print(answer)

def assembleDirectory(lines):
    i = 0
    while i < len(lines):
        if "$" in lines[i]:
            i = runCommand(lines[i], lines, i)

def runCommand(line, lines, i):
    global currentDirectory
    global root
    if "cd" in line:
        if "/" in line:
            currentDirectory = root
        elif ".." in line:
            currentDirectory = currentDirectory.parentDirectory
        else:
            targetDir = line.split()[2]
            if targetDir not in currentDirectory.files:
                currentDirectory.files[targetDir] = Directory(targetDir, currentDirectory)
            currentDirectory = currentDirectory.files[targetDir]
        i += 1
    else:
        i += 1
        while i < len(lines) and "$" not in lines[i]:
            fileData = lines[i].split()
            if "dir" in lines[i]:
                currentDirectory.files[fileData[1]] = Directory(fileData[1], currentDirectory)
            else:
                currentDirectory.files[fileData[1]] = int(fileData[0])
            i += 1

    
    return i

def calculateSizes(dir):
    global answer
    global sizes
    for _, val in dir.files.items():
        if isinstance(val, int):
            dir.size += val
        else:
            dir.size += calculateSizes(val)
    
    if dir.size < 100000:
        answer += dir.size

    sizes.append(dir.size)
    return dir.size

def calculateDirToDelete():
    totalDiskSpace = 70000000
    totalUnusedNeeded = 30000000
    totalAvailable = totalDiskSpace - root.size
    totalNeeded = totalUnusedNeeded - totalAvailable

    sizes.sort()
    for size in sizes:
        if size > totalNeeded:
            print(size)
            break



def parse():
    lines = [l.strip() for l in open("./Day07/input.txt")]
    return lines

class Directory:
    def __init__(self, name, pDir):
        self.name = name
        self.files = {}
        self.parentDirectory = pDir
        self.size = 0

root = Directory('/', None)
currentDirectory = root
answer = 0
sizes = []

main()
        