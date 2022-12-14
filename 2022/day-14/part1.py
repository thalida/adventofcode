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

def get_paths(inputs):
  paths = []
  for line in inputs:
    line_paths = line.split(' -> ')
    paths.append([])
    for path in line_paths:
      paths[-1].append(list(map(int, path.split(','))))

  return paths


def get_rock_positions(paths):
  rock_positions = set()
  for path in paths:
    for i in range(1, len(path)):
      (x1, y1) = path[i-1]
      (x2, y2) = path[i]
      min_x = min(x1, x2)
      min_y = min(y1, y2)
      max_x = max(x1, x2)
      max_y = max(y1, y2)
      range_x = list(range(min_x, max_x+1))
      range_x.reverse()
      range_y = list(range(min_y, max_y+1))

      max_len = max(len(range_x), len(range_y))

      if len(range_x) == 1:
        range_x = range_x * max_len
      elif len(range_y) == 1:
        range_y = range_y * max_len

      new_points = set(zip(range_x, range_y))
      rock_positions |= new_points

  return rock_positions


def get_grid(start, rocks):
  grid = []
  xs = [x for x, y in rocks]
  ys = [y for x, y in rocks]
  min_x = min(xs + [start[0]])
  min_y = min(ys + [start[1]])
  max_x = max(xs)
  max_y = max(ys)

  num_rows = max_y - min_y + 1
  num_cols = max_x - min_x + 1

  for row in range(num_rows):
    grid.append([])
    for col in range(num_cols):
      if (col + min_x, row + min_y) in rocks:
        grid[-1].append('#')
      else:
        grid[-1].append('.')

  return grid, (start[0] - min_x, start[1] - min_y)


def print_grid(grid, start_pos):
  for x, row in enumerate(grid):
    row_str = ''.join(row)
    if x == start_pos[1]:
      row_str = row_str[:start_pos[0]] + '+' + row_str[start_pos[0]+1:]
    print(row_str)


def is_filled(grid, pos):
  x, y = pos
  return grid[y][x] == '#' or grid[y][x] == 'o'


def process(inputs):
  start = [500, 0]
  paths = get_paths(inputs)
  rocks = get_rock_positions(paths)
  grid, start_pos = get_grid(start, rocks)

  num_cols = len(grid[0])
  num_rows = len(grid)

  num_sand = 0
  found_void = False
  pos = start_pos
  while not found_void:
    x, y = pos

    found_void = x - 1 < 0 or x + 1 >= num_cols or y + 1 >= num_rows
    if found_void:
      break

    can_move_down = not is_filled(grid, (x, y + 1))
    can_move_left_diag = not is_filled(grid, (x - 1, y + 1))
    can_move_right_diag = not is_filled(grid, (x + 1, y + 1))

    if not can_move_down and not can_move_left_diag and not can_move_right_diag:
      grid[y][x] = 'o'
      num_sand += 1
      pos = start_pos
      continue

    if can_move_down:
      pos = (x, y + 1)
    elif can_move_left_diag:
      pos = (x - 1, y + 1)
    elif can_move_right_diag:
      pos = (x + 1, y + 1)


  return num_sand


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 24

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 888
