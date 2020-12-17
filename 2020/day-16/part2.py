# https://adventofcode.com/2020/day/16

import os
from pprint import pprint

import copy

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample_2.txt'


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
        notes['rules'][field].append([int(start), int(end)+1])

  return notes

def process(inputs):
  notes = parse_notes(inputs)
  overlapping_rules = {}

  for ticket in notes['nearby']:
    for i, num in enumerate(ticket):
      matching_rules = []

      for field, ranges in notes['rules'].items():
        if num in range(*ranges[0]) or num in range(*ranges[1]):
            matching_rules.append(field)

      # Stop processing this ticket if a number didn't have a matching rule
      if len(matching_rules) == 0:
        break

      # Have we processed this index before?
      if i not in overlapping_rules:
        overlapping_rules[i] = set(matching_rules)
      else:
        # get the intersection of the overlapping rules and the new matching rules
        overlapping_rules[i] = overlapping_rules[i] & set(matching_rules)


  found_rules = {}
  departure_multi = 1
  while len(overlapping_rules.keys()) > 0:
    for i, overlap in copy.deepcopy(overlapping_rules).items():
      if len(overlap) > 1:
        overlapping_rules[i] = overlap - set(found_rules.values())
        continue

      found_rules[i] = list(overlap)[0]
      del overlapping_rules[i]

      if 'departure' in found_rules[i]:
        departure_multi *= notes['yours'][i]

  return departure_multi

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 1265347500049
