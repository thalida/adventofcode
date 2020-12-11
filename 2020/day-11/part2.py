# https://adventofcode.com/2020/day/11

import os
from pprint import pprint

import copy
import itertools

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs

def do_seats(rows):
  new_rows = copy.deepcopy(rows)
  new_occupied = 0

  directions = set(itertools.product(range(-1, 2), range(-1, 2)))

  for y, cols in enumerate(rows):
    for x, col in enumerate(cols):
      if col == '.':
        continue

      seen_directions = set([(0, 0)])
      loop = 0
      num_occupied = 0

      while len(seen_directions) < len(directions):
        loop += 1
        missing = directions - seen_directions

        for d in missing:
          dx, dy = d
          ax = x + (dx * loop)
          ay = y + (dy * loop)

          if ax < 0 or ax >= len(cols):
            seen_directions.add(d)
            continue

          if ay < 0 or ay >= len(rows):
            seen_directions.add(d)
            continue

          if rows[ay][ax] == '.':
            continue

          if rows[ay][ax] == '#':
            num_occupied += 1

          seen_directions.add(d)

      if col == 'L' and num_occupied == 0:
        new_rows[y][x] = '#'

      elif col == '#' and num_occupied >= 5:
        new_rows[y][x] = 'L'

      if new_rows[y][x] == '#':
        new_occupied += 1

  return new_rows, new_occupied


def process(inputs):
  seats = []
  for row in inputs:
    seats.append(list(row))

  prev_occupied = -1
  num_occupied = 0

  while True:
    prev_occupied = num_occupied
    seats, num_occupied = do_seats(seats)

    if num_occupied == prev_occupied:
      break

  return num_occupied


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 26

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1990
