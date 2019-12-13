# https://adventofcode.com/2019/day/1
import os
os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from shared.intcode import Intcode
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

BLACK = 0
WHITE = 1
DEFAULT_COLOR = BLACK

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0]


def get_grid(program):

  TURN_LEFT_90 = 0
  TURN_RIGHT_90 = 1

  position = (0, 0)
  face = 'north'
  grid = {}
  panels_painted = []

  computer = Intcode(program, enable_exit_on_output=True)
  actions = []
  is_first_run = True

  while True:
    if position not in grid:
      grid[position] = DEFAULT_COLOR

    if is_first_run:
      grid[position] = WHITE
      is_first_run = False

    computer.run(input_val=grid[position])

    if computer.exit_code == computer.EXIT_CODES['EXIT']:
      break

    actions.append(computer.outputs[-1])

    if len(actions) < 2:
      continue

    grid[position] = actions[0]

    if position not in panels_painted:
      panels_painted.append(position)

    x, y = position

    if actions[1] == TURN_LEFT_90:
      if face == 'north':
        new_position = (x - 1, y)
        new_face = 'west'
      elif face == 'south':
        new_position = (x + 1, y)
        new_face = 'east'
      elif face == 'east':
        new_position = (x, y - 1)
        new_face = 'north'
      elif face == 'west':
        new_position = (x, y + 1)
        new_face = 'south'

    elif actions[1] == TURN_RIGHT_90:
      if face == 'north':
        new_position = (x + 1, y)
        new_face = 'east'
      elif face == 'south':
        new_position = (x - 1, y)
        new_face = 'west'
      elif face == 'east':
        new_position = (x, y + 1)
        new_face = 'south'
      elif face == 'west':
        new_position = (x, y - 1)
        new_face = 'north'

    position = new_position
    face = new_face
    actions = []

  return grid


def paint_grid(grid_obj):
  min_x = None
  min_y = None
  max_x = None
  max_y = None

  for x, y in grid_obj.keys():
    if min_x is None or x < min_x:
      min_x = x

    if min_y is None or y < min_y:
      min_y = y

    if max_x is None or x > max_x:
      max_x = x

    if max_y is None or y > max_y:
      max_y = y

  paint_grid = []
  for y in range(min_y, max_y+1):
    paint_grid.append([])
    for x in range(min_x, max_x+1):
      pos = (x, y)
      color_num = grid_obj.get(pos, DEFAULT_COLOR)
      color_sym = ' ' if color_num == BLACK else '#'
      paint_grid[-1].append(color_sym)
    print(''.join(paint_grid[-1]))

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  grid = get_grid(inputs)
  paint = paint_grid(grid)


main()
