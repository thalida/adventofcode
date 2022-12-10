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
  x = 1
  cmd_cycles = {
    'addx': 2,
    'noop': 1,
  }

  cycle = 1
  signal_strength = 0
  check_point = 20
  for line in inputs:
    cmd, *args = line.split()

    for _ in range(cmd_cycles[cmd]):
      if cycle == check_point:
        signal_strength += cycle * x
        check_point += 40

      cycle += 1

    if cmd == 'addx':
      x += int(args[0])

  return signal_strength


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 13140

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 17380
