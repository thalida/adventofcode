# https://adventofcode.com/2020/day/7

import os
import re
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


def make_rules_dict(inputs):
  rules = {}
  for input in inputs:
    parts = input.split('contain')
    key = parts[0].strip()
    contains = parts[1].strip().split(', ')

    rules[key] = {}

    for bag in contains:
      matches = re.match(r"^([\d]*) ([a-z\s]*)", bag)

      if matches:
        bkey = matches.group(2)

        if bkey[-1] != 's':
          bkey = f'{bkey}s'

        bcount = matches.group(1)
        rules[key][bkey] = int(bcount)

  return rules


def count_nested_bags(rules, bag):
  counts = 0
  contains = rules.get(bag, None)
  for nested_bag, amount in contains.items():
    nested_count = count_nested_bags(rules, nested_bag)
    counts += amount + (amount * nested_count)

  return counts

def process(inputs):
  rules = make_rules_dict(inputs)
  count = count_nested_bags(rules, 'shiny gold bags')
  return count


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer_one = process(test_inputs)
print(f'test answer 1:', test_answer_one)
assert test_answer_one == 32

test_inputs = get_inputs(filename='inputs_sample_two.txt')
test_answer_two = process(test_inputs)
print(f'test answer 2:', test_answer_two)
assert test_answer_two == 126

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 5956
