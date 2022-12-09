import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample_2.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)


def process(inputs):
  outputs = inputs.copy()

  knots = [['0,0'] for _ in range(10)]
  print(f'knots:', knots)

  for line in inputs:
    direction, amount = line[0], int(line[1:])

    for i in range(1, amount + 1):
      new_head = list(map(int, knots[0][-1].split(',')))
      if direction == 'L':
        new_head[0] -= 1
      elif direction == 'R':
        new_head[0] += 1
      elif direction == 'U':
        new_head[1] += 1
      elif direction == 'D':
        new_head[1] -= 1

      knots[0].append(f'{new_head[0]},{new_head[1]}')

      for j in range(1, len(knots)):
        knot_head = list(map(int, knots[j - 1][-1].split(',')))
        next_tail = list(map(int, knots[j][-1].split(',')))

        x_diff = knot_head[0] - next_tail[0]
        y_diff = knot_head[1] - next_tail[1]

        same_col = knot_head[0] == next_tail[0]
        same_row = knot_head[1] == next_tail[1]
        is_diagonal = (
          not same_col and not same_row and
          (abs(x_diff) >= 2 or abs(y_diff) >= 2)
        )

        if is_diagonal or abs(x_diff) >= 2:
          if x_diff > 0:
            next_tail[0] += 1
          else:
            next_tail[0] -= 1

        if is_diagonal or abs(y_diff) >= 2:
          if y_diff > 0:
            next_tail[1] += 1
          else:
            next_tail[1] -= 1

        knots[j].append(f'{next_tail[0]},{next_tail[1]}')

  return len(set(knots[9]))


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 36

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2331
