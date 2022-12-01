# https://adventofcode.com/2020/day/19

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

def validate_message(line, rules):

  paths = [[0, 0, 0]]
  path_starts = [0]
  message_idx = path_starts[-1]

  while message_idx < len(line):
    rule_id, subrule_idx, part_idx = paths[-1]

    if subrule_idx >= len(rules[rule_id]):
      paths.pop()
      path_starts.pop()

      if len(paths) == 0:
        return False

      message_idx = path_starts[-1]
      paths[-1][1] += 1
      paths[-1][2] = 0
      continue

    if part_idx >= len(rules[rule_id][subrule_idx]):
      paths.pop()
      path_starts.pop()

      if len(paths) == 0:
        return False

      paths[-1][2] += 1
      continue

    rule_val = rules[rule_id][subrule_idx][part_idx]
    if isinstance(rule_val, int):
      paths.append([rule_val, 0, 0])
      path_starts.append(message_idx)
      continue

    if line[message_idx] == rule_val:
      paths.pop()
      path_starts.pop()
      paths[-1][2] += 1
      message_idx += 1
      continue

    paths.pop()
    path_starts.pop()
    message_idx = path_starts[-1]
    paths[-1][1] += 1
    paths[-1][2] = 0

  return True

def process(inputs):
  rules = {}

  on_messages = False
  num_valid = 0

  for line in inputs:
    if len(line) == 0:
      on_messages = True
      continue

    if on_messages:
      if validate_message(line, rules):
        num_valid += 1
      continue

    idx, rule_strs = line.split(': ')
    idx = int(idx)
    rules[idx] = []
    for rule_str in rule_strs.split(' | '):
      if '"' in rule_str:
        rules[idx].append(rule_str.replace('"', ''))
        continue

      line_rules = [int(x) for x in rule_str.split(' ')]
      rules[idx].append(line_rules)

  return num_valid


test_inputs = get_inputs(filename='inputs_sample.txt')
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 2

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 176
