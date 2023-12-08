import math
from collections import defaultdict
from pathlib import Path

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample_3.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs


def process(inputs):
    directions = inputs[0]
    nodes = defaultdict(list)
    start_nodes = []

    for line in inputs[2:]:
        node, neighbors = line.split(" = ")
        neighbors = neighbors.replace("(", "").replace(")", "").split(", ")
        nodes[node] = neighbors

        if node.endswith("A"):
            start_nodes.append(node)

    steps = 0
    steps_to_end = []
    num_directions = len(directions)
    open_nodes = start_nodes
    while len(open_nodes) > 0:
        d = directions[steps % num_directions]
        n = 0 if d == "L" else 1

        next_nodes = []
        next_step = steps + 1
        for node in open_nodes:
            next_node = nodes[node][n]

            if next_node.endswith("Z"):
                steps_to_end.append(next_step)
                continue

            next_nodes.append(next_node)

        open_nodes = next_nodes.copy()
        steps = next_step

    return math.lcm(*steps_to_end)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 6

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 11188774513823
