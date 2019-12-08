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
    'EXIT': 99,
}
POSITION_MODE = 0
IMMEDIATE_MODE = 1


def get_program(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return list(map(int, inputs[0].split(',')))


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


def intcode(program_orig, user_inputs=[]):
  program = program_orig.copy()
  user_inputs = user_inputs.copy()

  outputs = []
  num_user_inputs = len(user_inputs)

  input_i = 0
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
      input_val = user_inputs[input_i] if input_i < num_user_inputs else 0
      # print(user_inputs, input_i, input_val)
      program[program[i+1]] = input_val
      input_i += 1
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

  # print(outputs)
  return outputs[0]


def process(program):
  output = 0
  range_min = 0
  range_max = 4 + 1

  num_amps = 5
  found_settings = []
  max_output = None

  for a in range(range_min, range_max):
    used = []
    a_output = intcode(program, user_inputs=[a, 0])
    print('a', used)

    for b in range(range_min, range_max):
      used = [a]
      if b in used:
        continue
      used.append(b)
      b_output = intcode(program, user_inputs=[b, a_output])

      for c in range(range_min, range_max):
        used = [a, b]
        if c in used:
          continue
        used.append(c)
        c_output = intcode(program, user_inputs=[c, b_output])

        for d in range(range_min, range_max):
          used = [a, b, c]
          if d in used:
            continue
          used.append(d)
          d_output = intcode(program, user_inputs=[d, c_output])

          for e in range(range_min, range_max):
            used = [a, b, c, d]
            if e in used:
              continue

            used.append(e)
            e_output = intcode(program, user_inputs=[e, d_output])
            if max_output is None or max_output < e_output:
              found_settings = used
              max_output = e_output

  print(found_settings)
  return max_output


def main():
  program = get_program(SCRIPT_DIR, INPUT_FILENAME)
  output = process(program)
  print(f'answer:', output)

main()
