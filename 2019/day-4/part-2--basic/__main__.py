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
  inputs_copy = inputs.copy()
  passwords_found = []

  for n in range(inputs_copy[0], inputs_copy[1] + 1):
    last_c = None
    has_true_double = False
    always_increases = True
    run = 0
    loops = 0
    # print(n)
    for c in str(n):
      # print(c)
      if last_c is None:
        last_c = c
        loops += 1
        continue

      if int(last_c) > int(c):
        always_increases = False
        break

      same_char = int(last_c) == int(c)
      # print('here?', last_c, c, same_char, run)
      if same_char:
        run += 1

      # print('during?', last_c, c, same_char, run, loops, len(str(n)), has_true_double)

      if not same_char or loops + 1 == len(str(n)):
        has_true_double = has_true_double or run == 1

      if not same_char:
        run = 0

      # print('after?', last_c, c, same_char, run, has_true_double)

      # if run > 2:
      #   has_true_double = True


      # print('double', last_c, c, run, has_true_double)
      # if has_true_double or run == 1:
      #   has_true_double = has_true_double or (run == 1)
      # run = 0

      last_c = c
      loops += 1

    if has_true_double and always_increases:
      passwords_found.append(n)

  pprint(passwords_found)
  return len(passwords_found)

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  # answer = num_potential_passwords([566699, 566699])
  answer = num_potential_passwords(inputs)
  print(f'answer:', answer)

main()
