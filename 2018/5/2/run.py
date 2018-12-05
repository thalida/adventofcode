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

def poly_reduce(s, skip):
    str_arr = list(s)
    i = 0
    while True:
        try:
            a, b = (str_arr[i], str_arr[i+1])
            if a.lower() == skip:
                del str_arr[i:i+1]
                continue
            if b.lower() == skip:
                del str_arr[i+1:i+2]
                continue
        except IndexError:
            break

        if abs(ord(a) - ord(b)) == 32:
            del str_arr[i:i+2]
            i = i - 1 if i > 0 else 0
        else:
            i += 1

    return len(str_arr)


def run(s):
    min_str = (None, None)
    unit_types = set(map(lambda x: x.lower(), list(set(s))))
    print('unit_types', unit_types)
    for letter in unit_types:
        str_len = poly_reduce(inputs[0], letter)
        print(letter, str_len)
        if min_str[1] is None or str_len < min_str[1]:
            min_str = (letter, str_len)

    return min_str

print('min:', run(inputs[0]))
