# https://adventofcode.com/2018/day/_d

import os

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(inputs):
    output = 'day/_d'
    return output

print(run(inputs))
