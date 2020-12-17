# https://adventofcode.com/2020/day/16

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

def parse_notes(inputs):
  notes = {
    'rules': {},
    'yours': [],
    'nearby': []
  }

  handle_yours = False
  handle_nearby = False
  for line in inputs:
    if len(line) == 0:
      continue

    if 'your ticket' in line:
      handle_yours = True
      handle_nearby = False

    elif 'nearby tickets' in line:
      handle_yours = False
      handle_nearby = True

    elif handle_yours:
      notes['yours'] = [int(x) for x in line.split(',')]
      handle_yours = False

    elif handle_nearby:
      notes['nearby'].append([int(x) for x in line.split(',')])

    else:
      field, values = line.split(': ')
      notes['rules'][field] = []
      for range_str in values.split(' or '):
        start, end = range_str.split('-')
        notes['rules'][field].append([int(start), int(end) + 1])

  return notes

def process(inputs):
  notes = parse_notes(inputs)

  invalid_values = []
  for ticket in notes['nearby']:
    for num in ticket:
      invalid = True

      for ranges in notes['rules'].values():
        if num in range(*ranges[0]) or num in range(*ranges[1]):
          invalid = False
          break

      if invalid:
        invalid_values.append(num)

  return sum(invalid_values)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 71

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 25984
