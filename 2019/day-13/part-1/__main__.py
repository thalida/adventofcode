# https://adventofcode.com/2019/day/1

import os
from pprint import pprint

os.sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from shared.intcode import Intcode

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

TILE_TYPES = {
  'EMPTY': 0,
  'WALL': 1,
  'BLOCK': 2,
  'HORIZONTAL_PADDLE': 3,
  'BALL': 4,
}


def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0]


def get_instructions(program):
  computer = Intcode(program)
  computer.run()
  return computer.outputs


def generate_game_tiles(instructions):
  game_tiles = []
  tile_stats = {tile: 0 for tile in TILE_TYPES.values()}
  total_instructions = len(instructions)
  i = 0
  while i < total_instructions:
    x = instructions[i]
    y = instructions[i + 1]
    tile_type = instructions[i + 2]

    max_y = len(game_tiles)
    if y > max_y - 1:
      for new_y in range(max_y, y + 1):
        game_tiles.append([])

    max_x = len(game_tiles[y])
    if x > max_x - 1:
      for new_y in range(max_x, x + 1):
        game_tiles[y].append(TILE_TYPES['EMPTY'])

    game_tiles[y][x] = tile_type
    tile_stats[tile_type] += 1

    i += 3

  print(TILE_TYPES)
  pprint(tile_stats)

  return game_tiles


def render_game_tiles(game_tiles):
  for row in game_tiles:
    row_str = ''
    for cell in row:
      if cell == TILE_TYPES['EMPTY']:
        row_str += ' '
      elif cell == TILE_TYPES['WALL']:
        row_str += '|'
      elif cell == TILE_TYPES['BLOCK']:
        row_str += '█'
      elif cell == TILE_TYPES['HORIZONTAL_PADDLE']:
        row_str += '_'
      elif cell == TILE_TYPES['BALL']:
        row_str += 'o'
    print(row_str)


def main():
  program = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  instructions = get_instructions(program)
  game_tiles = generate_game_tiles(instructions)
  render_game_tiles(game_tiles)

main()
