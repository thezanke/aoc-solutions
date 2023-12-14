import re
import sys
from typing import Any, List, Optional, Tuple
from common import expectation
from enum import Enum

debugging = False


from typing import Any, Optional, IO


def debug_log(
    *args: Any,
    sep: Optional[str] = " ",
    end: Optional[str] = "\n",
    file: Optional[IO[str]] = None,
    flush: bool = False,
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


class Category(Enum):
    SEED = 0
    SOIL = 1
    FERT = 2
    WATER = 3
    LIGHT = 4
    TEMP = 5
    HUMIDITY = 6
    LOCATION = 7


CATEGORIES = [
    Category.SEED,
    Category.SOIL,
    Category.FERT,
    Category.WATER,
    Category.LIGHT,
    Category.TEMP,
    Category.HUMIDITY,
    Category.LOCATION,
]

MapListEntry = tuple[int, int, int, int]
MapList = List[MapListEntry]

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

        return split(head[7:]), [sorted(x, key=lambda x: x[2]) for x in data]


def map_entry(entry: MapListEntry, mapper: MapListEntry) -> MapList:
    a1, a2, ab1, ab2 = entry
    b1, b2, bc1, _ = mapper
    delta = bc1 - b1

    if b1 <= ab1 and b2 >= ab2:  # completely contained
        return [(a1, a2, ab1 + delta, ab2 + delta)]

    parts: MapList = []
    if ab1 <= b1 <= ab2 or ab1 <= b2 <= ab2:  # overlapped
        # print(f"! {CATEGORIES[next_category]}{mapper}")
        d1 = b1 - ab1
        d2 = ab2 - b2
        l = d1 > 0
        r = d2 > 0

        if l:
            parts += [(a1, a1 - d1, ab1 - d1, ab2 - d2)]

        parts += [
            (
                a1 + d1 + 1 if l else a1,
                a2 - d2 if r else a2,
                (ab1 + d1 + 1 if l else ab1) + delta,
                (ab2 - d2 if r else ab2) + delta,
            )
        ]

        if r:
            parts += [(a2 - d2 + 1, a2, b2 + 1, ab2)]

    return parts


def upgrade_seed_map(
    input_list: MapList,
    almanac: Almanac,
    target_category: int = Category.LOCATION.value,
    next_category: int = Category.SOIL.value,
) -> MapList:
    print(f"\nINPUT (SEED-TO-{CATEGORIES[next_category].name}): {input_list}")
    next_map = almanac[next_category]
    print(f"NEXT({CATEGORIES[next_category]}): {next_map}")
    output_list: MapList = []
    for entry in input_list:
        # print(f"* entry: {entry}")

        parts: MapList = []

        for mapper in next_map:
            parts += map_entry(entry, mapper)

        if not len(parts):
            parts += [entry]

        # print(f"! MAPPED => {parts}")
        output_list += parts

    print(f"SEED-TO-{CATEGORIES[next_category+1].name}: {output_list}")

    if next_category < target_category:
        return upgrade_seed_map(
            output_list, almanac, target_category, next_category + 1
        )

    return output_list


def simplify_almanac(almanac: Almanac):
    seed_map = almanac[Category.SEED.value]
    print(almanac)
    # print(soil_map)
    # print(seed_map)

    seed_to_location: MapList = upgrade_seed_map(
        seed_map, almanac, Category.HUMIDITY.value
    )

    return seed_to_location


def part1(inpt: ParsedInput):
    seeds, almanac = inpt

    debug_log("almanac: %s" % almanac)
    debug_log("seeds: %r" % seeds)

    simple_almanac = simplify_almanac(almanac)
    lowest = sys.maxsize

    for num in seeds:
        debug_log("\nseed: %s" % num)

        for start, end, dest, _ in simple_almanac:
            if start <= num <= end:
                debug_log("  ! found %r in %r" % (num, (start, end, dest)))

                num = dest + num - start
                break

        if num < lowest:
            lowest = num

    debug_log("\nlowest: %s\n" % lowest)

    return lowest


def part2(inpt: ParsedInput):
    _, almanac = inpt
    almanac = simplify_almanac(almanac)

    return 0


# def generate_seed_to_location_map(almanac: Almanac):
#     seed_to_location: MapList = almanac[0].copy()

#     for dest_cat_id in range(1, len(CATEGORIES) - 1):
#         src_cat_id = dest_cat_id - 1

#         debug_log(
#             "%s %s -> %s %s"
#             % (
#                 src_cat_id,
#                 CATEGORIES[src_cat_id],
#                 dest_cat_id,
#                 CATEGORIES[dest_cat_id],
#             )
#         )

#         seed_to_location = convert_to_next_category(
#             seed_to_location,
#             almanac[dest_cat_id],
#         )

#     return seed_to_location


# def part2(inpt: ParsedInput):
#     timer_start = timer()

#     seeds, almanac = inpt
#     debug_log("almanac: %s" % almanac)
#     debug_log("seeds: %r" % seeds)

#     seed_to_location = generate_seed_to_location_map(almanac)
#     debug_log("seed_to_location: %r" % seed_to_location)

#     lowest = sys.maxsize
#     i = 0
#     chunks: list[list[int]] = chunk_list(seeds, 2)
#     total = sum(chunk[1] for chunk in chunks)

#     for start, size in chunks:
#         for num in range(start, start + size):
#             debug_log("\nseed: %s" % num)

#             for category in range(len(CATEGORIES) - 1):
#                 for start, end, dest, _ in almanac[category]:
#                     if start <= num <= end:
#                         debug_log("  ! found %r in %r" % (num, (start, end, dest)))

#                         num = dest + num - start
#                         break

#                 debug_log("  => %s %s" % (num, CATEGORIES[category + 1]))

#             if num < lowest:
#                 lowest = num

#             i += 1

#             elapsed = timer() - timer_start
#             if i % 1000 == 0:
#                 print(
#                     ("%.4f" % (i / total))
#                     + "% complete in "
#                     + ("%.1f" % elapsed)
#                     + " sec",
#                     end="\r",
#                 )

#     debug_log("\nlowest: %s\n" % lowest)

#     return lowest


def run():
    # example1 = get_input("day5/example1.txt")
    # final_input = get_input("day5/final_input.txt")

    expectation(
        "Day 5-1:   map_entry",
        [(98, 99, 35, 36)],
        map_entry,
        (98, 99, 50, 51),
        (15, 51, 0, 36),
    )
    expectation(
        "Day 5-1:   map_entry",
        [(50, 51, 37, 38), (52, 97, 54, 99)],
        map_entry,
        (50, 97, 52, 99),
        (52, 53, 37, 38),
    )
    expectation(
        "Day 5-1:   map_entry",
        [(52, 58, 50, 56), (59, 97, 61, 99)],
        map_entry,
        (52, 97, 54, 99),
        (53, 60, 49, 56),
    )
    # expectation("Day 5-1:   Example 1", 35, part1, example1)
    # expectation("Day 5-1: Final Input", 551761867, part1, final_input)
    # expectation("Day 5-2:   Example 1", 46, part2, example1)
    # expectation("Day 5-2: Final Input", 2, part2, final_input)


if __name__ == "__main__":
    run()
