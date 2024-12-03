import heapq
import os

script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, "input.txt")

if __name__ == "__main__":
    l1, l2 = [], []

    with open(input_path) as f:
        for line in f:
            v1, v2 = line.split("   ")
            heapq.heappush(l1, int(v1))
            heapq.heappush(l2, int(v2))

    total = 0
    while len(l1) > 0:
        v1 = heapq.heappop(l1)
        v2 = heapq.heappop(l2)
        total += abs(v1 - v2)

    print("Day 1 part 1:", total)
