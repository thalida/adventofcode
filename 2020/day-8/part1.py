# https://adventofcode.com/2020/day/8

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
  outputs = inputs.copy()
  sum = 0
  curr_idx = 0
  visited_idxs = set()
  num_instructions = len(inputs)

  while True:
    if curr_idx in visited_idxs:
      break

    parts = inputs[curr_idx].split(' ')
    op = parts[0]
    arg = int(parts[1])
    next_idx = curr_idx + 1

    if op == 'acc':
      sum += arg
    elif op == 'jmp':
      next_idx = curr_idx + arg

    visited_idxs.add(curr_idx)
    curr_idx = next_idx

  return sum


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 5

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1614
