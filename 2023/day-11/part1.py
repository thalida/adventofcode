from pathlib import Path
import itertools

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs


def process(inputs):
    expand_h = []
    for line in inputs:
        expand_h.append(list(line))
        if set(line) == set("."):
            expand_h.append(list(line))

    expand_v = []
    for col in range(len(expand_h[0])):
        expand_v.append([])
        for row in range(len(expand_h)):
            expand_v[-1].append(expand_h[row][col])

        if set(expand_v[-1]) == set("."):
            expand_v.append(expand_v[-1])

    grid = expand_v.copy()

    galaxies = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                galaxies.append((row, col))

    combos = list(itertools.combinations(galaxies, 2))
    min_dists = []
    for combo in combos:
        drow = abs(combo[1][0] - combo[0][0])
        dcol = abs(combo[1][1] - combo[0][1])
        d = drow + dcol
        min_dists.append(d)

    return sum(min_dists)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 374

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 9521550
