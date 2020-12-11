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
  chain = set()

  if len(inputs) == 0:
    error = False
    return chain, error

  next_num = None
  error = False
  if curr + 1 in inputs:
    next_num = curr + 1

  elif curr + 2 in inputs:
    next_num = curr + 2

  elif curr + 3 in inputs:
    next_num = curr + 3

  if not next_num:
    error = True
    return chain, error

  chain.add(next_num)
  curr_idx = inputs.index(next_num)
  new_inputs = inputs.copy()
  del new_inputs[curr_idx]

  new_chain, error = get_chain(new_inputs, curr=next_num)

  if error:
    return chain, error

  chain.update(new_chain)

  return chain, False


def count_paths(chain):
  branches = {}
  max_value = max(chain)

  for i, x in enumerate(chain):
    if i == 0:
      branches[x] = 1

    if x not in branches:
      branches[x] = 0

    for j in range(1, i + 1):
      y = chain[i - j]

      if y - x > 3:
        break

      branches[x] += branches[y]

  return branches[0]


def process(str_inputs):
  inputs = [int(str) for str in str_inputs]
  chain, error = get_chain(inputs)
  chain = list(chain)
  chain.reverse()
  chain.append(0)
  paths = count_paths(chain)

  return paths


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 19208

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 3022415986688
