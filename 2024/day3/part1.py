import os
import re

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
script_dir = os.path.dirname(__file__)
input_path = os.path.join(script_dir, "input.txt")
pattern = r"mul\((\d+),(\d+)\)"

def count_matches(input: str):
    matches = re.findall(pattern, input)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
        
    return result
  
final = open(os.path.join(os.path.dirname(__file__), "input.txt")).read()

if __name__ == '__main__':
  example_results = count_matches(example)
  assert example_results == 161, "Expected 161, got " + str(example_results)
  print("✔️  All tests passed")
  
  results = count_matches(final)
  print("Day 3 Part 1:", results)
  
  