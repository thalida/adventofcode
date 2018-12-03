# https://adventofcode.com/2018/day/1

import os
script_dir = os.path.dirname(__file__)

inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
    inputs = f.read().splitlines()

def find_sum(inputs, sums, prev_sum):
    for n in inputs:
        curr_sum = int(n) + prev_sum
        if curr_sum in sums:
            return {'found': True, 'answer': curr_sum}
        sums.add(curr_sum)
        prev_sum = curr_sum
    return {'found': False, 'sums': sums, 'prev_sum': prev_sum}

def run(inputs, sums={0}, prev_sum=0):
    res = find_sum(inputs, sums, prev_sum)
    return res['answer'] if res['found'] else run(inputs, res['sums'], res['prev_sum'])

print(run(inputs))
