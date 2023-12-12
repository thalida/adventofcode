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
        open_pos = None
        close_pos = None
        history.append([])
        for col, symbol in enumerate(line):
            pos = (row, col)

            if row == 0 or row == num_rows - 1 or col == 0 or col == num_cols - 1:
                continue

            if pos not in pipe:
                if open_pos is not None and close_pos is None:
                    num_open += 1
                continue

            if open_pos is None:
                open_pos = pos
                history[-1].append(open_pos)
                continue

            more_pipes = False
            for c in range(1, num_cols - col):
                p = (row, col + c)
                if p in pipe:
                    more_pipes = True
                    break

            if not more_pipes:
                close_pos = pos
                history[-1].append(close_pos)
                continue

            if open_pos is not None and close_pos is None:
                open_symbol = inputs[open_pos[0]][open_pos[1]]
                if "e" in valid_directions[open_symbol] and symbol in valid_directions[open_symbol]["e"]:
                    open_pos = pos
                    continue

                close_pos = pos
                history[-1].append(close_pos)
                continue

            # if close_pos is not None and open_pos is not None:
            close_symbol = inputs[close_pos[0]][close_pos[1]]
            if "e" in valid_directions[close_symbol] and symbol in valid_directions[close_symbol]["e"]:
                close_pos = pos
                continue


            open_pos = None
            close_pos = None

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
