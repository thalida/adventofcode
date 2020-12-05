# https://adventofcode.com/2020/day/4

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


valid_keys = [
  'byr', #(Birth Year)
  'iyr', #(Issue Year)
  'eyr', #(Expiration Year)
  'hgt', #(Height)
  'hcl', #(Hair Color)
  'ecl', #(Eye Color)
  'pid', #(Passport ID)
  'cid', #(Country ID)
]


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def process(inputs):
  valid_count = 0
  found_keys = []
  inputs = inputs + ['']

  for line in inputs:
    parts = line.split(' ')

    if len(line) == 0:
      if len(found_keys) > 0:
        missing_keys = list(set(valid_keys) - set(found_keys))
        if ((len(missing_keys) == 0) or
            (len(missing_keys) == 1 and missing_keys[0] == 'cid')):
          valid_count += 1

      found_keys = []
      continue

    for kv in parts:
      k = kv.split(':')[0]
      found_keys.append(k)

  return valid_count


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 4

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 182
