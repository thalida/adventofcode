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


def get_grid(inputs):
  grid = []
  waypoints = {}

  start = ord('S')
  end = ord('E')

  for line in inputs:
    elevations = list(map(ord, list(line)))

    if start in elevations:
      waypoints['start'] = (len(grid), elevations.index(start))
      elevations[elevations.index(start)] = ord('a')

    if end in elevations:
      waypoints['end'] = (len(grid), elevations.index(end))
      elevations[elevations.index(end)] = ord('z')

    grid.append(elevations)

  return grid, waypoints


def get_neighbors(grid):
  neighbors = {}

  num_rows = len(grid)
  num_cols = len(grid[0])

  for x in range(0, num_rows):
    for y in range(0, num_cols):
      possible_moves = [
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
      ]

      neighbors[(x, y)]  = []

      for move in possible_moves:
        if move[0] < 0 or move[0] >= num_rows:
          continue

        if move[1] < 0 or move[1] >= num_cols:
          continue

        elevation = grid[move[0]][move[1]]
        if elevation > grid[x][y] + 1:
          continue

        neighbors[(x, y)].append(move)

  return neighbors


def search(start, end, neighbors):
  seen = set((start,))
  queue = [(start, 0)]

  while queue:
    pos, step = queue.pop(0)
    if pos == end:
      return step

    for neighbor in neighbors[pos]:
      if neighbor in seen:
        continue
      seen.add(neighbor)
      queue.append((neighbor, step + 1))


def process(inputs, debug=False):
  grid, waypoints = get_grid(inputs)
  neighbors = get_neighbors(grid)
  start = waypoints['start']
  end = waypoints['end']

  return search(start, end, neighbors)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, debug=False)
print(f'test answer:', test_answer)
assert test_answer == 31

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, debug=True)
print(f'answer:', answer)
assert answer == 420
