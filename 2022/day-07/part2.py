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

def get_dirs(inputs):
  dirs = {}
  curr_cmd = None
  curr_path = []
  for line in inputs:
    if line.startswith('$'):
      cmd = line[1:].split()
      if cmd[0] == 'cd':
        curr_cmd = cmd[0]
        if cmd[1] == '..':
          curr_path.pop()
        else:
          curr_path.append(cmd[1])

      if cmd[0] == 'ls':
        curr_cmd = cmd[0]

      continue

    if curr_cmd == 'ls':
      for i in range(0, len(curr_path)):
        path_str = '/'.join(curr_path[:i+1])

        if path_str not in dirs:
          dirs[path_str] = 0

        file = line.split()
        if file[0] == 'dir':
          continue

        dirs[path_str] += int(file[0])

  return dirs

def process(inputs):
  dirs = get_dirs(inputs)


  avail_space = 70000000
  target_unused_space = 30000000
  curr_space = dirs['/']
  unused = avail_space - curr_space
  needed_space = target_unused_space - unused

  found_size = dirs['/']
  for d in dirs:
    size = dirs[d]
    if size >= needed_space and size < found_size:
      found_size = size

  return found_size

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f'test answer:', test_answer)
assert test_answer == 24933642

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f'answer:', answer)
assert answer == 2568781
