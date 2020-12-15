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


def process(inputs):
  start_nums = inputs[0].split(',')
  start_turn = len(start_nums)
  end_turn = 2020
  history = {}
  spoken_num = 0

  for i, num in enumerate(start_nums):
    num = int(num)
    history[num] = [i]
    spoken_num = num

  for turn in range(start_turn, end_turn):
    num_history = history[spoken_num]

    if len(num_history) <= 1:
      spoken_num = 0
    else:
      timebefore = num_history[-1]
      timebeforethat = num_history[-2]
      spoken_num = timebefore - timebeforethat

    if spoken_num not in history:
      history[spoken_num] = []

    history[spoken_num].append(turn)

    if len(history[spoken_num]) > 2:
      history[spoken_num].pop(0)

  return spoken_num


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 436

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 620
