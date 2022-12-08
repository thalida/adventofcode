import os
from pprint import pprint
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

def get_tree_grid(inputs):
  grid = []
  for line in inputs:
    grid.append(list(map(int, list(line))))
  return grid

def calc_score(arr, h):
  score = 0

  for v in arr:
    score += 1
    if v >= h:
      break

  return score

def process(inputs):
  outputs = inputs.copy()
  grid = get_tree_grid(inputs)

  num_rows = len(grid)
  max_score = 0

  for (y, row) in enumerate(grid):
    if y == 0 or y == num_rows - 1:
      continue

    for (x, tree) in enumerate(row):
      if x == 0 or x == len(row) - 1:
        continue

      col = [grid[i][x] for i in range(num_rows)]

      top = col[:y]
      bottom = col[y+1:]

      left = row[:x]
      right = row[x+1:]

      # Put the trees in order from the current tree
      top.reverse()
      left.reverse()

      score = math.prod([
        calc_score(left, tree),
        calc_score(right, tree),
        calc_score(top, tree),
        calc_score(bottom, tree),
      ])
      max_score = max(max_score, score)

  return max_score

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 8

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 504000
