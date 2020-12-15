# https://adventofcode.com/2020/day/15

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


def process(inputs, end_turn=30000000):
  start_nums = inputs[0].split(',')
  start_turn = len(start_nums)
  history = {}
  spoken_num = 0

  for i, num in enumerate(start_nums):
    num = int(num)
    history[num] = i
    spoken_num = num

  for turn in range(start_turn, end_turn):
    last_spoken = history.get(spoken_num)
    last_turn = turn - 1
    history[spoken_num] = last_turn

    if last_spoken is None:
      spoken_num = 0
    else:
      spoken_num = last_turn - last_spoken

  return spoken_num


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, end_turn=2020)
print(f'test answer:', test_answer)
assert test_answer == 436

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, end_turn=2020)
print(f'answer:', answer)
assert answer == 620

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, end_turn=30000000)
print(f'test answer:', test_answer)
assert test_answer == 175594

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, end_turn=30000000)
print(f'answer:', answer)
assert answer == 110871
