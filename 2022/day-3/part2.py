# https://adventofcode.com/2022/day/0

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
  outputs = []

  i = 0
  while i < len(inputs):
    line1 = set(inputs[i])
    line2 = set(inputs[i + 1])
    line3 = set(inputs[i + 2])
    intersection = line1.intersection(line2, line3).pop()
    num = ord(intersection)

    if num > 96:
      num -= 96
    else:
      num -= 64 - 26

    outputs.append(num)
    i += 3

  return sum(outputs)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 70

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2434
