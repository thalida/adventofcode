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

def print_crt(crt):
  for row in crt:
    print(''.join(row))

def process(inputs):
  num_rows = 6
  num_pixels = 40
  crt = [[' ']*num_pixels for _ in range(num_rows)]

  x = 1
  cmd_cycles = {
    'addx': 2,
    'noop': 1,
  }

  cycle = 0
  for i, line in enumerate(inputs):
    cmd, *args = line.split()

    for j in range(cmd_cycles[cmd]):
      row = cycle // num_pixels
      pixel = cycle % num_pixels
      if pixel in range(x-1, x+2):
        crt[row][pixel] = '█'

      cycle += 1

    if cmd == 'addx':
      x += int(args[0])

  print_crt(crt)
  return [''.join(row) for row in crt]


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
test_output = [
'██  ██  ██  ██  ██  ██  ██  ██  ██  ██  ',
'███   ███   ███   ███   ███   ███   ███ ',
'████    ████    ████    ████    ████    ',
'█████     █████     █████     █████     ',
'██████      ██████      ██████      ████',
'███████       ███████       ███████     '
]
assert test_answer == test_output


print('\n')

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
output = [
'████  ██   ██  █  █ ████ ███  ████  ██  ',
'█    █  █ █  █ █  █    █ █  █ █    █  █ ',
'███  █    █    █  █   █  █  █ ███  █    ',
'█    █ ██ █    █  █  █   ███  █    █    ',
'█    █  █ █  █ █  █ █    █ █  █    █  █ ',
'█     ███  ██   ██  ████ █  █ ████  ██  ']
assert answer == output
