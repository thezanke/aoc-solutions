import re
import sys
from timeit import default_timer as timer
from typing import Any, List, Optional, Tuple
from common import chunk_list, expectation

debugging = False


from typing import Any, Optional, IO


def debug_log(
    *args: Any,
    sep: Optional[str] = " ",
    end: Optional[str] = "\n",
    file: Optional[IO[str]] = None,
    flush: bool = False
):
    global debugging

    if debugging:
        print(
            *args,
            sep=sep,
            end=end,
            file=file,
            flush=flush,
        )


CATEGORIES = ["seed", "soil", "fert", "water", "light", "temp", "humidity", "location"]

MapList = List[tuple[int, int, int, int]]

Almanac = List[MapList]
ParsedInput = Tuple[list[int], Almanac]


def split(x: str):
    return [int(n) for n in re.split(r"\s+", x)]


def get_input(filename: str) -> ParsedInput:
    with open(filename, "r") as file:
        data: list[MapList] = []
        head, *lines = file.read().splitlines()

        for line in lines:
            if not line.strip():
                continue

            if line.endswith(":"):
                data += [[]]
                continue

            dest, start, range_len = split(line)
            data[-1] += [(start, start + range_len - 1, dest, dest + range_len - 1)]

        return split(head[7:]), data


def part1(inpt: ParsedInput):
    seeds, almanac = inpt

    debug_log("almanac: %s" % almanac)
    debug_log("seeds: %r" % seeds)

    lowest = sys.maxsize

    for num in seeds:
        debug_log("\nseed: %s" % num)

        for category in range(len(CATEGORIES) - 1):
            for start, end, dest, _ in almanac[category]:
                if start <= num <= end:
                    debug_log("  ! found %r in %r" % (num, (start, end, dest)))

                    num = dest + num - start
                    break

            debug_log("  => %s %s" % (num, CATEGORIES[category + 1]))

        if num < lowest:
            lowest = num

    debug_log("\nlowest: %s\n" % lowest)

    return lowest


def convert_to_next_category(
    input_list: MapList,
    output_map: MapList,
):
    # output_list: MapList = []

    for inpt in input_list:
        debug_log(inpt)
        for outpt in output_map:
            overlaps = max(inpt[2], outpt[3]) <= min(inpt[1], outpt[1])
            if overlaps:
                debug_log(
                    "  ! found %r in %r" % ((inpt[2], inpt[3]), (outpt[0], outpt[1]))
                )

    return input_list


def generate_seed_to_location_map(almanac: Almanac):
    seed_to_location: MapList = almanac[0].copy()

    for dest_cat_id in range(1, len(CATEGORIES) - 1):
        src_cat_id = dest_cat_id - 1

        debug_log(
            "%s %s -> %s %s"
            % (
                src_cat_id,
                CATEGORIES[src_cat_id],
                dest_cat_id,
                CATEGORIES[dest_cat_id],
            )
        )

        seed_to_location = convert_to_next_category(
            seed_to_location,
            almanac[dest_cat_id],
        )

    return seed_to_location


def part2(inpt: ParsedInput):
    timer_start = timer()

    seeds, almanac = inpt
    debug_log("almanac: %s" % almanac)
    debug_log("seeds: %r" % seeds)

    seed_to_location = generate_seed_to_location_map(almanac)
    debug_log("seed_to_location: %r" % seed_to_location)

    lowest = sys.maxsize
    i = 0
    chunks: list[list[int]] = chunk_list(seeds, 2)
    total = sum(chunk[1] for chunk in chunks)

    for start, size in chunks:
        for num in range(start, start + size):
            debug_log("\nseed: %s" % num)

            for category in range(len(CATEGORIES) - 1):
                for start, end, dest, _ in almanac[category]:
                    if start <= num <= end:
                        debug_log("  ! found %r in %r" % (num, (start, end, dest)))

                        num = dest + num - start
                        break

                debug_log("  => %s %s" % (num, CATEGORIES[category + 1]))

            if num < lowest:
                lowest = num

            i += 1

            elapsed = timer() - timer_start
            if i % 1000 == 0:
                print(
                    ("%.4f" % (i / total))
                    + "% complete in "
                    + ("%.1f" % elapsed)
                    + " sec",
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
