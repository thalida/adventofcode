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

def get_tree_grid(inputs):
  grid = []
  for line in inputs:
    grid.append(list(map(int, list(line))))

  return grid

def process(inputs):
  grid = get_tree_grid(inputs)

  num_rows = len(grid)
  num_visible_trees = 0
  for (y, row) in enumerate(grid):
    if y == 0 or y == num_rows - 1:
      num_visible_trees += len(row)
      continue

    for (x, tree) in enumerate(row):
      if x == 0 or x == len(row) - 1:
        num_visible_trees += 1
        continue

      col = [grid[i][x] for i in range(num_rows)]
      shortest_dir = min([
        max(col[:y]),
        max(col[y+1:]),
        max(row[:x]),
        max(row[x+1:]),
      ])

      if shortest_dir < tree:
        num_visible_trees += 1

  return num_visible_trees


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 21

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1708
