from part1 import input_path

if __name__ == "__main__":
    k, m = [], {}

    with open(input_path) as f:
        for line in f:
            v1, v2 = line.rstrip().split("   ")
            k.append(v1)
            m[v2] = 1 if v2 not in m else m[v2] + 1

    total = 0

    for n in k:
        count = 0 if n not in m else m[n]
        total += int(n) * count

    print("Day 1 part 2:", total)
