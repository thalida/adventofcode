import itertools
from pathlib import Path

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

def subsections(num, parts):
    sums = []
    part = num // parts

    for idx in range(parts):
        sums[idx] = [part]





def process(inputs):
    operational = "."
    damaged = "#"
    unknown = "?"


    num_arragements = 0
    # for idx, line in enumerate(inputs):


    for idx, line in enumerate(inputs):
        conditions, counts_str = line.split()
        counts = [int(count) for count in counts_str.split(",")]

        leading_dots = 0 if conditions.startswith(damaged) else 1
        trailing_dots = 0 if conditions.endswith(damaged) else 1

        damage_sets = ["#" * count for count in counts]

        num_operational = conditions.count(operational)
        num_damaged = conditions.count(damaged)
        num_unknowns = conditions.count(unknown)

        num_missing_cells = len(conditions) - sum(counts)
        num_gaps = len(damage_sets) - 1 + leading_dots + trailing_dots
        num_missing_cells_2 = len(conditions) - (num_operational + sum(counts))
        # combos = list(itertools.permutations(range(1, num_missing_cells), num_gaps))
        combos = list(itertools.combinations_with_replacement(range(1, num_missing_cells), num_gaps))
        valid_combos = [combo for combo in combos if sum(combo) == num_missing_cells]
        # combos = [sum(combo) for combo in combos if sum(combo) == num_missing_cells]
        # combos = list(itertools.combinations(range(1, num_missing_cells + 1), num_missing_cells))


        print(conditions)
        print(damage_sets)
        print(combos)
        print(valid_combos)
        # print(num_missing_cells, (len(damage_sets) // 2), num_gaps)
        print(num_gaps, leading_dots, trailing_dots, num_missing_cells, num_unknowns, num_missing_cells_2)


    return num_arragements


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 21

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 0
