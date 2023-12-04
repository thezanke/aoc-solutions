import re
from typing import Any


def get_input(filename: str):
    with open(filename, "r") as file:
        data = file.read()
        groups = re.findall(
            r"^Card\s+(?P<row>\d+):\s+(?P<winning>(?:\s*\d+)+)\s\|\s+(?P<numbers>(?:\s*\d+)+).+$",
            data,
            flags=re.MULTILINE,
        )

        return groups
        # return re.finditer(r"Card\s+\d+:(\s+\d)+\s\|(\s+\d)+", data, flags=re.MULTILINE)


def get_numbers(string: str):
    return [int(x) for x in re.split(r"\s+", string)]


def part1(inpt: Any):
    scores: list[int] = []
    for row, winning, numbers in inpt:
        print("row " + row)
        winning = get_numbers(winning)
        print(winning)
        chances = get_numbers(numbers)
        print(chances)
        score = 0

        for winner in winning:
            if winner in chances:
                score = 1 if not score else score * 2

        print("score " + str(score))
        scores.append(score)
    return scores


def part2(inpt: Any):
    return 0


example1 = get_input("day4/example1.txt")

e1p1 = part1(example1)
print(sum(e1p1))


# e1p2 = part2(example1)
# print(e1p2)
# assert e1p2 == 0

# final_input = get_input("day4/final_input.txt")

# p1 = part1(final_input)
# print(p1)
# assert p1 == 0

# p2 = part2(final_input)
# print(p2)
# assert p2 == 0
