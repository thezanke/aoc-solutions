import re

from part1 import count_matches, final

DO_SPLITTER = r"do\(\)"
DONT_SPLITTER = r"don\'t\(\)"

example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def solve(data: str):
    total = 0
    reading = True

    while len(data) > 0:
        if not reading:
            match = re.search(DO_SPLITTER, data)
            data = data[match.end() :] if match else ""
            reading = True
            continue

        match = re.search(DONT_SPLITTER, data)
        total += count_matches(data[: match.start()] if match else data)
        data = data[match.end() :] if match else ""
        reading = False

    return total


if __name__ == "__main__":
    example_results = solve(example)
    assert example_results == 48, "Expected 48, got " + str(example_results)
    print("✔️  All tests passed")

    results = solve(final)
    print("Day 3 Part 2:", results)
