# https://adventofcode.com/2020/day/11

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


def do_seats(rows, ruleOne):
  new_rows = []
  for y, cols in enumerate(rows):
    new_rows.append([])
    for x, col in enumerate(cols):
      new_rows[y].append(col)

      if col == '.':
        continue

      num_occupied = 0
      for dy in range(-1, 2):
        for dx in range(-1, 2):
          ax = x + dx
          ay = y + dy

          if x == ax and y == ay:
            continue

          if ay < 0 or ay >= len(rows):
            continue

          if ax < 0 or ax >= len(cols):
            continue

          if rows[ay][ax] == '#':
            num_occupied += 1

      if col == 'L' and num_occupied == 0:
        new_rows[y][x] = '#'

      elif col == '#' and num_occupied >= 4:
        new_rows[y][x] = 'L'

  return new_rows

def process(inputs):
  seats = []
  for row in inputs:
    seats.append(list(row))

  prev_occupied = -1
  num_occupied = 0
  ruleOne = False
  loop = 0
  while True:
    ruleOne = not ruleOne
    seats = do_seats(seats, ruleOne)
    prev_occupied = num_occupied
    num_occupied = 0
    for rows in seats:
      for col in rows:
        if col == '#':
          num_occupied += 1

    if num_occupied == prev_occupied:
      break

    loop += 1

  return num_occupied


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 37

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2183
