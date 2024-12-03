import os

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)


def handle_report(report: str):
    rdir = 0
    vals = list(map(int, report.split(" ")))

    for idx in range(len(vals)):
        val = vals[idx]
        n = None if idx == len(vals) - 1 else vals[idx + 1]

        if n is not None:
            diff = n - val
            abs_diff = abs(n - val)

            if abs_diff == 0 or abs_diff > 3:
                return False

            dir = diff / abs_diff

            if rdir == 0:
                rdir = dir
            else:
                if rdir != dir:
                    return False

    return True


final = open(os.path.join(os.path.dirname(__file__), "input.txt")).read().split("\n")

if __name__ == "__main__":
    example_results = list(map(handle_report, example))
    assert example_results.count(True) == 2
    print("✔️  All tests passed")

    results = list(map(handle_report, final))
    print("Day 2 Part 1:", results.count(True))
