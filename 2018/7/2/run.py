# https://adventofcode.com/2018/day/7

from collections import defaultdict
from pprint import pprint
import re
import os

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

# inputs = [
# "Step C must be finished before step A can begin.",
# "Step C must be finished before step F can begin.",
# "Step A must be finished before step B can begin.",
# "Step A must be finished before step D can begin.",
# "Step B must be finished before step E can begin.",
# "Step D must be finished before step E can begin.",
# "Step F must be finished before step E can begin.",
# ]

def assign_work(ticks, workers, steps, potential_next_steps, inprogress_steps, completed_steps):
    multiplier = 60
    num_workers = len(workers)
    for i, w in enumerate(workers):
        if w is not None:
            step, wait = w
            new_wait = wait - 1
            if new_wait == 0:
                inprogress_steps.remove(step)
                completed_steps.add(step)
                potential_next_steps = (potential_next_steps | steps[step]) - completed_steps
                workers[i] = None
            else:
                workers[i] = (step, new_wait)
                continue

        next_steps = []
        sorted_potential = sorted(potential_next_steps)
        for skey in sorted_potential:
            depends_on = {k for k, v in steps.items() if skey in v}
            if len(depends_on - completed_steps) == 0:
                next_steps.append(skey)
                continue

        if len(next_steps) == 0:
            continue

        step = next_steps[0]
        wait = ord(step.upper()) - ord('A') + 1 + multiplier
        workers[i] = (step, wait)
        inprogress_steps.add(step)
        potential_next_steps -= inprogress_steps

        if i == num_workers - 1 and len(set(next_steps) - inprogress_steps) > 0 and None in workers:
            return assign_work(ticks, workers, steps, potential_next_steps, inprogress_steps, completed_steps)

    return (ticks, workers, steps, potential_next_steps, inprogress_steps, completed_steps)

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

    num_workers = 5
    workers = [None] * num_workers
    ticks = -1
    first_loop = True

    potential_next_steps = all_steps - depends_on_something
    completed_steps = set()
    inprogress_steps = set()
    while True:
        if len(all_steps - completed_steps) == 0:
            break;
        else:
            ticks += 1
        
        ticks, workers, steps, potential_next_steps, inprogress_steps, completed_steps = assign_work(ticks, workers, steps, potential_next_steps, inprogress_steps, completed_steps)

    return ticks

print(run(inputs))
