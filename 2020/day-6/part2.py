# https://adventofcode.com/2020/day/6

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
  inputs = inputs + ['']

  count = 0
  is_first = True
  overlap = set()
  for input in inputs:
    if len(input) == 0:
      count += len(overlap)
      overlap = set()
      is_first = True
      continue

    if is_first:
      overlap = set(list(input))
      is_first = False
    else:
      overlap = overlap & set(list(input))

  return count


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 6

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 3570
