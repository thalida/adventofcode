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


def validate_message(line, rules, print_message='aaaabbaaaabbaaa'):
  paths = [[0, 0, 0]]
  built_message = []

  while len(built_message) < len(line):
    message_idx = len(built_message)
    rule_id, subrule_idx, part_idx = paths[-1]

    if subrule_idx >= len(rules[rule_id]):
      prev_path = paths[-1]
      paths.pop()

      if len(built_message) > 0:
        built_message.pop()

      if len(paths) == 0:
        print(prev_path)
        print(line, subrule_idx, len(rules[rule_id]))
        print(''.join(built_message), paths)
        return False

      paths[-1][1] += 1
      paths[-1][2] = 0
      continue

    if part_idx >= len(rules[rule_id][subrule_idx]):
      paths.pop()

      if len(paths) == 0:
        return False

      paths[-1][2] += 1
      continue

    # if line == print_message:
    #   spacer = '|    '*(len(paths)-1) + '|___'
    #   spacer = '\033[94m' + spacer + '\033[0m'
    #   print(spacer, message_idx, line[message_idx], ''.join(built_message))
    #   print(spacer, rule_id, subrule_idx, part_idx)
    #   print(spacer, rules[rule_id])
    #   print()

    was_valid = False
    rule_val = rules[rule_id][subrule_idx][part_idx]

    if isinstance(rule_val, int):
      paths.append([rule_val, 0, 0])
      continue

    if line[message_idx] == rule_val:
      built_message.append(line[message_idx])
      paths[-1][2] += 1
      continue

    # if len(built_message) > 0:
    #   print('before:', ''.join(built_message))
    #   built_message.pop()
    #   print('after:', ''.join(built_message))

    paths.pop()
    paths[-1][1] += 1
    paths[-1][2] = 0

  print(''.join(built_message), line, ''.join(built_message) == line)
  print(len(built_message), len(line))

  return True


def process(inputs):
  rules = {}

  on_messages = False
  num_valid = 0

  test_matches = [
      "bbabbbbaabaabba",
      "babbbbaabbbbbabbbbbbaabaaabaaa",
      "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
      "bbbbbbbaaaabbbbaaabbabaaa",
      "bbbababbbbaaaaaaaabbababaaababaabab",
      "ababaaaaaabaaab",
      "ababaaaaabbbaba",
      "baabbaaaabbaaaababbaababb",
      "abbbbabbbbaaaababbbbbbaaaababb",
      "aaaaabbaabaaaaababaa",
      "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
      "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba",
  ]

  for line in inputs:
    if len(line) == 0:
      rules[8] = [[42], [42, 8]]
      rules[11] = [[42, 31], [42, 11, 31]]
      on_messages = True
      continue

    if on_messages:
      is_valid = validate_message(line, rules)
      if is_valid:
        num_valid += 1
        if line in test_matches:
          print('correct positive', line)
        else:
          print('false positive', line)
      else:
        if line in test_matches:
          print('false negative', line)
        else:
          print('correct negative', line)

      print('\n----------\n')
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


test_inputs = get_inputs(filename='inputs_sample_2.txt')
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 12

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer < 366
