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
  play_score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
  }
  play_type_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
  }
  outputs = []
  for i, input in enumerate(inputs):
    print(f'input {i}:', input)
    [y, m] = input.split(' ')
    score = play_score[m]
    if (play_type_map[y] == play_type_map[m]):
      score += 3
    elif (m == 'X' and y == 'C') or (m == 'Y' and y == 'A') or (m == 'Z' and y == 'B'):
      score += 6


    outputs.append(score)

  print(f'outputs:', outputs)
  return sum(outputs)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 15

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 17189
