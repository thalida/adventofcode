# https://adventofcode.com/2018/day/3

import os
import functools
import re
from collections import defaultdict

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(inputs):
    regex = r"(\d*)\s\@\s(\d*),(\d*)\:\s(\d*)x(\d*)"
    fabric = defaultdict(lambda: defaultdict(set))
    all_ids = set()
    overlaping_ids = set()
    for s in inputs:
        m = re.search(regex, s)
        fid, x, y, w, h = m.groups()
        fid = int(fid)
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        all_ids.add(fid)
        for nx in range(x, x+w):
            for ny in range(y, y+h):
                already_has = fabric.get(nx, {}).get(ny);
                fabric[nx][ny].add(fid)

                if already_has:
                    all_ids -= fabric[nx][ny]
    return all_ids

print(run(inputs))

