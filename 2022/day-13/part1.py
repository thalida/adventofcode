import os
from pprint import pprint

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


def get_packet_pairs(inputs):
  packet_pairs = []
  packet_i = 0
  for line in inputs:
    if len(line) == 0:
      packet_i += 1
      continue

    if len(packet_pairs) <= packet_i:
      packet_pairs.append([])

    packet = parse_packet(line)
    packet_pairs[packet_i].append(packet[0][0])

  return packet_pairs


def validate_packet_pair(packet_pair):
  is_valid = False
  continue_loop = True

  while continue_loop:
    left_size = len(packet_pair[0])
    right_size = len(packet_pair[1])

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

    left = packet_pair[0].pop(0)
    right = packet_pair[1].pop(0)

    if isinstance(left, int) and isinstance(right, int):
      is_valid = left < right
      continue_loop = left == right

    elif isinstance(left, list) and isinstance(right, list):
      is_valid, continue_loop = validate_packet_pair([left, right])

    elif isinstance(left, list) and isinstance(right, int):
      new_left = left
      new_right = [right]
      is_valid, continue_loop = validate_packet_pair([new_left, new_right])

    elif isinstance(left, int) and isinstance(right, list):
      new_left = [left]
      new_right = right
      is_valid, continue_loop = validate_packet_pair([new_left, new_right])

  return is_valid, continue_loop


def process(inputs, debug=False):
  outputs = inputs.copy()
  packet_pairs = get_packet_pairs(inputs)

  valid_indexes = []
  for i, packet_pair in enumerate(packet_pairs):
    is_valid, _ = validate_packet_pair(packet_pair.copy())
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
