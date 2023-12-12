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

    h_walls = []
    v_walls = []

    for row, line in enumerate(inputs):
        h_walls.append([])

        last_pos = None
        for col in range(len(line)):
            prev_wall = h_walls[row][-1] if len(h_walls[row]) > 0 else None
            curr_pos = (row, col)

            if curr_pos not in pipe:
                continue

            if inputs[curr_pos[0]][curr_pos[1]] == "-":
                continue

            last_pos = curr_pos

            is_first = len(h_walls[row]) == 0
            if is_first:
                h_walls[row].append(curr_pos)
                continue

            if prev_wall is not None:
                is_prev_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                if is_prev_start and ((pipe.index(curr_pos) == 1) or pipe.index(curr_pos) == len(pipe) - 1):
                    continue

                is_curr_start = inputs[curr_pos[0]][curr_pos[1]] == "S"
                if is_curr_start and ((pipe.index(prev_wall) == 1) or pipe.index(prev_wall) == len(pipe) - 1):
                    continue

                if not is_prev_start and not is_curr_start and abs(pipe.index(prev_wall) - pipe.index(curr_pos)) == 1:
                    continue

            h_walls[row].append(curr_pos)

        if last_pos is not None and h_walls[row][-1] != last_pos:
            h_walls[row].append(last_pos)

    for col in range(num_cols):
        v_walls.append([])

        last_pos = None
        for row in range(num_rows):
            prev_wall = v_walls[col][-1] if len(v_walls[col]) > 0 else None
            curr_pos = (row, col)

            if curr_pos not in pipe:
                continue

            if inputs[curr_pos[0]][curr_pos[1]] == "|":
                continue

            last_pos = curr_pos

            is_first = len(v_walls[col]) == 0
            is_last = curr_pos[0] == num_rows - 1

            if is_first or is_last:
                v_walls[col].append(curr_pos)
                continue

            if prev_wall is not None:
                is_prev_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                if is_prev_start and ((pipe.index(curr_pos) == 1) or pipe.index(curr_pos) == len(pipe) - 1):
                    continue

                is_curr_start = inputs[curr_pos[0]][curr_pos[1]] == "S"
                if is_curr_start and ((pipe.index(prev_wall) == 1) or pipe.index(prev_wall) == len(pipe) - 1):
                    continue

                # if not is_prev_start and not is_curr_start and abs(pipe.index(prev_wall) - pipe.index(curr_pos)) == 1:
                #     continue

                # is_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                # if is_start and ((pipe.index(curr_pos) == 1) or pipe.index(curr_pos) == len(pipe) - 2):
                #     continue

                # if not is_start and abs(pipe.index(prev_wall) - pipe.index(curr_pos)) == 1:
                #     continue

            v_walls[col].append(curr_pos)

        if last_pos is not None and v_walls[col][-1] != last_pos:
            v_walls[col].append(last_pos)

    print("Found walls!")
    print("h_walls:", h_walls)

    # insides = []
    # for row, line in enumerate(inputs):
    #     insides.append([])
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         if pos in pipe:
    #             continue

    #         if pos[0] <= 0 or pos[0] >= num_rows - 1:
    #             continue

    #         if pos[1] <= 0 or pos[1] >= num_cols - 1:
    #             continue

    #         print("pos:", pos)

    #         h_wall = h_walls[row].copy()
    #         v_wall = v_walls[col].copy()

    #         h_wall.append(pos)
    #         v_wall.append(pos)

    #         h_wall.sort(key=lambda p: p[1])
    #         v_wall.sort(key=lambda p: p[0])

    #         h_idx = h_wall.index(pos)
    #         left_wall = h_wall[:h_idx] if h_idx > 0 else None
    #         right_wall = h_wall[h_idx + 1:] if h_idx < len(h_wall) - 1 else None

    #         print("left_wall:", left_wall, "right_wall:", right_wall)

    #         v_idx = v_wall.index(pos)
    #         top_wall = v_wall[:v_idx] if v_idx > 0 else None
    #         bottom_wall = v_wall[v_idx + 1:] if v_idx < len(v_wall) - 1 else None

    #         print("top_wall:", top_wall, "bottom_wall:", bottom_wall)

    #         if left_wall is None or right_wall is None or top_wall is None or bottom_wall is None:
    #             insides[row].append((pos, False))
    #             print("----")
    #             continue

    #         is_odd_top = len(top_wall) % 2 == 1
    #         is_odd_bottom = len(bottom_wall) % 2 == 1
    #         is_odd_left = len(left_wall) % 2 == 1
    #         is_odd_right = len(right_wall) % 2 == 1
    #         is_inside = is_odd_top or is_odd_bottom or is_odd_left or is_odd_right
    #         print("is_odd_top:", is_odd_top, "is_odd_bottom:", is_odd_bottom, "is_odd_left:", is_odd_left, "is_odd_right:", is_odd_right)
    #         print("----")

    #         insides[row].append((pos, is_inside))

    # print("Found insides!")
    # print("insides:", insides)

    # num_inside = 0
    # for row in insides:
    #     for pos, is_inside in row:
    #         if is_inside:
    #             num_inside += 1

    return num_inside

    # return abs((b-a)/2)

# print("running test 1...")
# test_inputs = get_inputs(filename=SAMPLE_INPUTS_1_FILENAME)
# test_answer = process(test_inputs)
# print("test answer:", test_answer)
# assert test_answer == 4

# print("running test 2...")
# test_inputs = get_inputs(filename=SAMPLE_INPUTS_2_FILENAME)
# test_answer = process(test_inputs)
# print("test answer:", test_answer)
# assert test_answer == 4

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
