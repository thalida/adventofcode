import os
from pprint import pprint

import ast
from functools import cmp_to_key

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'
SAMPLE_INPUTS_FILENAME = 'inputs_sample.txt'


def get_inputs(filename=INPUT_FILENAME):
  filepath = os.path.join(SCRIPT_DIR, filename)
  with open(filepath, 'r') as f:
    inputs = f.read().splitlines()

  return list(inputs)

def parse_packet(line):
  packet = []
  i = 0
  while i < len(line) - 1 and len(line) > 0:
    char = line[i]

    if char == ',':
      i += 1
      continue

    if char == '[':
      nested_packet, line = parse_packet(line[i+1:])
      packet.append(nested_packet)
      i = 0
      continue

    if char == ']':
      return packet, line[i+1:]

    next_comma = line.index(',', i) if ',' in line[i:] else len(line)
    next_bracket = line.index(']', i) if ']' in line[i:] else len(line)
    end = min(next_comma, next_bracket)
    ss = line[i:end]
    packet.append(int(ss) if ss.isdigit() else ss)
    i += len(ss)

  return packet, line[i+1:]


def get_packets(inputs):
  packets = []

  for line in inputs:
    if len(line) == 0:
      continue

    packets.append(ast.literal_eval(line))

  packets.append([[2]])
  packets.append([[6]])

  return packets

def compare_packets(left_packet_in, right_packet_in):
  state = 0

  left_packet = left_packet_in.copy()
  right_packet = right_packet_in.copy()

  while state == 0:
    left_size = len(left_packet)
    right_size = len(right_packet)

    if left_size == 0 and left_size < right_size:
      state = -1
      break

    if right_size == 0 and right_size < left_size:
      state = 1
      break

    if left_size == 0 and right_size == 0:
      state = 0
      break

    left = left_packet.pop(0)
    right = right_packet.pop(0)

    if isinstance(left, int) and isinstance(right, int):
      diff = left - right
      state = 0 if diff == 0 else -1 if diff < 0 else 1

    elif isinstance(left, list) and isinstance(right, list):
      state = compare_packets(left, right)

    elif isinstance(left, list) and isinstance(right, int):
      new_left = left
      new_right = [right]
      state = compare_packets(new_left, new_right)

    elif isinstance(left, int) and isinstance(right, list):
      new_left = [left]
      new_right = right
      state = compare_packets(new_left, new_right)

  return state

def process(inputs):
  outputs = inputs.copy()
  packets = get_packets(inputs)
  sorted_packets = sorted(packets, key=cmp_to_key(compare_packets))

  decoder_a = sorted_packets.index([[2]]) + 1
  decoder_b = sorted_packets.index([[6]]) + 1
  return decoder_a * decoder_b

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 140

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 21614
