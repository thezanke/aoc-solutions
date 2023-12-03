from pprint import pprint


def get_input(filename: str):
    with open(filename, "r") as file:
        return file.read().split("\n")


def part1(input: str):
    bag = {"red": 12, "green": 13, "blue": 14}
    valid = []

    for i, game in enumerate(input):
        invalid = False

        for game_set in game.split("; "):
            for color_count in game_set.split(", "):
                n, color = color_count.split(" ")

                if bag[color] < int(n):
                    invalid = True
                    break

            if invalid:
                break

        if not invalid:
            valid.append(i + 1)

    return sum(valid)


example1 = get_input("day2/example1.txt")
print(part1(example1))

final_input = get_input("day2/final_input.txt")
print(part1(final_input))


def part2(input: str):
    powers = []

    for game in input:
        bag = {"red": 0, "green": 0, "blue": 0}

        for game_set in game.split("; "):
            for color_count in game_set.split(", "):
                n, color = color_count.split(" ")
                n = int(n)

                if n > bag[color]:
                    bag[color] = n

        powers.append(bag["red"] * bag["green"] * bag["blue"])

    return sum(powers)


example1 = get_input("day2/example1.txt")
print(part2(example1))

final_input = get_input("day2/final_input.txt")
print(part2(final_input))
