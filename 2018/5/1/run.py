# https://adventofcode.com/2018/day/5
import pprint
import os
import functools
import re
from collections import defaultdict

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(s):
    i = 0
    while True:
        try:
            a, b = (s[i], s[i+1])
        except IndexError:
            break

        if abs(ord(a) - ord(b)) == 32:
            s = s[:i] + s[i+2:]
            i = i - 1 if i > 0 else 0
        else:
            i += 1

    return len(s)

print(run("dabAcCaCBAcCcaDA"))
print(run("pQqGgPzZWwSoOsgYLfFjJlypPGXxdDGhHBFfbLlcCGghHNnBbl"))
print(run(inputs[0]))
