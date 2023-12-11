from pathlib import Path

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample_1_1.txt"
SAMPLE_INPUTS_2_FILENAME = "inputs_sample_1_2.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
#
#
# valid_directions = {
#     "S": { "n": ["|", "7", "F"], "s": ["|", "L", "J"], "e": ["-", "J", "7"], "w": ["-", "L", "F"]},
#     "|": {"n": ["7", "F", "|"], "s": ["L", "J", "|"]},
#     "-": {"e": ["J", "7", "-"], "w": ["L", "F", "-"]},
#     "L": {"n": ["|", "7", "F"], "e": ["-", "J", "7"]},
#     "J": {"n": ["|", "7", "F"], "w": ["-", "L", "F"]},
#     "7": {"s": ["|", "L", "J"], "w": ["-", "L", "F"]},
#     "F": {"s": ["|", "L", "J"], "e": ["-", "J", "7"]},
#     ".": {},
# }

def process(inputs):
    valid_directions = {
        "S": { "n": ["|", "7", "F"], "s": ["|", "L", "J"], "e": ["-", "J", "7"], "w": ["-", "L", "F"]},
        "|": ["n", "s"],
        "-": ["e", "w"],
        "L": ["n", "e"],
        "J": ["n", "w"],
        "7": ["s", "w"],
        "F": ["s", "e"],
        ".": [],
    }


    starting_pos = (0, 0)
    for idx, line in enumerate(inputs):
        if "S" in line:
            starting_pos = (idx, line.index("S"))
            break

    num_rows = len(inputs)
    num_cols = len(inputs[0])
    pipe = set()
    pos = starting_pos
    while pos is not None:
        pipe.add(pos)
        curr_symbol = inputs[pos[0]][pos[1]]
        is_start = curr_symbol == "S"

        options = [
            ["n", (pos[0] - 1, pos[1])],
            ["s", (pos[0] + 1, pos[1])],
            ["e", (pos[0], pos[1] + 1)],
            ["w", (pos[0], pos[1] - 1)],
        ]

        next_pos = None

        for direction, check_pos in options:
            if check_pos[0] < 0 or check_pos[0] >= num_rows:
                continue

            if check_pos[1] < 0 or check_pos[1] >= num_cols:
                continue

            if direction not in valid_directions[curr_symbol]:
                continue

            if check_pos in pipe:
                continue

            is_valid_start_symbol = False
            if is_start:
                valid_symbols = valid_directions[curr_symbol][direction]
                is_valid_start_symbol = inputs[check_pos[0]][check_pos[1]] in valid_symbols

            if not is_start or (is_start and is_valid_start_symbol):
                next_pos = check_pos
                break

        pos = next_pos

    return int(len(pipe) / 2)

test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 4

test_inputs = get_inputs(filename=SAMPLE_INPUTS_2_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 8

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 7145
