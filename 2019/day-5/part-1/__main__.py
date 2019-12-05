# https://adventofcode.com/2019/day/5

import os

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0].split(',')

def intcode(inputs):
  ADD_CODE = 1
  MULTI_CODE = 2
  INPUT_CODE = 3
  OUTPUT_CODE = 4
  EXIT_CODE = 99
  ALLOWED_VALUES = [ADD_CODE, MULTI_CODE, INPUT_CODE, OUTPUT_CODE, EXIT_CODE]

  POSITION_MODE = 0
  IMMEDIATE_MODE = 1

  inputs_copy = inputs.copy()
  outputs = []

  total_inputs = len(inputs_copy)
  i = 0

  LOG_IDX = -1
  while i < total_inputs:
    input_program = list(str(inputs_copy[i]))

    optcode = int(''.join(input_program[-2:]))
    params = input_program[0:-2]
    params.reverse()

    if i <= LOG_IDX:
      print(i, 'input_program', input_program, 'optcode', optcode, 'params', params)

    if (optcode not in ALLOWED_VALUES) or (optcode == EXIT_CODE):
      break

    if optcode == ADD_CODE or optcode == MULTI_CODE:
      if len(params) == 0 or int(params[0]) == POSITION_MODE:
        val1 = inputs_copy[int(inputs_copy[i+1])]
        if i <= LOG_IDX:
          print('val1 in position mode:', val1, int(inputs_copy[i+1]))
      else:
        val1 = inputs_copy[i+1]
        if i <= LOG_IDX:
          print('val1 in immed mode:', val1, int(inputs_copy[i+1]))

      if len(params) <= 1 or int(params[1]) == POSITION_MODE:
        val2 = inputs_copy[int(inputs_copy[i+2])]
        if i <= LOG_IDX:
          print('val2 in position mode:', val2, int(inputs_copy[i+2]))
      else:
        val2 = inputs_copy[i+2]
        if i <= LOG_IDX:
          print('val2 in immed mode:', val2, int(inputs_copy[i+2]))

      if optcode == ADD_CODE:
        output = int(val1) + int(val2)
      elif optcode == MULTI_CODE:
        output = int(val1) * int(val2)

      output_idx = int(inputs_copy[i+3])
      inputs_copy[output_idx] = output
      step = 4
      if i <= LOG_IDX:
        print(i, val1, val2, output, output_idx, inputs_copy[output_idx], step)
    elif optcode == INPUT_CODE:
      inputs_copy[int(inputs_copy[i+1])] = 1
      step = 2
      if i <= LOG_IDX:
        print(i, int(inputs_copy[i+1]), inputs_copy[int(inputs_copy[i+1])], step)
    elif optcode == OUTPUT_CODE:
      if len(params) == 0 or int(params[0]) == POSITION_MODE:
        output = inputs_copy[int(inputs_copy[i+1])]
      else:
        output = inputs_copy[i+1]

      output = int(output)
      outputs.append(output)

      print('OUTPUT:', output)
      step = 2


    i += step
    if i <= LOG_IDX:
      print('----')

  return outputs

def main():
  # MAX_VALUE = 99
  # MIN_VALUE = 0

  # # FIND = 19690720
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  # print(inputs)
  answer = intcode(inputs)
  print(f'answer:', answer)

  # result = {
  #   'success': False,
  #   'noun': None,
  #   'verb': None
  # }

  # for noun in range(MIN_VALUE, MAX_VALUE + 1):
  #   if result['success']:
  #     break

  #   for verb in range(MIN_VALUE, MAX_VALUE + 1):
  #     if intcode(INPUTS.copy(), noun, verb) == FIND:
  #       result['success'] = True
  #       result['noun'] = noun
  #       result['verb'] = verb
  #       break

  # print('answer:', 100 * result['noun'] + result['verb'])

main()
