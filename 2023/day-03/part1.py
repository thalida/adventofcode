import re
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


def process(inputs):
    num_coords = []

    for y, line in enumerate(inputs):
        for m in re.finditer(r"\d+", line):
            num_coords.append((m.group(0), y, m.start()))

    has_symbol = []

    search_directions = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1],
    ]

    for coord in num_coords:
        num, y, x = coord

        for char_idx in range(len(num)):
            found_symbol = False

            for direction in search_directions:
                y_offset, x_offset = direction

                new_y = y + y_offset
                new_x = x + x_offset + char_idx

                if new_y < 0 or new_y >= len(inputs):
                    continue

                if new_x < 0 or new_x >= len(inputs[new_y]):
                    continue

                check_char = inputs[new_y][new_x]

                if not check_char.isdigit() and check_char != ".":
                    has_symbol.append(int(num))
                    found_symbol = True
                    break

            if found_symbol:
                break

    return sum(has_symbol)


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 4361

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 519444
