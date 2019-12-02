# https://adventofcode.com/2019/day/2

def intcode(inputs, noun, verb):
  ADD_CODE = 1
  MULTI_CODE = 2
  EXIT_CODE = 99
  ALLOWED_VALUES = [ADD_CODE, MULTI_CODE, EXIT_CODE]
  STEP = 4

  inputs_copy = inputs.copy()
  total_inputs = len(inputs_copy)

  inputs_copy[1] = noun
  inputs_copy[2] = verb

  i = 0
  while i < total_inputs:
    optcode = inputs_copy[i]
    val1_idx = inputs_copy[i+1]
    val2_idx = inputs_copy[i+2]
    output_idx = inputs_copy[i+3]

    if (optcode not in ALLOWED_VALUES) or (optcode == EXIT_CODE):
      break

    if optcode == ADD_CODE:
      output = inputs_copy[val1_idx] + inputs_copy[val2_idx]
    elif optcode == MULTI_CODE:
      output = inputs_copy[val1_idx] * inputs_copy[val2_idx]

    inputs_copy[output_idx] = output

    i += STEP

  return inputs_copy[0]

def main():
  MAX_VALUE = 99
  MIN_VALUE = 0

  FIND = 19690720
  INPUTS = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,5,27,2,27,10,31,1,31,9,35,1,35,5,39,1,6,39,43,2,9,43,47,1,5,47,51,2,6,51,55,1,5,55,59,2,10,59,63,1,63,6,67,2,67,6,71,2,10,71,75,1,6,75,79,2,79,9,83,1,83,5,87,1,87,9,91,1,91,9,95,1,10,95,99,1,99,13,103,2,6,103,107,1,107,5,111,1,6,111,115,1,9,115,119,1,119,9,123,2,123,10,127,1,6,127,131,2,131,13,135,1,13,135,139,1,9,139,143,1,9,143,147,1,147,13,151,1,151,9,155,1,155,13,159,1,6,159,163,1,13,163,167,1,2,167,171,1,171,13,0,99,2,0,14,0]

  result = {
    'success': False,
    'noun': None,
    'verb': None
  }

  for noun in range(MIN_VALUE, MAX_VALUE + 1):
    if result['success']:
      break

    for verb in range(MIN_VALUE, MAX_VALUE + 1):
      if intcode(INPUTS.copy(), noun, verb) == FIND:
        result['success'] = True
        result['noun'] = noun
        result['verb'] = verb
        break

  print('answer:', 100 * result['noun'] + result['verb'])

main()
