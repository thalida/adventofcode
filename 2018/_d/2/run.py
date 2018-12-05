# https://adventofcode.com/2018/day/_d

import pprint
import os
import functools
import re
from collections import defaultdict

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(inputs):
    output = 'day/_d'
    return output

print(run(inputs))
