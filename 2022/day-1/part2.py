# https://adventofcode.com/2022/day/1

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def process(inputs):
  inputs.append('')
  groups = []
  numCals = 0
  for i, cal in enumerate(inputs):
    if cal == '':
      groups.append(numCals)
      numCals = 0
    else:
      numCals += int(cal)

  sorted_groups = sorted(groups)
  sorted_groups.reverse()

  return sum(sorted_groups[:3])


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 45000

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 211189
