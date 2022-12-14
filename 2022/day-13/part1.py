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


def compare_packets(left_packet_in, right_packet_in):
  is_valid = None

  left_packet = left_packet_in.copy()
  right_packet = right_packet_in.copy()

  while is_valid is None:
    left_size = len(left_packet)
    right_size = len(right_packet)

    if left_size == 0 and left_size < right_size:
      is_valid = True
      break

    if right_size == 0 and right_size < left_size:
      is_valid = False
      break

    if left_size == 0 and right_size == 0:
      is_valid = None
      break

    left = left_packet.pop(0)
    right = right_packet.pop(0)

    if isinstance(left, int) and isinstance(right, int):
      is_valid = None if left == right else left < right
      continue

    if isinstance(left, int):
      left = [left]

    elif isinstance(right, int):
      right = [right]

    is_valid = compare_packets(left, right)

  return is_valid


def process(inputs, debug=False):
  outputs = inputs.copy()
  packets = get_packets(inputs)
  packet_pairs = zip(*[iter(packets)]*2)

  valid_indexes = []
  for i, (a, b) in enumerate(packet_pairs):
    is_valid = compare_packets(a, b)
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
