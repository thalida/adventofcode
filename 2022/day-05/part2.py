import os
from pprint import pprint
import re

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

def get_stacks(inputs):
  stacks = []

  for line in inputs:
    if '[' not in line:
      continue

    for (i, char) in enumerate(line[1::4]):
      if i >= len(stacks):
        stacks.append([])

      if len(char.strip()) == 0:
        continue

      stacks[i].append(char)

  return stacks

def process(inputs, in_reverse=False):
  output = []
  stacks = get_stacks(inputs)

  for line in inputs:
    if not line.startswith("move"):
      continue

    action = list(map(int, re.findall(r"move (\w+) from (\w+) to (\w+)", line)[0]))

    amount = action[0]
    from_idx = action[1] - 1
    to_idx = action[2] - 1

    items = stacks[from_idx][:amount]
    if in_reverse:
      items.reverse()

    stacks[from_idx] = stacks[from_idx][amount:]
    stacks[to_idx] = items + stacks[to_idx]

  for stack in stacks:
    output.append(stack[0])

  return ''.join(output)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, in_reverse=False)
print(f'test answer:', test_answer)
assert test_answer == "MCD"

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, in_reverse=False)
print(f'answer:', answer)
assert answer == "VHJDDCWRD"
