# https://adventofcode.com/2019/day/1

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
  outputs = inputs.copy()
  return outputs

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(inputs)
  print(f'answer:', answer)

main()
