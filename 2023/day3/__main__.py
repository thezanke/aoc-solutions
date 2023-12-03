import re


def get_input(filename: str):
    with open(filename, "r") as file:
        lines = file.read().split("\n")
        return len(lines[0]) + 1, "." + ".".join(lines)


def get_adjacent_positions(match: re.Match, line_len: int, inpt: str):
    adjacents = []

    start = match.start()
    end = match.end()

    start_of_line = start % line_len == 0
    end_of_line = end % line_len == 0

    if start >= line_len:
        start_above = start - line_len
        if not start_of_line:
            start_above -= 1

        end_above = end - line_len
        if not end_of_line:
            end_above += 1

        adjacents += range(start_above, end_above)

    if not start_of_line:
        adjacents.append(start - 1)

    if not end_of_line:
        adjacents.append(end)

    if len(inpt) - end >= line_len:
        start_below = start + line_len
        if not start_of_line:
            start_below -= 1

        end_below = end + line_len
        if not end_of_line:
            end_below += 1

        adjacents += range(start_below, end_below)

    return adjacents


def part1(line_len: int, inpt: str):
    part_nums = []

    for match in re.finditer(r"\d+", inpt):
        adj_sym = [
            inpt[pos]
            for pos in get_adjacent_positions(match, line_len, inpt)
            if not re.match(r"\d|\.", inpt[pos])
        ]

        if len(adj_sym) > 0:
            part_nums.append(int(match.group()))

    return sum(part_nums)


def part2(line_len: int, inpt: str):
    gear_positions = [match.start() for match in re.finditer(r"\*", inpt)]
    gears = {pos: [] for pos in gear_positions}

    for match in re.finditer(r"\d+", inpt):
        for pos in get_adjacent_positions(match, line_len, inpt):
            if pos in gear_positions:
                gears[pos].append(int(match.group()))

    return sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2])


example1 = get_input("day3/example1.txt")
assert part1(*example1) == 4361
assert part2(*example1) == 467835

final_input = get_input("day3/final_input.txt")
assert part1(*final_input) == 514969
assert part2(*final_input) == 78915902
