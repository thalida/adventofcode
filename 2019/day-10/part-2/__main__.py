# https://adventofcode.com/2019/day/10

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


NODE_EMPTY = '.'
NODE_ASTROID = '#'


def get_astrorid_coords(map):
  astroid_coords = []
  for y, row in enumerate(map):
    for x, node in enumerate(list(row)):
      if node == NODE_EMPTY:
        continue
      astroid_coords.append((x,y))

  return astroid_coords


def group_astroids_by_slope(astroids):
  astroids = astroids.copy()
  astroids_by_slope = {}

  for astroidA in astroids:
    x1, y1 = astroidA

    for astroidB in astroids:
      x2, y2 = astroidB
      if x1 == x2 and y1 == y2:
        continue

      dx = x2 - x1
      dy = y2 - y1
      x_sign = '-' if dx < 0 else '+'
      y_sign = '-' if dy < 0 else '+'
      quad = (x_sign, y_sign)

      if dx != 0 and dy != 0:
        slope = dy / dx
        slope = f'{x_sign}{y_sign}{slope}'
      elif dx == 0:
        slope = 'up' if dy < 0 else 'down'
      elif dy == 0:
        slope = 'left' if dx < 0 else 'right'

      if astroidA not in astroids_by_slope:
        astroids_by_slope[astroidA] = {}

      if quad not in astroids_by_slope[astroidA]:
        astroids_by_slope[astroidA][quad] = {}

      if slope not in astroids_by_slope[astroidA][quad]:
        astroids_by_slope[astroidA][quad][slope] = []

      astroids_by_slope[astroidA][quad][slope].append(astroidB)

  return astroids_by_slope


def process(astroids_by_slope, find_deleted_at=200):
  astroids_by_slope = astroids_by_slope.copy()
  odd_slopes = ['up', 'right', 'down', 'left']
  num_deleted = 0
  astroid_found = None

  while True:
    if astroid_found is not None:
      break

    for quad in ['+-','++','-+', '--']:
      if astroid_found is not None:
        break

      quad_slopes = astroids_by_slope[(quad[0], quad[1])]
      ordered_quad_slopes = {float(slope.replace(quad, '')): val for slope, val in quad_slopes.items() if slope not in odd_slopes}
      ordered_keys = odd_slopes + list(sorted(ordered_quad_slopes.keys()))

      for key in ordered_keys:
        if key not in odd_slopes:
          key = f'{quad}{key}'

        if key not in quad_slopes:
          continue

        active_astroid = quad_slopes[key][-1]
        quad_slopes[key].pop()
        num_deleted += 1

        if num_deleted >= find_deleted_at:
          astroid_found = active_astroid
          break

  return astroid_found

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)

  astroids = get_astrorid_coords(inputs)
  astroids_by_slope = group_astroids_by_slope(astroids)
  chosen_astroid_slopes = astroids_by_slope[(20, 18)]
  answer = process(chosen_astroid_slopes)
  print(f'answer:', answer, (answer[0] * 100) + answer[1])

main()
