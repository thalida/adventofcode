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


def slope_trees(rows, sx, sy):
  x = 0
  y = 0
  max_y = len(rows)
  max_x = len(rows[0])

  num_trees = 0

  for row in range(len(rows) - 1):
    y += sy
    x += sx
    x = x % max_x

    if y > max_y:
      break

    if rows[y][x] == '#':
      num_trees += 1

  return num_trees

def process(inputs):
  slopes = [
      slope_trees(inputs, 1, 1),
      slope_trees(inputs, 3, 1),
      slope_trees(inputs, 5, 1),
      slope_trees(inputs, 7, 1),
      slope_trees(inputs, 1, 2),
  ]

  slope_ans = 1
  for slope in slopes:
    slope_ans *= slope

  return slope_ans



test_inputs = get_inputs(filename=TEST_INPUT_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 336

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 4723283400
