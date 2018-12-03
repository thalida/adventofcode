# https://adventofcode.com/2018/day/1

import os
import functools
script_dir = os.path.dirname(__file__)

inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

twice = 0
thrice = 0

for s in inputs:
    chars = list(s)
    unique_chars = set(chars)

    if len(unique_chars) == len(chars):
        print('here')
        continue

    foundTwice = False
    foundThrice = False
    for c in unique_chars:
        counts = chars.count(c)

        if foundTwice and foundThrice:
            break;

        if not foundTwice and counts == 2:
            foundTwice = True
            twice += 1

        if not foundThrice and counts == 3:
            foundThrice = True
            thrice += 1

answer = twice * thrice
print(answer, '=', twice, '*', thrice)
