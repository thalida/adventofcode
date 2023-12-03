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
    output = 0

    num_map = []

    for line_idx, line in enumerate(inputs):
        num_start = None
        num_end = None
        for idx, char in enumerate(line):
            if not char.isdigit():
                continue

            if num_start is None:
                num_start = idx

            next_char = line[idx + 1] if idx + 1 < len(line) else None
            next_char_is_digit = next_char is not None and next_char.isdigit()

            if next_char_is_digit:
                continue

            num_end = idx

            found_num = line[num_start : (num_end + 1)]
            num_map.append((found_num, line_idx, num_start))

            num_start = None
            num_end = None

    found_gears = defaultdict(list)

    for idx, num_set in enumerate(num_map):
        num, line_idx, num_start = num_set

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

        for char_idx, char in enumerate(str(num)):
            found_symbol = False

            for direction in search_directions:
                line_idx_offset, num_start_offset = direction

                new_line_idx = line_idx + line_idx_offset
                new_num_start = num_start + num_start_offset + char_idx

                if new_line_idx < 0 or new_line_idx >= len(inputs):
                    continue

                if new_num_start < 0 or new_num_start >= len(inputs[new_line_idx]):
                    continue

                check_char = inputs[new_line_idx][new_num_start]

                if check_char == "*":
                    found_gears[(new_line_idx, new_num_start)].append(num)
                    found_symbol = True
                    break

            if found_symbol:
                break

    for gear, nums in found_gears.items():
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
