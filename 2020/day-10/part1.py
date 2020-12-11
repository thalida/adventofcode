# https://adventofcode.com/2020/day/10

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


def get_chain(inputs, curr=0):

  jolts = {
    1: set(),
    2: set(),
    3: set()
  }

  if len(inputs) == 0:
    error = False
    return jolts, error

  found = None
  error = False
  if curr + 1 in inputs:
    jolts[1].add(curr + 1)
    found = curr + 1

  elif curr + 2 in inputs:
    jolts[2].add(curr + 2)
    found = curr + 2

  elif curr + 3 in inputs:
    jolts[3].add(curr + 3)
    found = curr + 3

  if not found:
    error = True
    return jolts, error

  curr_idx = inputs.index(found)
  new_inputs = inputs.copy()
  del new_inputs[curr_idx]

  new_jolts, error = get_chain(new_inputs, curr=found)

  if error:
    return jolts, error

  jolts[1].update(new_jolts[1])
  jolts[2].update(new_jolts[2])
  jolts[3].update(new_jolts[3])

  return jolts, False


def process(str_inputs):
  inputs = [int(str) for str in str_inputs]
  jolts, error = get_chain(inputs)

  return len(jolts[1]) * (len(jolts[3]) + 1)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 22 * 10

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2112
