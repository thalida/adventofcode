# https://adventofcode.com/2018/day/1

import os
import functools
script_dir = os.path.dirname(__file__)

inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

answer = functools.reduce(lambda a,b : int(a)+int(b), inputs)
print(answer)
