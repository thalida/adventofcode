from collections import defaultdict
from pathlib import Path

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample_2.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs


def process(inputs):
    directions = inputs[0]
    nodes = defaultdict(list)

    for line in inputs[2:]:
        node, neighbors = line.split(" = ")
        neighbors = neighbors.replace("(", "").replace(")", "").split(", ")
        nodes[node] = neighbors

    steps = 0
    current = "AAA"
    dest = "ZZZ"
    num_directions = len(directions)
    while current != dest:
        d = directions[steps % num_directions]
        n = 0 if d == "L" else 1
        current = nodes[current][n]
        steps += 1

    return steps


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 6

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 22411
