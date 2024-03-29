from pathlib import Path

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_1_FILENAME = "inputs_sample_2_1.txt"
SAMPLE_INPUTS_2_FILENAME = "inputs_sample_2_2.txt"
SAMPLE_INPUTS_3_FILENAME = "inputs_sample_2_3.txt"
SAMPLE_INPUTS_4_FILENAME = "inputs_sample_2_4.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs

def process(inputs):
    valid_directions = {
        "S": { "n": ["|", "7", "F"], "s": ["|", "L", "J"], "e": ["-", "J", "7"], "w": ["-", "L", "F"]},
        "|": {"n": ["7", "F", "|"], "s": ["L", "J", "|"]},
        "-": {"e": ["J", "7", "-"], "w": ["L", "F", "-"]},
        "L": {"n": ["|", "7", "F"], "e": ["-", "J", "7"]},
        "J": {"n": ["|", "7", "F"], "w": ["-", "L", "F"]},
        "7": {"s": ["|", "L", "J"], "w": ["-", "L", "F"]},
        "F": {"s": ["|", "L", "J"], "e": ["-", "J", "7"]},
        ".": {},
    }

    end_symbol_map = {
        "S": ["|", "L", "F"],
        "|": ["S", "|", "-", "L", "J", "7", "F"],
        "-": ["S", "|", "L", "J", "F"],
        "L": ["S", "|", "L", "J", "F"],
        "J": ["S", "|", "-", "L", "J", "7", "F"],
        "7": ["S", "|", "-", "L", "J", "7", "F"],
        "F": ["S", "|", "L", "7", "F"],
    }

    starting_pos = (0, 0)
    for idx, line in enumerate(inputs):
        if "S" in line:
            starting_pos = (idx, line.index("S"))
            break

    num_rows = len(inputs)
    num_cols = len(inputs[0])
    seen_pipes = set()
    pipe = []
    pos = starting_pos
    while pos is not None:
        pipe.append(pos)
        seen_pipes.add(pos)
        curr_symbol = inputs[pos[0]][pos[1]]

        options = [
            ["s", (pos[0] + 1, pos[1])],
            ["w", (pos[0], pos[1] - 1)],
            ["n", (pos[0] - 1, pos[1])],
            ["e", (pos[0], pos[1] + 1)],
        ]

        next_pos = None

        for direction, check_pos in options:
            if check_pos[0] < 0 or check_pos[0] >= num_rows:
                continue

            if check_pos[1] < 0 or check_pos[1] >= num_cols:
                continue

            if direction not in valid_directions[curr_symbol].keys():
                continue

            if check_pos in seen_pipes:
                continue

            valid_symbols = valid_directions[curr_symbol][direction]
            if inputs[check_pos[0]][check_pos[1]] in valid_symbols:
                next_pos = check_pos
                break

        pos = next_pos


    # pipe.append(pipe[0])
    print("Found pipe!")

    num_open = 0
    history  = []
    for row, line in enumerate(inputs):
        if row == 0 or row == num_rows - 1:
            continue

        open_pos = None
        closed_on = None
        history.append([])

        first_pipe_in_row = None
        last_pipe_in_row = None
        for col, symbol in enumerate(line):
            pos = (row, col)

            if pos not in pipe:
                continue

            if first_pipe_in_row is None:
                first_pipe_in_row = pos

            last_pipe_in_row = pos

        print("first_pipe_in_row:", first_pipe_in_row, "last_pipe_in_row:", last_pipe_in_row)

        for col, symbol in enumerate(line):
            pos = (row, col)

            if pos[1] < first_pipe_in_row[1] or pos[1] > last_pipe_in_row[1]:
                continue

            if pos not in pipe:
                closed_on = None
                if open_pos is not None:
                    num_open += 1
                    print("pos:", pos, num_open)
                continue

            if open_pos is None and closed_on is not None:
                closed_on_symbol = inputs[closed_on[0]][closed_on[1]]
                if symbol in end_symbol_map[closed_on_symbol]:
                    closed_on = pos
                    continue

                if symbol not in end_symbol_map[closed_on_symbol]:
                    continue

            if open_pos is None:
                open_pos = pos
                closed_on = None
                history[-1].append(open_pos)
                continue

            open_symbol = inputs[open_pos[0]][open_pos[1]]
            if symbol in end_symbol_map[open_symbol]:
                history[-1].append(pos)
                closed_on = pos
                open_pos = None



    print("history:", history)
    print("num_open:", num_open)
    return num_open


print("running test 1...")
test_inputs = get_inputs(filename=SAMPLE_INPUTS_1_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 4

print("running test 2...")
test_inputs = get_inputs(filename=SAMPLE_INPUTS_2_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 4

print("running test 3...")
test_inputs = get_inputs(filename=SAMPLE_INPUTS_3_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 8

print("running test 4...")
test_inputs = get_inputs(filename=SAMPLE_INPUTS_4_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 10

print("running actual...")
inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 690 # too high
