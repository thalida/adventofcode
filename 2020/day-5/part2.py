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
  max_rows = 128
  start_row = 0
  end_row = max_rows

  seat_nums = []
  for input in inputs:
    seat_num = get_seat(input)
    seat_nums.append(seat_num)

  missing_seats = []
  found_seat = None
  for seat in seat_nums:
    prev_seat = seat - 1
    next_seat = seat + 1
    found_prev = prev_seat in seat_nums
    found_next = next_seat in seat_nums

    if found_prev and found_next:
      continue

    if not found_prev:
      if prev_seat in missing_seats:
        found_seat = prev_seat
        break

      missing_seats.append(prev_seat)

    if not found_next:
      if next_seat in missing_seats:
        found_seat = next_seat
        break

      missing_seats.append(next_seat)

  return found_seat


inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 603
