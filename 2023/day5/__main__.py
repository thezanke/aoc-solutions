import re
import sys
from common import chunk_list, expectation
from timeit import default_timer as timer

debugging = False


def debug_log(*args: object):
    global debugging
    if debugging:
        print(*args)


CATEGORIES = [
    "seed",
    "soil",
    "fert",
    "water",
    "light",
    "temp",
    "humidity",
    "location",
]


def split(x: str):
    return [int(n) for n in re.split(r"\s+", x)]


def get_input(filename: str):
    with open(filename, "r") as file:
        data: list[list[tuple[int, int, int]]] = []
        head, *lines = file.read().splitlines()

        for line in lines:
            if not line.strip():
                continue

            if line.endswith(":"):
                data += [[]]
                continue

            dest, start, range_len = split(line)
            data[-1] += [(start, start + range_len - 1, dest)]

        return split(head[7:]), data


def part1(inpt: tuple[list[int], list[list[tuple[int, int, int]]]]):
    seeds, almanac = inpt
    debug_log("almanac: %s" % almanac)
    debug_log("seeds: %r" % seeds)

    lowest = sys.maxsize

    for num in seeds:
        debug_log("\nseed: %s" % num)

        for category in range(len(CATEGORIES) - 1):
            for start, end, dest in almanac[category]:
                if start <= num <= end:
                    debug_log("  ! found %r in %r" % (num, (start, end, dest)))

                    num = dest + num - start
                    break

            debug_log("  => %s %s" % (num, CATEGORIES[category + 1]))

        if num < lowest:
            lowest = num

    debug_log("\nlowest: %s\n" % lowest)

    return lowest


# New Idea.. what if I work backwards.... pre-cache the ranges from each category to the one before it;
# then, once we reach seed, it should be easier to determine the final value quickly. TBD..
def part2(inpt: tuple[list[int], list[list[tuple[int, int, int]]]]):
    global debugging

    timer_start = timer()

    seeds, almanac = inpt
    debug_log("almanac: %s" % almanac)
    debug_log("seeds: %r" % seeds)

    lowest = sys.maxsize
    i = 0
    chunks = chunk_list(seeds, 2)
    total = sum(chunk[1] for chunk in chunks)

    for start, size in chunks:
        for num in range(start, start + size):
            debug_log("\nseed: %s" % num)

            for category in range(len(CATEGORIES) - 1):
                for start, end, dest in almanac[category]:
                    if start <= num <= end:
                        debug_log("  ! found %r in %r" % (num, (start, end, dest)))

                        num = dest + num - start
                        break

                debug_log("  => %s %s" % (num, CATEGORIES[category + 1]))

            if num < lowest:
                lowest = num

            i += 1

            timer_end = timer()
            elapsed = timer_end - timer_start
            if i % 1000 == 0:
                print(
                    "%.4f" % (i / total) + "% complete in " + ("%.3f" % elapsed) + "s",
                    end="\r",
                )

    debug_log("\nlowest: %s\n" % lowest)

    return lowest


def run():
    example1 = get_input("day5/example1.txt")
    final_input = get_input("day5/final_input.txt")

    expectation("Day 5-1:   Example 1", 35, part1, example1)
    expectation("Day 5-1: Final Input", 551761867, part1, final_input)
    expectation("Day 5-2:   Example 1", 46, part2, example1)
    expectation("Day 5-2: Final Input", 2, part2, final_input)


if __name__ == "__main__":
    run()
