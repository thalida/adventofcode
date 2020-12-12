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
  facing = 'E'
  coords = { 'N': 0, 'S': 0, 'E': 0, 'W': 0 }
  deg_map = { 'N': 0, 'E': 90, 'S': 180, 'W': 270 }

  for step in steps:
    action = step[0]
    amt = int(step[1:])

    if action == 'R' or action == 'L':
      if action == 'R':
        deg = deg_map[facing] + amt
      elif action == 'L':
        deg = deg_map[facing] - amt

      deg = deg % 360
      face_list = list(deg_map.keys())
      face_degs = list(deg_map.values())
      facing = face_list[face_degs.index(deg)]
      continue

    if action == 'F':
      action = facing

    if action == 'N':
      coords[action] += amt - coords['S']
      coords['S'] = 0
    elif action == 'S':
      coords[action] += amt - coords['N']
      coords['N'] = 0
    elif action == 'E':
      coords[action] += amt - coords['W']
      coords['W'] = 0
    elif action == 'W':
      coords[action] += amt - coords['E']
      coords['E'] = 0

  return coords

def process(inputs):
  coords = navigate(inputs)

  distance = 0
  for v in coords.values():
    distance += abs(v)

  return distance


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 25

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1838
