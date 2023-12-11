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


    pipe.append(pipe[0])
    print("Found pipe!")

    insides = []
    for row, line in enumerate(inputs):
        insides.append([])
        for col, char in enumerate(line):
            pos = (row, col)

            if pos in pipe:
                continue

            if pos[0] <= 0 or pos[0] >= num_rows:
                continue

            if pos[1] <= 0 or pos[1] >= num_cols:
                continue

            # print(pos)

            left_walls = []
            for i in range(col):
                prev_wall = left_walls[-1] if len(left_walls) > 0 else None
                check_pos = (row, i)

                if check_pos not in pipe:
                    continue

                if inputs[check_pos[0]][check_pos[1]] == "-":
                    continue

                is_first = len(left_walls) == 0
                if is_first:
                    left_walls.append(check_pos)
                    continue


                if prev_wall is not None:
                    is_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                    if is_start and ((pipe.index(check_pos) == 1) or pipe.index(check_pos) == len(pipe) - 2):
                        continue

                    if not is_start and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
                        continue

                left_walls.append(check_pos)

            right_walls = []
            for i in range(col, num_cols):
                prev_wall = right_walls[-1] if len(right_walls) > 0 else None
                check_pos = (row, i)

                if check_pos not in pipe:
                    continue

                if inputs[check_pos[0]][check_pos[1]] == "-":
                    continue

                is_last = check_pos[1] == num_cols - 1
                if is_last:
                    right_walls.append(check_pos)
                    continue

                if prev_wall is not None:
                    is_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                    if is_start and ((pipe.index(check_pos) == 1) or pipe.index(check_pos) == len(pipe) - 2):
                        continue

                    if not is_start and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
                        continue

                right_walls.append(check_pos)

            top_walls = []
            for i in range(row):
                prev_wall = top_walls[-1] if len(top_walls) > 0 else None
                check_pos = (i, col)

                if check_pos not in pipe:
                    continue

                if inputs[check_pos[0]][check_pos[1]] == "|":
                    continue

                top_walls.append(check_pos)


            bottom_walls = []
            for i in range(row, num_rows):
                prev_wall = bottom_walls[-1] if len(bottom_walls) > 0 else None
                check_pos = (i, col)

                if check_pos not in pipe:
                    continue

                if inputs[check_pos[0]][check_pos[1]] == "|":
                    continue

                bottom_walls.append(check_pos)

            # print("left_walls:", left_walls, "right_walls:", right_walls, "top_walls:", top_walls, "bottom_walls:", bottom_walls)

            if len(left_walls) == 0 or len(right_walls) == 0 or len(top_walls) == 0 or len(bottom_walls) == 0:
                insides[row].append((pos, False))
                # print("------")
                continue


            is_odd_left = len(left_walls) % 2 == 1
            is_odd_right = len(right_walls) % 2 == 1
            is_odd_top = len(top_walls) % 2 == 1
            is_odd_bottom = len(bottom_walls) % 2 == 1
            is_inside = is_odd_left or is_odd_right or is_odd_top or is_odd_bottom
            # print("is_odd_left:", is_odd_left, "is_odd_right:", is_odd_right, "is_odd_top:", is_odd_top, "is_odd_bottom:", is_odd_bottom)
            # print("------")

            insides[row].append((pos, is_inside))

    print("Found insides!")
    # print("insides:", insides)

    num_inside = 0
    for row in insides:
        for pos, is_inside in row:
            if is_inside:
                num_inside += 1

    return num_inside

    # return abs((b-a)/2)

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
assert answer == 7145
