# https://adventofcode.com/2022/day/2

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


def process(inputs):
  # 1 Rock
  # 2 Paper
  # 3 Scissors

  move_map = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
  }
  win_map = {
    1: 3,
    2: 1,
    3: 2,
  }

  outputs = []
  for i, input in enumerate(inputs):
    [a, b] = input.split(' ')

    their_move = move_map[a]
    my_move = move_map[b]

    score = my_move
    if my_move == their_move:
      score += 3
    elif win_map[my_move] == their_move:
      score += 6

    outputs.append(score)

  return sum(outputs)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 15

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 17189
