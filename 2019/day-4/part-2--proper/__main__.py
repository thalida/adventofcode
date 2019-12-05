# https://adventofcode.com/2019/day/4

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same(like 22 in 122345).
# Going from left to right, the digits never decrease
# they only ever increase or stay the same(like 111123 or 135679).

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()
    inputs = inputs[0].split('-')

  return [int(inputs[0]), int(inputs[1])]

def num_potential_passwords(inputs):
  start, end = inputs.copy()
  passwords_found = []

  for n in range(start, end + 1):
    potential_password = str(n)
    has_true_double = False
    always_increases = False

    last_c = None
    run = 1
    loops = 0
    for c in potential_password:
      c = int(c)

      if last_c is not None:
        same_char = last_c == c
        is_last_char = loops + 1 == len(potential_password)

        if last_c > c:
          always_increases = False
          break

        if same_char:
          run += 1

        if not same_char or is_last_char:
          has_true_double = has_true_double or run == 2
          run = 1

      always_increases = True
      last_c = c
      loops += 1

    if has_true_double and always_increases:
      passwords_found.append(n)

  return len(passwords_found)

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = num_potential_passwords(inputs)
  print(f'answer:', answer)

main()
