from common import expectation

GetInputResult = list[list[int]]


def get_input(filename: str) -> GetInputResult:
    with open(filename, "r") as file:
        return [[int(l) for l in line.split(" ")] for line in file.readlines()]


def iterate_group(inpt: list[int]):
    group = inpt.copy()
    yield group
    while True:
        group = [j - i for i, j in zip(group[:-1], group[1:])]
        yield group
        if all(n == 0 for n in group):
            break


def part1(inpt: GetInputResult):
    return sum(gg[-1] for g in inpt for gg in iterate_group(g))


def part2(inpt: GetInputResult):
    x = 0
    for g in inpt:
        gv = [g[0] for g in iterate_group(g)]
        y = gv[-1]
        for i in range(len(gv) - 1, 0, -1):
            y = gv[i - 1] - y
        x += y
    return x


def run():
    example = get_input("day9/example.txt")
    inpt = get_input("day9/input.txt")
    expectation("Day 9-1:   Example", 114, part1, example)
    expectation("Day 9-1:   Final", 2005352194, part1, inpt)
    expectation("Day 9-2:   Example", 2, part2, example)
    expectation("Day 9-2:   Final", 1077, part2, inpt)


if __name__ == "__main__":
    run()
