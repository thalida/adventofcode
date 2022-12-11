import os
from pprint import pprint
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

def setup_monkeys(inputs):
  monkeys = []
  for line in inputs:
    if 'Monkey' in line:
      monkeys.append({
        'items': [],
        'num_inspections': 0,
        'operation': {'action': None, 'arg': None},
        'test': {
          'divisible_by': None,
          'if_true': None,
          'if_false': None,
        }
      })
      continue

    if 'Starting items:' in line:
      monkeys[-1]['items'] = list(map(lambda x: int(x), line.split(': ')[1].split(', ')))
      continue

    if 'Operation:' in line:
      formula = line.replace('Operation: new = old ', '')

      monkeys[-1]['operation']['action'] = formula.split()[0]

      arg = int(formula.split()[1]) if formula.split()[1] != 'old' else 'old'
      monkeys[-1]['operation']['arg'] = arg
      continue

    if 'Test:' in line:
      divisible_by = int(line.replace('Test: divisible by ', ''))
      monkeys[-1]['test']['divisible_by'] = divisible_by
      continue

    if 'If true:' in line:
      next_monkey = line.replace('If true: throw to monkey', '')
      monkeys[-1]['test']['if_true'] = int(next_monkey)
      continue

    if 'If false:' in line:
      next_monkey = line.replace('If false: throw to monkey', '')
      monkeys[-1]['test']['if_false'] = int(next_monkey)
      continue

  return monkeys


def process(inputs):
  monkeys = setup_monkeys(inputs)
  num_monkeys = len(monkeys)
  divisible_product = math.prod([monkey['test']['divisible_by'] for monkey in monkeys])
  round_num = 1
  max_rounds = 10000

  while round_num <= max_rounds:
    for i, monkey in enumerate(monkeys):
      num_items = len(monkey['items'])

      if num_items == 0:
        continue

      for worry_level in monkey['items']:
        arg = monkey['operation']['arg'] if monkey['operation']['arg'] != 'old' else worry_level

        if monkey['operation']['action'] == '+':
          worry_level += arg
        elif monkey['operation']['action'] == '*':
          worry_level *= arg

        # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
        worry_level %= divisible_product

        if worry_level % monkey['test']['divisible_by'] == 0:
          next_monkey = monkey['test']['if_true']
        else:
          next_monkey = monkey['test']['if_false']

        monkeys[next_monkey]['items'].append(worry_level)

      monkey['num_inspections'] += num_items
      monkey['items'] = []

    round_num += 1

  most_active = sorted(monkeys, key=lambda monkey: monkey['num_inspections'], reverse=True)[0:2]
  num_inspections_prod = most_active[0]['num_inspections'] * most_active[1]['num_inspections']

  return num_inspections_prod


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 2713310158

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 14106266886
