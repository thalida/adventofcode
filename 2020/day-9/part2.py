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


def find_contagion(inputs, contagion, i=0):
  error = False
  nums = []

  for x in inputs[i:]:
    contagion -= x
    if contagion < 0:
      error = True
      break

    if contagion == 0:
      break

    nums.append(x)

  return nums, error


def process(str_inputs, contagion):
  inputs = [int(str) for str in str_inputs]

  for i in range(len(inputs)):
    nums, error = find_contagion(inputs, contagion, i=i)
    if error is False:
      return min(nums) + max(nums)

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, contagion=127)
print(f'test answer:', test_answer)
assert test_answer == 62

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, contagion=1212510616)
print(f'answer:', answer)
assert answer == 171265123
