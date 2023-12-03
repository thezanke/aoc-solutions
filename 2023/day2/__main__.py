def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().split("\n")


def coloriter(game: str):
    for game_set in game.split("; "):
        for color_count in game_set.split(", "):
            val_str, color = color_count.split(" ")
            yield int(val_str), color


def part1(input: list[str]):
    bag = {"red": 12, "green": 13, "blue": 14}
    valid: list[int] = []

    for i, game in enumerate(input):
        invalid = False

        for val, color in coloriter(game):
            if bag[color] < val:
                invalid = True
                break

        if not invalid:
            valid.append(i + 1)

    return sum(valid)


def part2(input: list[str]):
    powers: list[int] = []

    for game in input:
        bag = {"red": 0, "green": 0, "blue": 0}

        for val, color in coloriter(game):
            if val > bag[color]:
                bag[color] = val

        powers.append(bag["red"] * bag["green"] * bag["blue"])

    return sum(powers)


example1 = get_input("day2/example1.txt")
assert part1(example1) == 8
assert part2(example1) == 2286


final_input = get_input("day2/final_input.txt")
assert part1(final_input) == 2545
assert part2(final_input) == 78111
