import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

test_stack = [
  ["N", "Z"],
  ["D", "C", "M"],
  ["P"],
]

actual_stack = [
  ["P","D","Q","R","V","B","H","F"],
  ["V", "W", 'Q', 'Z', 'D', 'L'],
  ['C', 'P', 'R', 'G', 'Q', 'Z', 'L', 'H'],
  ['B', 'V', 'J', 'F', 'H', 'D', 'R'],
  ['C', 'L', 'W', 'Z'],
  ['M', 'V', 'G', 'T', 'N', 'P', 'R', 'J'],
  ['S', 'B', 'M', 'V', 'L', 'R', 'J'],
  ['J', 'P', 'D'],
  ['V', 'W', 'N', 'C', 'D'],
]

import re
def process(inputs, is_test=True):
  stacks = test_stack if is_test else actual_stack
  output = []

  for line in inputs:
    stack = []

    if not line.startswith("move"):
      continue

    action = list(map(int, re.findall(r"move (\w+) from (\w+) to (\w+)", line)[0]))

    from_idx = action[1] - 1
    to_idx = action[2] - 1

    items = stacks[from_idx][0:action[0]]
    # items.reverse()

    stacks[from_idx] = stacks[from_idx][action[0]:]
    stacks[to_idx] = items + stacks[to_idx]

  for stack in stacks:
    output.append(stack[0])

  return ''.join(output)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, is_test=True)
print(f'test answer:', test_answer)
assert test_answer == "MCD"

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, is_test=False)
print(f'answer:', answer)
assert answer == "VHJDDCWRD"
