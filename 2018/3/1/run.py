# https://adventofcode.com/2018/day/3

import os
import functools
import re
from collections import defaultdict

script_dir = os.path.dirname(__file__)

inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()
regex = r"(\d*),(\d*)\:\s(\d*)x(\d*)"

def run(inputs):
    fabric = defaultdict(dict)
    overlaping = set()
    for s in inputs:
        m = re.search(regex, s)
        x, y, w, h = m.groups()
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)

        for nx in range(x, x+w):
            for ny in range(y, y+h):
                if fabric.get(nx, {}).get(ny):
                    overlaping.add((nx, ny))
                else:
                    fabric[nx][ny] = True
    return len(overlaping)

print(run(inputs))

