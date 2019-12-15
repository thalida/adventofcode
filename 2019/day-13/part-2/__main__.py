# https://adventofcode.com/2019/day/1

import os
from pprint import pprint
import curses

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from shared.intcode import Intcode

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

TILES = {
  'EMPTY': 0,
  'WALL': 1,
  'BLOCK': 2,
  'HORIZONTAL_PADDLE': 3,
  'BALL': 4,
}
JOYSTICK = {
  'NEUTRAL': 0,
  'LEFT': -1,
  'RIGHT': 1,
}

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0]


def generate_game(instructions):
  game_score = 0
  game_tiles = []
  total_instructions = len(instructions)
  i = 0
  while i < total_instructions:
    x = instructions[i]
    y = instructions[i + 1]
    tile_type = instructions[i + 2]

    if (x, y) == (-1, 0):
      game_score = tile_type
      i += 3
      continue

    max_y = len(game_tiles)
    if y > max_y - 1:
      for new_y in range(max_y, y + 1):
        game_tiles.append([])

    max_x = len(game_tiles[y])
    if x > max_x - 1:
      for new_y in range(max_x, x + 1):
        game_tiles[y].append(TILES['EMPTY'])

    game_tiles[y][x] = tile_type
    i += 3

  return {
    'score': game_score,
    'tiles': game_tiles,
  }


def render_game(window, game):
  window.clear()
  window.addstr(0, 0, f'SCORE: {game["score"]}\n')

  for row in game['tiles']:
    row_str = ''
    for cell in row:
      if cell == TILES['EMPTY']:
        row_str += ' '
      elif cell == TILES['WALL']:
        row_str += '|'
      elif cell == TILES['BLOCK']:
        row_str += '█'
      elif cell == TILES['HORIZONTAL_PADDLE']:
        row_str += '⟙'
      elif cell == TILES['BALL']:
        row_str += 'O'

    window.addstr(row_str + '\n')
    window.refresh()


def main(window):
  window.keypad(True)
  program = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  computer = Intcode(program, enable_user_input=True)
  computer.write_value(0, 2)
  program_input = None
  while computer.exit_code != 'exit':
    computer.run(input_val=program_input)
    game = generate_game(computer.outputs)
    render_game(window, game)

    if computer.exit_code == 'input':
      user_input = window.getch()
      program_input = None
      if user_input == curses.KEY_LEFT:
        program_input = JOYSTICK['LEFT']
      elif user_input == curses.KEY_RIGHT:
        program_input = JOYSTICK['RIGHT']
      elif user_input == curses.KEY_ENTER:
        program_input = JOYSTICK['RIGHT']
      else:
        program_input = JOYSTICK['NEUTRAL']

curses.wrapper(main)
