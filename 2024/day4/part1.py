import os

example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def count_occurance(data: str):
    h_lines = data.split("\n")
    width = len(h_lines[0])
    height = len(h_lines)

    max_y = height - 1

    v_lines: list[str] = []

    for i in range(width):
        line = ""
        for j in range(height):
            line += h_lines[j][i]
        v_lines.append(line)

    d_lines: list[str] = []

    for i in range(width):
        line = ""

        for y in range(0, i + 1):
            x = i - y
            line += h_lines[y][x]

        d_lines.append(line)

        line = ""

        for x in range(i + 1):
            y = max_y - i + x
            line += h_lines[y][x]
            print(line)

        d_lines.append(line)

        if not i:
            continue

        line = ""

        for y in range(max_y, i - 1, -1):
            x = max_y + i - y
            line += h_lines[y][x]

        d_lines.append(line)

        line = ""

        for x in range(i, width):
            y = x - i
            line += h_lines[y][x]
            print(line)

        d_lines.append(line)

    data = "\n".join(h_lines + v_lines + d_lines)

    return data.count("XMAS") + data.count("SAMX")


final = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()

if __name__ == "__main__":
    example_results = count_occurance(example)
    assert example_results == 18, "Expected %d, got %d" % (18, example_results)
    print("✔️  All tests passed")

    results = count_occurance(final)
    print("Day 4 Part 1:", results)
