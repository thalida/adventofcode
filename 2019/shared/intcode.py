# https://adventofcode.com/2019/day/7

import os

class Intcode():
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

  MODES = {
    'POSITION': 0,
    'IMMEDIATE': 1,
    'RELATIVE': 2
  }

  EXIT_CODES = {
    'EXIT': 'exit',
    'OUTPUT': 'output',
  }

  def __init__(self, program, pointer=0, outputs=[], relative_base=0, enable_exit_on_output=False):
    if isinstance(program, str):
      program = program.split(',')

    if isinstance(program, list):
      program = {i: int(code) for i, code in enumerate(program)}

    self.program = program.copy()
    self.pointer = pointer
    self.outputs = outputs.copy()
    self.relative_base = relative_base
    self.enable_exit_on_output = enable_exit_on_output
    self.has_pending_output = False
    self.exit_code = None

  def get_program_value(self, index, default_value=0):
    if index not in self.program:
      self.program[index] = default_value

    return self.program[index]

  def get_program_write_index(self, pointer, write_mode):
    index = self.get_program_value(pointer)

    if write_mode == self.MODES['RELATIVE']:
      index += self.relative_base

    return index

  def get_instruction_inputs(self, input_modes, num_inputs=2, debug=False):
    inputs = []
    num_input_modes = len(input_modes)

    for i in range(0, num_inputs):
      input_pointer = self.pointer + i + 1
      input_val = self.get_program_value(input_pointer)

      if num_input_modes == 0 or input_modes[i] == self.MODES['POSITION']:
        input = self.get_program_value(input_val)
      elif input_modes[i] == self.MODES['RELATIVE']:
        input_val += self.relative_base
        input = self.get_program_value(input_val)
      else:
        input = self.get_program_value(input_pointer)
      inputs.append(input)

    return inputs[0] if len(inputs) == 1 else inputs

  def run(self, input_val=None, debug=False):
    while self.pointer < len(self.program):
      instruction = str(self.program[self.pointer])
      optcode = int(''.join(instruction[-2:]))
      modes = list(map(int, instruction[0:-2]))
      modes.reverse()

      if len(modes) < 3:
        num_missing = 3 - len(modes)
        modes += [self.MODES['POSITION']] * num_missing

      if optcode not in self.INSTRUCTIONS.values():
        break

      if optcode == self.INSTRUCTIONS['EXIT']:
        self.exit_code = self.EXIT_CODES['EXIT']
        return

      if self.enable_exit_on_output and self.has_pending_output:
        self.has_pending_output = False
        self.exit_code = self.EXIT_CODES['OUTPUT']
        return

      if optcode == self.INSTRUCTIONS['INPUT']:
        write_index = self.get_program_write_index(self.pointer + 1, modes[0])
        self.program[write_index] = input_val
        self.pointer += 2
        continue

      if optcode == self.INSTRUCTIONS['OUTPUT']:
        result = self.get_instruction_inputs(modes, num_inputs=1, debug=debug)
        self.outputs.append(result)
        self.has_pending_output = self.enable_exit_on_output
        self.pointer += 2
        continue

      if optcode == self.INSTRUCTIONS['ADJUST_RELATIVE_BASE']:
        result = self.get_instruction_inputs(modes, num_inputs=1)
        self.relative_base += result
        self.pointer += 2
        continue

      input1, input2 = self.get_instruction_inputs(modes, num_inputs=2, debug=self.pointer==53)
      result = None
      new_pointer = None
      if optcode == self.INSTRUCTIONS['ADD']:
        result = input1 + input2
      elif optcode == self.INSTRUCTIONS['MULTI']:
        result = input1 * input2
      elif optcode == self.INSTRUCTIONS['LESS_THAN']:
        result = input1 < input2
      elif optcode == self.INSTRUCTIONS['EQUALS']:
        result = input1 == input2
      elif optcode == self.INSTRUCTIONS['JUMP_IF_TRUE'] and input1 != 0:
        new_pointer = input2
      elif optcode == self.INSTRUCTIONS['JUMP_IF_FALSE'] and input1 == 0:
        new_pointer = input2

      if result is None:
        self.pointer = new_pointer if new_pointer is not None else self.pointer + 3
        continue

      if isinstance(result, bool):
        result = 1 if result is True else 0

      write_index = self.get_program_write_index(self.pointer + 3, modes[-1])
      self.program[write_index] = result
      self.pointer += 4
