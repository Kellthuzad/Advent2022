from pathlib import Path
import os

def main():
    for num in range(1, 27, 1):
        checkForDayAndMakeIfNeeded(num)


def checkForDayAndMakeIfNeeded(num):
    my_file = Path(f"./Day{num:02}")
    if not my_file.is_dir():
        os.mkdir(f"./Day{num:02}")
        f = open(f"./Day{num:02}/Solution.py", "w")
        f.write("""
def main():
    lines = parse()

    print(lines)

def parse():
    lines = [l.strip() for l in open("./Day/input.txt")]
    return lines

main()
        """)
        f.close()

        i = open(f"./Day{num:02}/input.txt", "a")
        i.write("hi paul")
        i.close()

main()