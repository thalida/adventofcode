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

    # standardize the input, replace space seperator with empty set
    line = line.replace('    ', '[]')
    # clean up all other spaces
    line = line.replace(' ', '')
    # convert to list of items
    row_items = line[1:-1].split('][')

    for (i, char) in enumerate(row_items):
      if i >= len(stacks):
        stacks.append([])

      if len(char) == 0:
        continue

      stacks[i] = stacks[i] + [char]

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
test_answer = process(test_inputs, in_reverse=True)
print(f'test answer:', test_answer)
assert test_answer == "CMZ"

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, in_reverse=True)
print(f'answer:', answer)
assert answer == "JDTMRWCQJ"
