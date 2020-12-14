# https://adventofcode.com/2020/day/14

import os
from pprint import pprint

import re
import itertools

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
    addr = f'{int(mem_matches.group(1)):b}'
    padded_addr = f"{'0' * (len(mask) - len(addr))}{addr}"
    val = int(mem_matches.group(2))

    masked_addr = list(padded_addr)
    num_floating = 0
    for i in range(len(mask)):
      if mask[i] == '0':
        continue

      if mask[i] == 'X':
        num_floating += 1

      masked_addr[i] = mask[i]
    masked_addr = ''.join(masked_addr)

    if num_floating == 0:
      memory[masked_addr] = val
      continue

    addrs = []
    permutations = list(itertools.product(['0', '1'], repeat=num_floating))
    for perm in permutations:
      addr_str = masked_addr

      for bit in perm:
        addr_str = addr_str.replace('X', bit, 1)

      addrs.append(addr_str)

    for addr in addrs:
      memory[addr] = val

  sum = 0
  for val in memory.values():
    sum += val

  return sum


test_inputs = get_inputs(filename='inputs_sample_2.txt')
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 208

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 4466434626828
