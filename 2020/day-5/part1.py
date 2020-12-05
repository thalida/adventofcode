# https://adventofcode.com/2020/day/5

import os
from pprint import pprint
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def get_row(input, start, end):
  char = input[0]
  middle = (start + end) / 2
  if char == 'F':
    return get_row(input[1:], start, math.floor(middle))
  elif char == 'B':
    return get_row(input[1:], math.ceil(middle), end)
  else:
    return start, input


def get_seat(input, start, end):
  if len(input) == 0:
    return start

  char = input[0]
  middle = (start + end) / 2
  if char == 'L':
    return get_seat(input[1:], start, math.floor(middle))
  elif char == 'R':
    return get_seat(input[1:], math.ceil(middle), end)

def process(inputs):
  max_rows = 128
  start_row = 0
  end_row = max_rows

  seat_nums = []

  for input in inputs:
    row, seats = get_row(input, 0, 127)
    seat = get_seat(seats, 0, 7)
    seat_num = row * 8 + seat
    seat_nums.append(seat_num)

  return seat_nums


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == [357, 567, 119, 820]

inputs = get_inputs(filename=INPUT_FILENAME)
seats = process(inputs)
answer = max(seats)
print(f'answer:', answer)
assert answer == 987
