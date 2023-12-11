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


def process(inputs, multi=2):
    empty_rows = []
    for row, line in enumerate(inputs):
        if set(line) == set("."):
            empty_rows.append(row)

    empty_cols = []
    for col in range(len(inputs[0])):
        col_chars = []
        for row in range(len(inputs)):
            col_chars.append(inputs[row][col])
        if set(col_chars) == set("."):
            empty_cols.append(col)


    galaxies = []
    for row, line in enumerate(inputs):
        for col, char in enumerate(line):
            if char != "#":
                continue

            num_empty_rows_before = sum([1 for empty_row in empty_rows if empty_row < row])
            num_empty_cols_before = sum([1 for empty_col in empty_cols if empty_col < col])

            row_offset = (num_empty_rows_before * multi) - num_empty_rows_before
            col_offset = (num_empty_cols_before * multi) - num_empty_cols_before

            galaxies.append((row+row_offset, col+col_offset))

    combos = list(itertools.combinations(galaxies, 2))
    min_dists = []
    for combo in combos:
        drow = abs(combo[1][0] - combo[0][0])
        dcol = abs(combo[1][1] - combo[0][1])
        d = drow + dcol
        min_dists.append(d)

    return sum(min_dists)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, 2)
print("test answer:", test_answer)
assert test_answer == 374

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, 10)
print("test answer:", test_answer)
assert test_answer == 1030

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs, 100)
print("test answer:", test_answer)
assert test_answer == 8410

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs, 1000000)
print("answer:", answer)
assert answer == 298932923702
