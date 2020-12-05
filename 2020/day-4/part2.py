# https://adventofcode.com/2020/day/4

import os
from pprint import pprint
import re

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


valid_keys = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    'cid',  # (Country ID)
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
      v = kv.split(':')[1]

      is_valid = False
      if k == 'byr':
        is_valid = 1920 <= int(v) <= 2002
      elif k == 'iyr':
        is_valid = 2010 <= int(v) <= 2020
      elif k == 'eyr':
        is_valid = 2020 <= int(v) <= 2030
      elif k == 'hgt':
        if 'cm' in v:
          hgt = int(v.replace('cm', ''))
          is_valid = 150 <= hgt <= 193
        elif 'in' in v:
          hgt = int(v.replace('in', ''))
          is_valid = 59 <= hgt <= 76
      elif k == 'hcl':
        is_valid = bool(re.match(r'^\#[0-9a-f]{6}$', v))
      elif k == 'ecl':
        is_valid = v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
      elif k == 'pid':
        is_valid = bool(re.match(r'^[0-9]{9}$', v))
      elif k == 'cid':
        is_valid = True

      if is_valid is True:
        found_keys.append(k)

  return valid_count


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 4

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 109
