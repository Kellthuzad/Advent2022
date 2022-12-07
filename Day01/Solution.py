def main():
    lines = [l.strip() for l in open("./Day1/input.txt")]
    numbers = []
    num = 0

    for line in lines:
        if line == '':
            numbers.append(num)
            num = 0
            continue
        tempnum = int(line)
        num += tempnum

    numbers.append(num)
    print(numbers)
    print(sum(sorted(numbers, reverse=True)[0:3]))

main()