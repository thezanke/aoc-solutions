import re
from typing import Sequence

from part1 import example, final

def is_cross(data: Sequence[str], x: int, y: int):
    line_above = data[y - 1]
    line_below = data[y + 1]

    if line_above[x-1] == 'M':
        if line_below[x+1] != 'S':
            return False
    elif line_above[x-1] == 'S':
        if line_below[x+1] != 'M':
            return False
    else:
        return False
    
    if line_above[x+1] == 'M':
        if line_below[x-1] != 'S':
            return False
    elif line_above[x+1] == 'S':
        if line_below[x-1] != 'M':
            return False
    else:
        return 
    
    return True

def count_occurance(data: Sequence[str]):
    total = 0

    for y in range(1, len(data) - 1):
        line = data[y]
        
        for m in re.finditer("(?=.{1}A.{1})", line):
            x = m.start() + 1

            if is_cross(data, x, y):
                total += 1
    
        
    return total


if __name__ == "__main__":
    example_results = count_occurance(example.strip().split("\n"))
    assert example_results == 9, "Expected %d, got %d" % (9, example_results)
    print("✔️  All tests passed")

    results = count_occurance(final.strip().split("\n"))
    print("Day 4 Part 2:", results)
