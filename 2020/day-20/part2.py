# https://adventofcode.com/2020/day/20

import copy
import math

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


def get_tile_edges(inputs):
  tiles = {}

  curr_tid = 0
  curr_ridx = 0
  max_row_idx = 9
  for line in inputs:
    if len(line) == 0:
      continue

    if 'Tile' in line:
      curr_tid = int(line.replace('Tile ', '').replace(':', ''))
      curr_ridx = 0
      tiles[curr_tid] = {
          'top': [], 'right': [], 'bottom': [], 'left': []
      }
      continue

    pixels = list(line)

    if curr_ridx == 0:
      tiles[curr_tid]['top'] = pixels
      tiles[curr_tid]['left'].append(pixels[0])
      tiles[curr_tid]['right'].append(pixels[-1])
    elif curr_ridx == max_row_idx:
      tiles[curr_tid]['bottom'] = pixels
      tiles[curr_tid]['left'].append(pixels[0])
      tiles[curr_tid]['right'].append(pixels[-1])
    else:
      tiles[curr_tid]['left'].append(pixels[0])
      tiles[curr_tid]['right'].append(pixels[-1])

    curr_ridx += 1

  return tiles


def get_seams(tiles):
  seams = {}
  tile_neighbors = {}

  for tile_id, tile in tiles.items():
    found_seams = tile_neighbors.get(tile_id, [])
    for side, pixels in tile.items():
      for check_tid, check_tile in tiles.items():
        if check_tid == tile_id or check_tid in found_seams:
          continue
        for check_side, check_pixels in check_tile.items():
          found_match = False

          reverse_pixels = copy.deepcopy(pixels)
          reverse_pixels.reverse()

          reverse_check = copy.deepcopy(check_pixels)
          reverse_check.reverse()

          if pixels == check_pixels:
            print((tile_id, check_tid), side, check_side, pixels, check_pixels)
            seams[(tile_id, check_tid)] = [side, check_side, False, False]
            found_match = True
          elif reverse_pixels == check_pixels:
            seams[(tile_id, check_tid)] = [side, check_side, True, False]
            found_match = True
          elif pixels == reverse_check:
            seams[(tile_id, check_tid)] = [side, check_side, False, True]
            found_match = True

          if found_match:
            if tile_id not in tile_neighbors:
              tile_neighbors[tile_id] = set()

            if check_tid not in tile_neighbors:
              tile_neighbors[check_tid] = set()

            tile_neighbors[tile_id].add(check_tid)
            tile_neighbors[check_tid].add(tile_id)

  return seams, tile_neighbors


def process(inputs):
  tiles = get_tile_edges(inputs)
  seams, neighbors_per_tile = get_seams(tiles)
  sq_size = int(math.sqrt(len(tiles)))
  chains = []

  print(tiles)
  print(seams)
  print(neighbors_per_tile)
  # for seam, orientation in seams.items():
  #   print(seam, orientation)

  corners = []
  borders = []
  for tile, neighbors in neighbors_per_tile.items():
    if len(neighbors) == 2:
      corners.append(tile)

  return answer


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 273

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 15003787688423
