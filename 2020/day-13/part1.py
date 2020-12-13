# https://adventofcode.com/2020/day/13

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
  start_time = int(inputs[0])
  time = start_time
  buses = inputs[1].split(',')
  found_bus = None

  while True:
    for bus in buses:
      if bus == 'x':
        continue

      bus = int(bus)
      if time % bus == 0:
        found_bus = bus
        break

    if found_bus is not None:
      break

    time += 1

  return (time - start_time) * bus


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 295

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 138
