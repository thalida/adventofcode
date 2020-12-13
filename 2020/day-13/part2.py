# https://adventofcode.com/2020/day/13

import os
from pprint import pprint


import sys

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
  bus_str = inputs.split(',')
  buses = []
  product = 1

  for i, bus in enumerate(bus_str):
    if bus == 'x':
      continue

    bus = int(bus)
    buses.append((i, bus))
    product *= bus

  time = 0
  for bus in buses:
    bus_idx, bus_num = bus
    rem = bus_num - bus_idx
    prod = product // bus_num
    mod_inv = pow(prod, -1, bus_num)

    time += rem * prod * mod_inv

  return time % product

assert sys.version_info >= (3, 8)

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs[1])
print(f'test answer 1:', test_answer)
assert test_answer == 1068781

test_answer = process('17,x,13,19')
print(f'test answer 2:', test_answer)
assert test_answer == 3417

test_answer = process('67,7,59,61')
print(f'test answer 3:', test_answer)
assert test_answer == 754018

test_answer = process('67,x,7,59,61')
print(f'test answer 4:', test_answer)
assert test_answer == 779210

test_answer = process('67,7,x,59,61')
print(f'test answer 5:', test_answer)
assert test_answer == 1261476

test_answer = process('1789,37,47,1889')
print(f'test answer 6:', test_answer)
assert test_answer == 1202161486

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs[1])
print(f'answer:', answer)
assert answer == 226845233210288
