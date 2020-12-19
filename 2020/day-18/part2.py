# https://adventofcode.com/2020/day/18

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

def solve(equation):
  equation = equation.replace(' ', '')

  while '(' in equation:
    start_idxs = [i for i, c in enumerate(list(equation)) if c == '(']
    start_idx = start_idxs[-1] + 1
    inner_eq = equation[start_idx:]

    end_idxs = [i for i, c in enumerate(list(inner_eq)) if c == ')']
    end_idx = end_idxs[0]
    inner_eq = inner_eq[:end_idx]

    solution = solve(inner_eq)
    equation = equation[:start_idx-1] + str(solution) + equation[start_idx+end_idx+1:]


  left = ''
  right = ''
  operation = None
  start_i = 0
  curr_i = 0
  while True:
    c = None

    if curr_i < len(equation):
      c = equation[curr_i]

      if operation == '*' and '+' in equation:
        start_i = curr_i
        left = ''
        right = ''
        operation = None
        continue

      if operation is None:
        if c in ['+', '*']:
          operation = c
        else:
          left += c
        curr_i += 1
        continue

      if c not in ['+', '*']:
        right += c
        curr_i += 1
        continue

    if operation == '*':
      res = int(left) * int(right)
    elif operation == '+':
      res = int(left) + int(right)

    equation = equation[:start_i] + str(res) + equation[curr_i:]
    curr_i = start_i + len(str(res)) + 1

    if curr_i >= len(equation):
      start_i = 0
      curr_i = 0
      left = ''
      right = ''
      operation = None
    else:
      left = str(res)
      right = ''
      operation = c

    try:
      return int(equation)
    except:
      continue

def process(inputs):
  answers = []

  for i, equation in enumerate(inputs):
    solution = solve(equation)
    answers.append(solution)

  if len(answers) < 2:
    return answers[0]

  return sum(answers)


test_answer1 = process(['1 + 2 * 3 + 4 * 5 + 6'])
print(f'test answer 1:', test_answer1)
assert test_answer1 == 231

test_answer2 = process(['1 + (2 * 3) + (4 * (5 + 6))'])
print(f'test answer 2:', test_answer2)
assert test_answer2 == 51

test_answer3 = process(['2 * 3 + (4 * 5)'])
print(f'test answer 3:', test_answer3)
assert test_answer3 == 46

test_answer4 = process(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])
print(f'test answer 4:', test_answer4)
assert test_answer4 == 1445

test_answer5 = process(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])
print(f'test answer 5:', test_answer5)
assert test_answer5 == 669060

test_answer6 = process(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'])
print(f'test answer 6:', test_answer6)
assert test_answer6 == 23340

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 85660197232452
