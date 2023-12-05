from common import expectation
from typing import Any
import re


def get_input(filename: str) -> list[tuple[int, str, str]]:
    with open(filename, "r") as file:
        data = file.read()
        groups = re.findall(
            r"^Card\s+(?P<row>\d+):\s+(?P<winning>.+)\s\|\s+(?P<numbers>.+)$",
            data,
            flags=re.MULTILINE,
        )

        return [(int(p), w, n) for p, w, n in groups]


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


def part2(inpts: list[tuple[int, str, str]]) -> int:
    class Card:
        n: int
        count = 1

        def __init__(self, n: int, w: str, n_str: str):
            self.n = n
            self.winning = get_numbers(w)
            self.numbers = get_numbers(n_str)

        def process(self):
            score = sum(winner in self.numbers for winner in self.winning)
            for num in range(self.n + 1, self.n + 1 + score):
                cards[num].count += self.count

    cards: dict[int, Card] = {int(p): Card(p, w, n) for p, w, n in inpts}
    [card.process() for card in cards.values()]

    return sum(card.count for card in cards.values())


def run():
    example1 = get_input("day4/example1.txt")
    final_input = get_input("day4/final_input.txt")

    expectation("Day 4-1:   Example 1", 13, part1, example1)
    expectation("Day 4-1: Final Input", 26914, part1, final_input)
    expectation("Day 4-2:   Example 1", 30, part2, example1)
    expectation("Day 4-2: Final Input", 13080971, part2, final_input)


if __name__ == "__main__":
    run()
