from part1 import handle_report, example, final


def handle_report(report: str, omit_idx: int = None):
    rdir = 0
    vals = list(map(int, report.split(" ")))

    if omit_idx is not None:
        vals.pop(omit_idx)

    for idx in range(len(vals)):
        val = vals[idx]
        n = None if idx == len(vals) - 1 else vals[idx + 1]

        if n is not None:
            diff = n - val
            abs_diff = abs(n - val)

            if abs_diff == 0 or abs_diff > 3:
                return (
                    False
                    if omit_idx is not None
                    else handle_report(report, idx)
                    or handle_report(report, idx - 1)
                    or handle_report(report, idx + 1)
                )

            dir = diff / abs_diff

            if rdir == 0:
                rdir = dir
            else:
                if rdir != dir:
                    return (
                        False
                        if omit_idx is not None
                        else handle_report(report, idx)
                        or handle_report(report, idx - 1)
                        or handle_report(report, idx + 1)
                    )

    return True


if __name__ == "__main__":
    example_results = list(map(handle_report, example))
    assert example_results.count(True) == 4, "Expected 4, got " + str(
        example_results.count(True)
    )
    print("✔️  All tests passed")

    results = list(map(handle_report, final))
    print("Day 2 Part 2:", results.count(True))
