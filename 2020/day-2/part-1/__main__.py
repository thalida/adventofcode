# https://adventofcode.com/2020/day/2

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
  num_valid = 0

  for line in inputs:
    parts = line.split(': ')
    requirements = parts[0]
    password = parts[-1]

    req_parts = requirements.split(' ')
    letter = req_parts[-1]
    min_max = req_parts[0].split('-')
    min = int(min_max[0])
    max = int(min_max[1])

    letter_count = password.count(letter)

    if letter_count >= min and letter_count <= max:
      num_valid += 1

  return num_valid

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(inputs)
  print(f'answer:', answer)

main()
