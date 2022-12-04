import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)


def process(inputs):
  num_overlapping = 0
  for i, claim in enumerate(inputs):
    ranges = claim.split(',')
    min_max_a = list(map(int, ranges[0].split('-')))
    min_max_b = list(map(int, ranges[1].split('-')))
    range_a = set(range(min_max_a[0], min_max_a[1] + 1))
    range_b = set(range(min_max_b[0], min_max_b[1] + 1))
    union = range_a.intersection(range_b)

    if len(union) > 0:
      if union == range_a or union == range_b:
        num_overlapping += 1

  return num_overlapping


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 2

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 532
