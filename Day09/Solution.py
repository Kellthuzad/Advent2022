
def main():
    lines = parse()
    snake = []
    tailHistory.add((0,0))

    # if you want part 1, set this to 2
    chunks = 10
    for _ in range(chunks):
        snake.append((0,0))

    for line in lines:
        direction, magnitude = line.split()
        mag = int(magnitude)
        moveHead(direction, mag, snake)
    print(len(tailHistory))

tailHistory = set()
 
def moveHead(direction, magnitude, snake):
    delta = (0,0)

    if direction == 'U':
        delta = (0,1)
    elif direction == 'D':
        delta = (0,-1)
    elif direction == 'R':
        delta = (1,0)
    elif direction == 'L':
        delta = (-1,0)

    for i in range(magnitude):
        snake[0] = (snake[0][0] + delta[0], snake[0][1] + delta[1])
        moveTail(snake, 0, delta)


def moveTail(snake, i, delta):
    global tailHistory
    if abs(snake[i][0] - snake[i+1][0]) > 1 or abs(snake[i][1] - snake[i+1][1]) > 1:
        dx = computeDelta(snake[i][0], snake[i+1][0])
        dy = computeDelta(snake[i][1], snake[i+1][1])

        snake[i+1] = (snake[i+1][0] + dx, snake[i+1][1] + dy)
        
        if i+1 == len(snake) - 1:
            tailHistory.add(snake[i+1])
        else:
            moveTail(snake, i+1, delta)

def computeDelta(head, tail):
    if head > tail:
        return 1
    elif head == tail:
        return 0
    else:
        return -1



def parse():
    lines = [l.strip() for l in open("./Day09/input.txt")]
    return lines

main()