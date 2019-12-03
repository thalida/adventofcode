# https://adventofcode.com/2019/day/3

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def get_path(wire, x=0, y=0):
  RIGHT = 'R'
  LEFT = 'L'
  UP = 'U'
  DOWN = 'D'

  path = []

  for move in wire:
    direction = move[0]
    amount = int(move[1:])

    for i in range(amount):
      if direction == RIGHT:
        x += 1
      elif direction == LEFT:
        x -= 1
      elif direction == UP:
        y += 1
      elif direction == DOWN:
        y -= 1

      path.append((x,y))

  return path


def calc_distance(intersection):
  x, y = intersection
  return abs(int(x) - 0) + abs(int(y) - 0)

def calc_steps(intersection, path1, path2):
  path1_idx = path1.index(intersection) + 1
  path2_idx = path2.index(intersection) + 1
  return path1_idx + path2_idx

def analyse_wires(inputs):
  inputs_copy = inputs.copy()

  wire1 = inputs_copy[0].split(',')
  wire2 = inputs_copy[1].split(',')

  path1 = get_path(wire1)
  path2 = get_path(wire2)

  intersections = list(set(path1) & set(path2))

  results = {
    'shortest_distance': None,
    'shortest_distance_intersection': None,
    'shortest_steps': None,
    'shortest_steps_intersection': None,
  }

  for cross in intersections:
    distance = calc_distance(cross)
    steps = calc_steps(cross, path1, path2)

    if results['shortest_distance'] is None or distance <= results['shortest_distance']:
      results['shortest_distance'] = distance
      results['shortest_distance_intersection'] = cross

    if results['shortest_steps'] is None or steps <= results['shortest_steps']:
      results['shortest_steps'] = steps
      results['shortest_steps_intersection'] = cross

  return results

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = analyse_wires(inputs.copy())
  pprint(answer)

main()
