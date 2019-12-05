# https://adventofcode.com/2019/day/5

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

CODES = {
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
LOG_IDX = -1

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0].split(',')

def get_program_values(i, inputs, params):
  if len(params) == 0 or int(params[0]) == POSITION_MODE:
    val1 = inputs[int(inputs[i+1])]
  else:
    val1 = inputs[i+1]

  if len(params) <= 1 or int(params[1]) == POSITION_MODE:
    val2 = inputs[int(inputs[i+2])]
  else:
    val2 = inputs[i+2]

  return [int(val1), int(val2)]

def intcode(intcode_input, inputs):
  inputs_copy = inputs.copy()
  outputs = []

  total_inputs = len(inputs_copy)
  i = 0
  while i < total_inputs:
    input_program = list(str(inputs_copy[i]))
    optcode = int(''.join(input_program[-2:]))
    params = input_program[0:-2]
    params.reverse()

    if (optcode not in CODES.values()) or (optcode == CODES['EXIT']):
      break

    if optcode == CODES['INPUT']:
      inputs_copy[int(inputs_copy[i+1])] = intcode_input
      step = 2
      i += step
      continue

    elif optcode == CODES['OUTPUT']:
      if len(params) == 0 or int(params[0]) == POSITION_MODE:
        output = inputs_copy[int(inputs_copy[i+1])]
      else:
        output = inputs_copy[i+1]

      output = int(output)
      outputs.append(output)
      step = 2
      i += step
      continue

    elif optcode in [CODES['ADD'], CODES['MULTI'], CODES['LESS_THAN'], CODES['EQUALS']]:
      val1, val2 = get_program_values(i, inputs_copy, params)

      if optcode == CODES['ADD']:
        output = val1 + val2
      elif optcode == CODES['MULTI']:
        output = val1 * val2
      elif optcode == CODES['LESS_THAN']:
        if val1 < val2:
          output = 1
        else:
          output = 0
      elif optcode == CODES['EQUALS']:
        if val1 == val2:
          output = 1
        else:
          output = 0

      output_idx = int(inputs_copy[i+3])
      inputs_copy[output_idx] = output
      step = 4
      i += step
      continue

    elif optcode in [CODES['JUMP_IF_TRUE'], CODES['JUMP_IF_FALSE']]:
      val1, val2 = get_program_values(i, inputs_copy, params)

      if optcode == CODES['JUMP_IF_TRUE'] and val1 != 0:
        i = val2
      elif optcode == CODES['JUMP_IF_FALSE'] and val1 == 0:
        i = val2
      else:
        i += 3

    else:
      print('UNKNOWN OPTCODE!!!', i, 'input_program', input_program,
            'optcode', optcode, 'params', params)

  return outputs

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = intcode(5, inputs)
  print(f'answer:', answer)

main()
