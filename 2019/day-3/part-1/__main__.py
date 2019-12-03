# https://adventofcode.com/2019/day/3

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def get_points(wire):
  RIGHT = 'R'
  LEFT = 'L'
  UP = 'U'
  DOWN = 'D'

  points = []
  x = 0
  y = 0
  for move in wire:
    direction = move[0]
    amount = int(move[1:])

    new_x = x
    new_y = y

    for i in range(amount):
      if direction == RIGHT:
        new_x = new_x + 1
      elif direction == LEFT:
        new_x = new_x - 1
      elif direction == UP:
        new_y = new_y + 1
      elif direction == DOWN:
        new_y = new_y - 1

      points.append((new_x,new_y))
      # points.append(f'{new_x},{new_y}')

    x = new_x
    y = new_y

  return points

def intersection(inputs):
  inputs_copy = inputs.copy()
  wireA = inputs_copy[0].split(',')
  wireB = inputs_copy[1].split(',')

  wireA_points = get_points(wireA)
  wireB_points = get_points(wireB)
  intersections = list(set(wireA_points) & set(wireB_points))
  shortest_distance = None
  found_intersection = []

  for cross in intersections:
    x, y = cross
    distance = abs(int(x) - 0) + abs(int(y) - 0)
    if shortest_distance is None or distance <= shortest_distance:
      shortest_distance = distance
      found_intersection = cross

  print(shortest_distance)
  print(found_intersection)

  return inputs_copy

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = intersection(inputs)
  # print(f'answer:', answer)

main()
