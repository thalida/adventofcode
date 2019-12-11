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


def process(astroids):
  astroids = astroids.copy()
  astroid_visible_slopes = {}
  found_astroid = {'coords': None, 'num_slopes': None, }

  DEBUG = False
  log = [(5, 8)]

  for astroidA in astroids:
    x1, y1 = astroidA

    for astroidB in astroids:
      x2, y2 = astroidB
      if x1 == x2 and y1 == y2:
        continue

      dx = x2 - x1
      dy = y2 - y1

      if dx == 0:
        slope = 'v'
      elif dy == 0:
        slope = 'h'
      else:
        slope = dy / dx

      x_sign = '-' if dx < 0 else '+'
      y_sign = '-' if dy < 0 else '+'
      slope = f'{x_sign}{y_sign}{slope}'

      if astroidA in astroid_visible_slopes and slope in astroid_visible_slopes[astroidA]:
        continue

      if astroidA not in astroid_visible_slopes:
        astroid_visible_slopes[astroidA] = []

      astroid_visible_slopes[astroidA].append(slope)
      visible_slopes = len(astroid_visible_slopes[astroidA])

      if found_astroid['coords'] is None or visible_slopes > found_astroid['num_slopes']:
        found_astroid['coords'] = astroidA
        found_astroid['num_slopes'] = visible_slopes

  num_visible_slopes = {astroid: len(slopes) for astroid, slopes in astroid_visible_slopes.items()}
  # pprint(num_visible_slopes)
  return found_astroid

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  astroids = get_astrorid_coords(inputs)
  answer = process(astroids)
  print(f'answer:', answer)

main()
