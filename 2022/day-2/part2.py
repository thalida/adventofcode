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
    'A': 1,
    'B': 2,
    'C': 3,
  }
  outcome_map = {
    'X': 0,
    'Y': 3,
    'Z': 6,
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

    score = outcome_map[b]

    if score == 0:
      my_move = win_map[their_move]
    elif score == 3:
      my_move = their_move
    elif score == 6:
      lose_map = {v: k for k, v in win_map.items()}
      my_move = lose_map[their_move]

    score += my_move

    outputs.append(score)

  return sum(outputs)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 12

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 13490
