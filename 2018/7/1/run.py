# https://adventofcode.com/2018/day/7

from collections import defaultdict
from pprint import pprint
import re
import os

script_dir = os.path.dirname(__file__)
inputs = []
# with open(os.path.join(script_dir,'input.txt'), 'r') as f:
with open(os.path.join(script_dir,'eddy-input.txt'), 'r') as f:
  inputs = f.read().splitlines()

# inputs = [
# "Step G must be finished before step A can begin.",
# "Step C must be finished before step F can begin.",
# "Step A must be finished before step B can begin.",
# "Step A must be finished before step D can begin.",
# "Step B must be finished before step E can begin.",
# "Step D must be finished before step E can begin.",
# "Step F must be finished before step E can begin.",
# ]

def run(inputs):  
    regex = r"Step\s(.{1}).*step\s(.{1})"
    steps = defaultdict(set)
    all_steps = set()
    depends_on_something = set()
    for direction in inputs:
        step_1, step_2 = re.search(regex, direction).groups()
        all_steps.add(step_1)
        all_steps.add(step_2)
        depends_on_something.add(step_2)
        steps[step_1].add(step_2)

    potential_next_steps = all_steps - depends_on_something
    completed_steps = set()
    order = []
    while potential_next_steps:
        step = None
        sorted_potential = sorted(potential_next_steps)
        available_steps = []
        for skey in sorted_potential:
            depends_on = {k for k, v in steps.items() if skey in v}
            if len(depends_on - completed_steps) == 0:
                available_steps.append(skey)
                continue;

        step = available_steps[0]
        order.append(step)
        completed_steps.add(step)
        potential_next_steps = (potential_next_steps | steps[step]) - completed_steps

    return "".join(order)

print(run(inputs))
