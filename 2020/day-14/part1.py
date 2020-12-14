# https://adventofcode.com/2020/day/14

import os
from pprint import pprint

import re

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
  mask = "0" * 32
  memory = {}

  mask_re = r"^mask\s\=\s([0-1X]+)$"
  mem_re = r"^mem\[([0-9]+)\]\s\=\s([0-9]+)$"

  for line in inputs:
    mask_matches = re.match(mask_re, line)
    if mask_matches:
      mask = mask_matches.group(1)
      continue

    mem_matches = re.match(mem_re, line)
    addr = int(mem_matches.group(1))
    binary_val = f'{int(mem_matches.group(2)):b}'
    padded_binary = f"{'0' * (len(mask) - len(binary_val))}{binary_val}"

    masked_binary = list(padded_binary)
    for i in range(len(mask)):
      if mask[i] == 'X':
        continue

      if mask[i] != masked_binary[i]:
        masked_binary[i] = mask[i]

    memory[addr] = ''.join(masked_binary)

  sum = 0
  for val in memory.values():
    sum += int(val, 2)

  return sum


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 165

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 12408060320841
