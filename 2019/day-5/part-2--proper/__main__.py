# https://adventofcode.com/2019/day/5

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

INSTRUCTIONS = {
  'ADD': 1,
  'MULTI': 2,
  'INPUT': 3,
  'OUTPUT': 4,
  'JUMP_IF_TRUE': 5,
  'JUMP_IF_FALSE': 6,
  'LESS_THAN': 7,
  'EQUALS': 8,
  'EXIT': 99,
}
POSITION_MODE = 0
IMMEDIATE_MODE = 1

def get_program(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return list(map(int,inputs[0].split(',')))


def get_instruction_inputs(program_index, program, modes, num_inputs=2):
  inputs = []
  num_modes = len(modes)

  for i in range(0, num_inputs):
    input_idx = program_index + i + 1
    input_val = program[input_idx]

    if num_modes <= i or modes[i] == POSITION_MODE:
      input = program[input_val]
    else:
      input = input_val

    inputs.append(input)

  return inputs[0] if len(inputs) == 1 else inputs


def intcode(program_orig, user_input = 1):
  program = program_orig.copy()
  outputs = []

  i = 0
  program_length = len(program)
  while i < program_length:
    instruction = str(program[i])
    optcode = int(''.join(instruction[-2:]))
    modes = list(map(int, instruction[0:-2]))
    modes.reverse()

    if optcode not in INSTRUCTIONS.values() or optcode == INSTRUCTIONS['EXIT']:
      break

    if optcode == INSTRUCTIONS['INPUT']:
      program[program[i+1]] = user_input
      i += 2
      continue

    if optcode == INSTRUCTIONS['OUTPUT']:
      result = get_instruction_inputs(i, program, modes, num_inputs=1)
      outputs.append(result)
      i += 2
      continue

    input1, input2 = get_instruction_inputs(i, program, modes, num_inputs=2)
    output = None
    new_i = None
    if optcode == INSTRUCTIONS['ADD']:
      output = input1 + input2
    elif optcode == INSTRUCTIONS['MULTI']:
      output = input1 * input2
    elif optcode == INSTRUCTIONS['LESS_THAN']:
      output = input1 < input2
    elif optcode == INSTRUCTIONS['EQUALS']:
      output = input1 == input2
    elif optcode == INSTRUCTIONS['JUMP_IF_TRUE'] and input1 != 0:
      new_i = input2
    elif optcode == INSTRUCTIONS['JUMP_IF_FALSE'] and input1 == 0:
      new_i = input2

    if output is None:
      i = new_i if new_i is not None else i + 3
      continue

    if isinstance(output, bool):
      output = 1 if output is True else 0

    output_idx = program[i+3]
    program[output_idx] = output
    i += 4

  return outputs

def main():
  program = get_program(SCRIPT_DIR, INPUT_FILENAME)
  output = intcode(program, 5)
  print(f'answer:', output)

main()
