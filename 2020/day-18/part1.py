# https://adventofcode.com/2020/day/18

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  inputs = []

  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return inputs

def solve(equation, from_paren=False):
  equation = equation.replace(' ', '')

  left = 0
  right = 0
  operation = None
  i = 0

  while i < len(equation):
    if equation[i] in ['+', '*']:
      i += 1
      continue

    if from_paren and equation[i] == ')':
      i += 1
      break

    if equation[i] == '(':
      right, end_i = solve(equation[i+1:], from_paren=True)
    else:
      end_i = 0
      right = int(equation[i])

    if i - 1 < 0:
      operation = '+'
    else:
      operation = equation[i-1]

    if operation == '+':
      left += right
    elif operation == '*':
      left *= right

    i = i + end_i + 1

  return left, i

def process(inputs):
  answers = []

  for i, equation in enumerate(inputs):
    solution, _ = solve(equation)
    answers.append(solution)

  if len(answers) < 2:
    return answers[0]

  return sum(answers)


test_answer1 = process(['1 + 2 * 3 + 4 * 5 + 6'])
print(f'test answer 1:', test_answer1)
assert test_answer1 == 71

test_answer2 = process(['1 + (2 * 3) + (4 * (5 + 6))'])
print(f'test answer 2:', test_answer2)
assert test_answer2 == 51

test_answer3 = process(['2 * 3 + (4 * 5)'])
print(f'test answer 3:', test_answer3)
assert test_answer3 == 26

test_answer4 = process(['5 + (8 * 3 + 9 + 3 * 4 * 3)'])
print(f'test answer 4:', test_answer4)
assert test_answer4 == 437

test_answer5 = process(['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'])
print(f'test answer 5:', test_answer5)
assert test_answer5 == 12240

test_answer6 = process(['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'])
print(f'test answer 6:', test_answer6)
assert test_answer6 == 13632

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 464478013511

inputs = get_inputs(filename='inputs-eddy.txt')
answer = process(inputs)
print(f'(eddy) answer:', answer)
assert answer == 650217205854
