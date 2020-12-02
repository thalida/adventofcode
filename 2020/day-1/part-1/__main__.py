# https://adventofcode.com/2020/day/1

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs

def process(inputs):
  inputs = inputs.copy()
  output = None

  for ia, a in enumerate(inputs):
    if output is not None:
      break

    for ib, b in enumerate(inputs):
      if ib == ia:
        continue

      num_a = int(a)
      num_b = int(b)

      if (num_a + num_b) == 2020:
        output = num_a * num_b
        break

  return output

inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)

assert answer == 1016619
