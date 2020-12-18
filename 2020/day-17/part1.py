# https://adventofcode.com/2020/day/17

import os
from pprint import pprint

import copy

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def count_active_neighbors(x, y, z, cube_states):
  num_active_neighbors = 0

  for dz in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      for dx in [-1, 0, 1]:
        if dx == 0 and dy == 0 and dz == 0:
          continue

        nx = x + dx
        ny = y + dy
        nz = z + dz

        if cube_states.get((nx, ny, nz), False):
          num_active_neighbors += 1

  return num_active_neighbors


def process(inputs):
  cube_states = {}

  for y, row in enumerate(inputs):
    for x, cube in enumerate(list(row)):
      if cube == '#':
        cube_states[(x, y, 0)] = True

  num_cycles = 6
  cycle = 0
  while cycle < num_cycles:
    cube_states_copy = copy.deepcopy(cube_states)

    for coords in cube_states.keys():
      x, y, z = coords

      for cz in range(z-1, z+2):
        for cy in range(y-1, y+2):
          for cx in range(x-1, x+2):
            is_active = cube_states.get((cx, cy, cz), False)
            num_active_neighbors = count_active_neighbors(
                cx, cy, cz, cube_states)

            if is_active and num_active_neighbors not in [2, 3]:
              if (cx, cy, cz) in cube_states_copy:
                del cube_states_copy[(cx, cy, cz)]

            elif not is_active and num_active_neighbors == 3:
              cube_states_copy[(cx, cy, cz)] = True

    cube_states = copy.deepcopy(cube_states_copy)
    cycle += 1

  return len(cube_states)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 112

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 424
