import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)


def process(inputs):
  outputs = inputs.copy()

  head_poses = [[0, 0]]
  tail_poses = [[0, 0]]

  for line in inputs:
    direction, amount = line[0], int(line[1:])

    for i in range(1, amount + 1):
      head = head_poses[-1].copy()
      if direction == 'L':
        head[0] -= 1
      elif direction == 'R':
        head[0] += 1
      elif direction == 'U':
        head[1] += 1
      elif direction == 'D':
        head[1] -= 1

      head_poses.append(head)

      tail = tail_poses[-1].copy()

      dx = head[0] - tail[0]
      dy = head[1] - tail[1]

      is_same_col = head[0] == tail[0]
      is_same_row = head[1] == tail[1]
      should_move_diag = (
        not is_same_col and
        not is_same_row and
        abs(dx) + abs(dy) > 2
      )

      if should_move_diag or abs(dx) > 1:
        tail[0] += 1 if dx > 0 else -1

      if should_move_diag or abs(dy) > 1:
        tail[1] += 1 if dy > 0 else -1

      tail_poses.append(tail)

  return len(set(map(lambda x: f'{x[0]},{x[1]}', tail_poses)))


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 13

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 5779
