from common import test
from typing import Any
import re


def get_input(filename: str):
    with open(filename, "r") as file:
        data = file.read()
        groups = re.findall(
            r"^Card\s+(?P<row>\d+):\s+(?P<winning>.+)\s\|\s+(?P<numbers>.+)$",
            data,
            flags=re.MULTILINE,
        )

        return groups


def get_numbers(string: str):
    return [int(x) for x in re.split(r"\s+", string)]


def part1(inpt: Any):
    scores: list[int] = []

    for _, winning, numbers in inpt:
        score = 0

        winning = get_numbers(winning)
        numbers = get_numbers(numbers)

        for winner in winning:
            if winner in numbers:
                score = 1 if not score else score * 2

        scores.append(score)

    return sum(scores)


def part2(inpt: Any):
    return 0


def run():
    example1 = get_input("day4/example1.txt")
    final_input = get_input("day4/final_input.txt")


    test("Day 4-1: Example 1", part1(example1), 13)
    test("Day 4-1: Final Input", part1(final_input), 26914)
    test("Day 4-2: Example 1", part2(example1), 0)
    test("Day 4-2: Final Input", part2(final_input), 0)

if __name__ == "__main__":
    run()