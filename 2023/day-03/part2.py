import re
from collections import defaultdict
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

    found_gears = defaultdict(list)
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

    for coords in num_coords:
        num, y, x = coords

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

                if check_char == "*":
                    found_gears[(new_y, new_x)].append(num)
                    found_symbol = True
                    break

            if found_symbol:
                break

    output = 0
    for nums in found_gears.values():
        if len(nums) != 2:
            continue

        output += int(nums[0]) * int(nums[1])

    return output


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 467835

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 74528807
