# https://adventofcode.com/2019/day/7

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
    'ADJUST_RELATIVE_BASE': 9,
    'EXIT': 99,
}
POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


def get_program(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return list(map(int, inputs[0].split(',')))


def get_value_at_index(index, program):
  if index not in program:
    program[index] = 0

  return program[index]


def get_instruction_inputs(program_index, program, modes, relative_base=0, num_inputs=2):
  inputs = []
  num_modes = len(modes)

  for i in range(0, num_inputs):
    input_idx = program_index + i + 1
    input_val = get_value_at_index(input_idx, program)

    if num_modes == 0 or modes[i] == POSITION_MODE:
      input = get_value_at_index(input_val, program)
    elif modes[i] == RELATIVE_MODE:
      input_val += relative_base
      input = get_value_at_index(input_val, program)
    else:
      input = get_value_at_index(input_idx, program)

    inputs.append(input)

  return inputs[0] if len(inputs) == 1 else inputs


def intcode(program_orig, user_inputs=[1], outputs=[], i=0, input_i=0, relative_base=0, halt_on_output=False, debug=False):
  program = program_orig.copy()
  num_user_inputs = len(user_inputs)
  has_pending_output = False

  program_length = len(program)
  while i < program_length:
    instruction = str(program[i])
    optcode = int(''.join(instruction[-2:]))
    modes = list(map(int, instruction[0:-2]))
    modes.reverse()

    if optcode not in INSTRUCTIONS.values():
      break

    if optcode == INSTRUCTIONS['EXIT']:
      return {
          'program': program,
          'i': i,
          'input_i': input_i,
          'inputs': user_inputs,
          'outputs': outputs,
          'exit_code': 'exit'
      }

    if halt_on_output and has_pending_output:
      has_pending_output = False
      return {
          'program': program,
          'i': i,
          'input_i': input_i,
          'inputs': user_inputs,
          'outputs': outputs,
          'exit_code': 'output'
      }

    if optcode == INSTRUCTIONS['INPUT']:
      input_val = user_inputs[input_i] if input_i < num_user_inputs else 0
      index = get_value_at_index(i+1, program)

      if modes[0] == RELATIVE_MODE:
        index += relative_base

      program[index] = input_val
      input_i += 1
      i += 2
      continue

    if optcode == INSTRUCTIONS['OUTPUT']:
      result = get_instruction_inputs(i, program, modes, relative_base=relative_base, num_inputs=1)
      outputs.append(result)

      if halt_on_output:
        has_pending_output = True

      i += 2
      continue

    if optcode == INSTRUCTIONS['ADJUST_RELATIVE_BASE']:
      result = get_instruction_inputs(i, program, modes, relative_base=relative_base, num_inputs=1)
      relative_base += result

      i += 2
      continue

    input1, input2 = get_instruction_inputs(i, program, modes, relative_base=relative_base, num_inputs=2)
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

    if len(modes) == 3 and modes[2] == RELATIVE_MODE:
      output_idx += relative_base

    program[output_idx] = output
    i += 4


def process(program_orig):
  output = intcode(program_orig, user_inputs=[2])
  return output


def main():
  program = get_program(SCRIPT_DIR, INPUT_FILENAME)
  program = {i: code for i, code in enumerate(program)}
  output = process(program)
  print(f'answer:', output['outputs'])


main()
