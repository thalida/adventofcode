# https://adventofcode.com/2020/day/1

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
TEST_INPUT_FILENAME = 'test_inputs.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def process(inputs):
  outputs = inputs.copy()
  return outputs


test_inputs = get_inputs(filename=TEST_INPUT_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == []

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == []
