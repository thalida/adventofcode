# https://adventofcode.com/2019/day/11
import os
os.sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from pprint import pprint
from shared.intcode import Intcode

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0]

def process(program):
  BLACK = 0
  WHITE = 1
  DEFAULT_COLOR = BLACK

  TURN_LEFT_90 = 0
  TURN_RIGHT_90 = 1

  position = (0, 0)
  face = 'north'
  grid = {}
  panels_painted = []

  computer = Intcode(program, enable_exit_on_output=True)
  actions = []

  while True:
    if position not in grid:
      grid[position] = DEFAULT_COLOR

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

  print(len(panels_painted), len(set(panels_painted)))
  print(len(grid.keys()))
  return

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(inputs)
  print(f'answer:', answer)

main()
