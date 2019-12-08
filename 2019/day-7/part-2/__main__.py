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


def intcode(program_orig, user_inputs=[], outputs=[], i=0, input_i=0, halt_on_output=True, debug=False):
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
      program[program[i+1]] = input_val
      input_i += 1
      i += 2
      continue

    if optcode == INSTRUCTIONS['OUTPUT']:
      result = get_instruction_inputs(i, program, modes, num_inputs=1)
      outputs.append(result)

      if halt_on_output:
        has_pending_output = True

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



def get_signal_output(program, a, b, c, d, e):
  amp_keys = ['a', 'b', 'c', 'd', 'e']
  default_state = {
      'program': program.copy(),
    'i': 0,
    'input_i': 0,
    'inputs': [],
    'outputs': [],
    'exit_code': None
  }
  state = {}

  for amp in amp_keys:
    state[amp] = default_state.copy()

  state['a']['inputs'] = [a, 0]
  state['b']['inputs'] = [b]
  state['c']['inputs'] = [c]
  state['d']['inputs'] = [d]
  state['e']['inputs'] = [e]

  while True:
    if state['a']['exit_code'] != 'exit':
      if len(state['e']['outputs']) > 0:
        state['a']['inputs'].append(state['e']['outputs'][-1])

      state['a'] = intcode(
          state['a']['program'],
        outputs=state['a']['outputs'],
        user_inputs=state['a']['inputs'],
        input_i=state['a']['input_i'],
        i=state['a']['i']
      )

    if state['b']['exit_code'] != 'exit':
      state['b']['inputs'].append(state['a']['outputs'][-1])
      print(state['b']['input_i'], state['b']['inputs'])
      state['b'] = intcode(
          state['b']['program'],
        outputs=state['b']['outputs'],
        user_inputs=state['b']['inputs'],
        input_i=state['b']['input_i'],
        i=state['b']['i']
      )

    if state['c']['exit_code'] != 'exit':
      state['c']['inputs'].append(state['b']['outputs'][-1])
      state['c'] = intcode(
          state['c']['program'],
        outputs=state['c']['outputs'],
        user_inputs=state['c']['inputs'],
        input_i=state['c']['input_i'],
        i=state['c']['i']
      )

    if state['d']['exit_code'] != 'exit':
      state['d']['inputs'].append(state['c']['outputs'][-1])
      state['d'] = intcode(
          state['d']['program'],
        outputs=state['d']['outputs'],
        user_inputs=state['d']['inputs'],
        input_i=state['d']['input_i'],
        i=state['d']['i']
      )

    if state['e']['exit_code'] != 'exit':
      state['e']['inputs'].append(state['d']['outputs'][-1])
      state['e'] = intcode(
          state['e']['program'],
        outputs=state['e']['outputs'],
        user_inputs=state['e']['inputs'],
        input_i=state['e']['input_i'],
        i=state['e']['i']
      )

    if state['e']['exit_code'] == 'exit':
      break

  return state['e']['outputs'][-1]


def process(program_orig):
  output = 0
  range_min = 5
  range_max = 9 + 1

  found_settings = []
  max_output = None

  for a in range(range_min, range_max):
    used = []
    for b in range(range_min, range_max):
      used = [a]
      if b in used:
        continue
      used.append(b)

      for c in range(range_min, range_max):
        used = [a, b]
        if c in used:
          continue
        used.append(c)

        for d in range(range_min, range_max):
          used = [a, b, c]
          if d in used:
            continue
          used.append(d)

          for e in range(range_min, range_max):
            used = [a, b, c, d]
            if e in used:
              continue
            used.append(e)

            output = get_signal_output(program_orig, *used)

            if max_output is None or max_output < output:
              found_settings = used
              max_output = output

  print(found_settings)
  return max_output


def main():
  program = get_program(SCRIPT_DIR, INPUT_FILENAME)
  output = process(program)
  print(f'answer:', output)

main()
