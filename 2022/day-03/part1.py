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


def process(inputs):
  outputs = []
  for (i, line) in enumerate(inputs):
    line_len = int(len(line) / 2)
    comp1 = set(line[:line_len])
    comp2 = set(line[line_len:])
    intersection = comp1.intersection(comp2).pop()
    num = ord(intersection)

    if num > 96:
      num -= 96
    else:
      num -= 64 - 26

    outputs.append(num)

  return sum(outputs)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 157

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 8515
