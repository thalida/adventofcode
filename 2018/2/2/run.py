# https://adventofcode.com/2018/day/2

import os
import functools
script_dir = os.path.dirname(__file__)

inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(): 
    for i1, s1 in enumerate(inputs):
        len_1 = len(s1)
        for i2, s2 in enumerate(inputs[i1+1:]):
            len_2 = len(s2)

            if len_1 != len_2:
                continue

            chars_1 = set([(i, c) for i, c in enumerate(s1)])
            chars_2 = set([(i, c) for i, c in enumerate(s2)])

            intersection = chars_1 & chars_2
            if len(intersection) + 1 == len_1:
                bad_char = list(chars_1 - intersection)[0][0]
                output = list(s1).copy()
                del output[bad_char]
                return ''.join(output)

print(run())

