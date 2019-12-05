# https://adventofcode.com/2019/day/4

import os

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
    has_double = False
    always_increases = True
    for c in str(n):
      if last_c is None:
        last_c = c
        continue

      if int(last_c) > int(c):
        always_increases = False
        break

      if int(last_c) == int(c):
        has_double = True

      last_c = c

    if has_double and always_increases:
      passwords_found.append(n)

  print(passwords_found)
  return len(passwords_found)

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = num_potential_passwords(inputs)
  print(f'answer:', answer)

main()
