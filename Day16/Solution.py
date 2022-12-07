
def main():
    lines = parse()

    print(lines)

def parse():
    lines = [l.strip() for l in open("./Day6/input.txt")]
    return lines

main()
        