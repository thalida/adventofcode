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


def get_seat(input):
  rows = list(range(0, 128))
  seats = list(range(0, 8))

  for ch in input:
    row_middle = int(len(rows) / 2)
    seat_middle = int(len(seats) / 2)

    if ch == 'F':
      rows = rows[:row_middle]
    elif ch == 'B':
      rows = rows[row_middle:]
    elif ch == 'L':
      seats = seats[:seat_middle]
    elif ch == 'R':
      seats = seats[seat_middle:]

  return rows[0] * 8 + seats[0]

def process(inputs):
  seat_nums = []
  for input in inputs:
    seat_num = get_seat(input)
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
