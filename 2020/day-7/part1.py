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
        rules[key][bkey] = bcount

  return rules

def count_bags(rules, bags, find, parent=None):
  parent_bags = set()
  for bag in bags:
    contains = rules.get(bag, None)

    if contains is None:
      continue

    nested_bags = contains.keys()

    for nested_bag in nested_bags:
      if parent is not None:
        bag_parent = parent
      else:
        bag_parent = bag

      if nested_bag.find(find) >= 0:
        parent_bags.add(bag_parent)
      else:
        new_parents = count_bags(rules, [nested_bag], find, parent=bag_parent)
        parent_bags.update(new_parents)

  return parent_bags

def process(inputs):
  find = 'shiny gold bag'
  rules = make_rules_dict(inputs)
  bags_set = count_bags(rules, rules.keys(), find)
  count = len(bags_set)
  return count


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 4

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 144
