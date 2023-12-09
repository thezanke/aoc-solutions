from common import expectation

GetInputResult = list[list[int]]


def get_input(filename: str) -> GetInputResult:
    with open(filename, "r") as file:
        return [[int(l) for l in line.split(" ")] for line in file.readlines()]

def handle_group(group: list[int]) -> list[int]:
    print(group)
    while True:
        group = [j - i for i, j in zip(group[:-1], group[1:])]
        print(group)
        if all(n == 0 for n in group):
            return group


def part1(inpt: GetInputResult):
    for h in inpt:
        handle_group(h)

    return len(inpt)


def run():
    example1 = get_input("day9/example1.txt")
    expectation("Day 9-1:   Example 1", 114, part1, example1)


if __name__ == "__main__":
    run()
