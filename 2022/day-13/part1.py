import os
from pprint import pprint

import ast

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

def get_packets(inputs):
  packets = []

  for line in inputs:
    if len(line) == 0:
      continue

    packets.append(ast.literal_eval(line))

  return packets


def validate_packet_pair(left_packet, right_packet):
  is_valid = False
  continue_loop = True

  while continue_loop:
    left_size = len(left_packet)
    right_size = len(right_packet)

    if left_size == 0 and left_size < right_size:
      is_valid = True
      continue_loop = False
      break

    if right_size == 0 and right_size < left_size:
      is_valid = False
      continue_loop = False
      break

    if left_size == 0 and right_size == 0:
      is_valid = False
      continue_loop = True
      break

    left = left_packet.pop(0)
    right = right_packet.pop(0)

    if isinstance(left, int) and isinstance(right, int):
      is_valid = left < right
      continue_loop = left == right

    elif isinstance(left, list) and isinstance(right, list):
      is_valid, continue_loop = validate_packet_pair(left, right)

    elif isinstance(left, list) and isinstance(right, int):
      new_left = left
      new_right = [right]
      is_valid, continue_loop = validate_packet_pair(new_left, new_right)

    elif isinstance(left, int) and isinstance(right, list):
      new_left = [left]
      new_right = right
      is_valid, continue_loop = validate_packet_pair(new_left, new_right)

  return is_valid, continue_loop


def process(inputs, debug=False):
  outputs = inputs.copy()
  packets = get_packets(inputs)
  packet_pairs = zip(*[iter(packets)]*2)

  valid_indexes = []
  for i, (a, b) in enumerate(packet_pairs):
    is_valid, _ = validate_packet_pair(a, b)
    if is_valid:
      valid_indexes.append(i+1)

  return sum(valid_indexes)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 13

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 4643
