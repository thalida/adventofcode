# https://adventofcode.com/2020/day/9

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


def process(str_inputs, preamble_len=5):
  inputs = [int(str) for str in str_inputs]
  preamble = inputs[:preamble_len + 1]
  odd_num = None
  for num in inputs[preamble_len:]:
    is_weird = True

    for x in preamble:
      y = num - x
      if y in preamble:
        is_weird = False
        break

    if is_weird:
      odd_num = num
      break

    preamble.pop(0)
    preamble.append(num)

  return odd_num


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 127

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, preamble_len=25)
print(f'answer:', answer)
assert answer == 1212510616
