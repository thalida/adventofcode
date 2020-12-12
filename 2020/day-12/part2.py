# https://adventofcode.com/2020/day/12

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


def navigate(steps):
  waypoint_coords = {'x': 10, 'y': 1 }
  ship_coords = { 'x': 0, 'y': 0 }
  cardinals = ['N', 'E', 'S', 'W']
  coords_map = {'N': 'y', 'S': 'y', 'E': 'x', 'W': 'x'}

  for step in steps:
    action = step[0]
    amt = int(step[1:])

    if action == 'F':
      ship_coords['x'] += waypoint_coords['x'] * amt
      ship_coords['y'] += waypoint_coords['y'] * amt
      continue

    if action == 'R' or action == 'L':
      new_wp_coords = {'x': 0, 'y': 0}

      for coord, val in waypoint_coords.items():
        if coord == 'y':
          face = 'N' if val > 0 else 'S'
        else:
          face = 'E' if val > 0 else 'W'

        if action == 'R':
          face_idx = (cardinals.index(face) + int(amt / 90)) % 4
        elif action == 'L':
          face_idx = (cardinals.index(face) - int(amt / 90)) % 4

        new_face = cardinals[face_idx]
        new_coord = coords_map[new_face]
        new_val = abs(val)

        if new_face == 'S' or new_face == 'W':
          new_val = 0 - new_val

        new_wp_coords[new_coord] = new_val

      waypoint_coords = new_wp_coords
      continue

    if action == 'N':
      waypoint_coords['y'] += amt
    elif action == 'S':
      waypoint_coords['y'] -= amt
    elif action == 'E':
      waypoint_coords['x'] += amt
    elif action == 'W':
      waypoint_coords['x'] -= amt

  return ship_coords

def process(inputs):
  ship_coords = navigate(inputs)
  return abs(ship_coords['x']) + abs(ship_coords['y'])


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 286

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 89936
