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

  num_knots = 10
  knots = { i: [[0, 0]] for i in range(num_knots) }

  for line in inputs:
    direction, amount = line[0], int(line[1:])

    for i in range(1, amount + 1):
      head = knots[0][-1].copy()

      if direction == 'L':
        head[0] -= 1
      elif direction == 'R':
        head[0] += 1
      elif direction == 'U':
        head[1] += 1
      elif direction == 'D':
        head[1] -= 1

      knots[0].append(head)

      for j in range(1, len(knots)):
        prev_knot = knots[j - 1][-1]
        curr_knot = knots[j][-1].copy()

        dx = prev_knot[0] - curr_knot[0]
        dy = prev_knot[1] - curr_knot[1]

        is_same_col = prev_knot[0] == curr_knot[0]
        is_same_row = prev_knot[1] == curr_knot[1]
        should_move_diag = (
          not is_same_col and
          not is_same_row and
          abs(dx) + abs(dy) > 2
        )

        if should_move_diag or abs(dx) > 1:
          curr_knot[0] += 1 if dx > 0 else -1

        if should_move_diag or abs(dy) > 1:
          curr_knot[1] += 1 if dy > 0 else -1

        knots[j].append(curr_knot)

  return len(set(map(lambda p: f'{p[0]},{p[1]}', knots[9])))


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 36

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2331
