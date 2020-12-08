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


def run_program(inputs, change=0):
  sum = 0
  curr_idx = 0
  visited_idxs = set()
  num_instructions = len(inputs)
  is_infinite = False

  while True:
    if curr_idx in visited_idxs:
      is_infinite = True
      break

    if curr_idx >= num_instructions:
      break

    parts = inputs[curr_idx].split(' ')
    op = parts[0]
    arg = int(parts[1])

    next_idx = curr_idx + 1

    if change == curr_idx:
      if op == 'nop':
        op = 'jmp'
      elif op == 'jmp':
        op = 'nop'

    if op == 'acc':
      sum += arg
    elif op == 'jmp':
      next_idx = curr_idx + arg

    visited_idxs.add(curr_idx)
    curr_idx = next_idx

  return sum, is_infinite


def process(inputs):
  outputs = inputs.copy()
  for i in range(len(inputs)):
    acc, is_infinite = run_program(inputs, change=i)
    if not is_infinite:
      return acc


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 8

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1260
