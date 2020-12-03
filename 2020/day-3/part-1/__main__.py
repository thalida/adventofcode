# https://adventofcode.com/2020/day/3

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
TEST_INPUT_FILENAME = 'test_inputs.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def process(rows):
  x = 0
  y = 0
  max_y = len(rows)
  max_x = len(rows[0])

  num_trees = 0

  for row in range(len(rows) - 1):
    y += 1
    x += 3
    x = x % max_x

    if rows[y][x] == '#':
      num_trees += 1

  return num_trees


test_inputs = get_inputs(filename=TEST_INPUT_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 7

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 187
