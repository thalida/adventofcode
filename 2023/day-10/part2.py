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

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# x, y => col, row


def point_inside_polygon(row, col, poly, include_edges=True):
    '''
    Test if point (x,y) is inside polygon poly.

    poly is N-vertices polygon defined as
    [(x1,y1),...,(xN,yN)] or [(x1,y1),...,(xN,yN),(x1,y1)]
    (function works fine in both cases)

    Geometrical idea: point is inside polygon if horisontal beam
    to the right from point crosses polygon even number of times.
    Works fine for non-convex polygons.
    '''
    n = len(poly)
    inside = False

    p1row, p1col = poly[0]
    for i in range(1, n + 1):
        p2row, p2col = poly[i % n]
        if p1row == p2row:
            if row == p1row:
                if min(p1col, p2col) <= col <= max(p1col, p2col):
                    # point is on horisontal edge
                    inside = include_edges
                    break
                elif col < min(p1col, p2col):  # point is to the left from current edge
                    inside = not inside
        else:  # p1row!= p2row
            if min(p1row, p2row) <= row <= max(p1row, p2row):
                xinters = (row - p1row) * (p2col - p1col) / float(p2row - p1row) + p1col

                if col == xinters:  # point is right on the edge
                    inside = include_edges
                    break

                if col < xinters:  # point is to the left from current edge
                    inside = not inside

        p1col, p1row = p2col, p2row

    return inside

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

    insides = []
    for row, line in enumerate(inputs):
        insides.append([])
        for col, char in enumerate(line):
            pos = (row, col)

            if pos in pipe:
                continue

            if pos[0] <= 0 or pos[0] >= num_rows -1:
                continue

            if pos[1] <= 0 or pos[1] >= num_cols -1:
                continue

            print(pos)

            # is_inside = point_inside_polygon(row, col, pipe)

            # if not is_inside:
            #     continue

            left_walls = []
            for i in range(col):
                prev_wall = left_walls[-1] if len(left_walls) > 0 else None
                check_pos = (row, i)

                if check_pos not in pipe:
                    continue

                if inputs[check_pos[0]][check_pos[1]] == "-":
                    continue

                if prev_wall is not None and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
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

                if prev_wall is not None:
                    is_start = inputs[prev_wall[0]][prev_wall[1]] == "S"
                    if is_start and ((pipe.index(check_pos) == 1) or pipe.index(check_pos) == len(pipe) - 2):
                        continue

                # if row == 4 and prev_wall:
                #     print(prev_wall, inputs[prev_wall[0]][prev_wall[1]], check_pos, inputs[check_pos[0]][check_pos[1]])

                    if not is_start and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
                        continue

                right_walls.append(check_pos)

            # top_walls = []
            # for i in range(row):
            #     prev_wall = top_walls[-1] if len(top_walls) > 0 else None
            #     check_pos = (i, col)

            #     if check_pos not in pipe:
            #         continue

            #     if inputs[check_pos[0]][check_pos[1]] == "|":
            #         continue

            #     if prev_wall is not None and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
            #         continue

            #     top_walls.append(check_pos)


            # bottom_walls = []
            # for i in range(row, num_rows):
            #     prev_wall = bottom_walls[-1] if len(bottom_walls) > 0 else None
            #     check_pos = (i, col)

            #     if check_pos not in pipe:
            #         continue

            #     if inputs[check_pos[0]][check_pos[1]] == "|":
            #         continue

            #     if prev_wall is not None and abs(pipe.index(prev_wall) - pipe.index(check_pos)) == 1:
            #         continue

            #     bottom_walls.append(check_pos)

            # print("left_walls:", left_walls, "right_walls:", right_walls, "top_walls:", top_walls, "bottom_walls:", bottom_walls)

            # left_walls = [p for p in line if p in pipe and pos[1] < col and inputs[pos[0]][pos[1]] not in ["-"]]
            # right_walls = [p for p in line if p in pipe and pos[1] > col and inputs[pos[0]][pos[1]] not in ["-"]]

            # print("pos:", pos, "left_walls:", left_walls, "right_walls:", right_walls)
            # top_walls = [p for p in inputs if p in pipe and pos[0] < row and inputs[pos[0]][pos[1]]]
            # bottom_walls = [p for p in inputs if p in pipe and pos[0] > row and inputs[pos[0]][pos[1]]]

            # is_even_left = len(left_walls) % 2 == 0
            # is_even_right = len(right_walls) % 2 == 0
            # is_even_top = len(top_walls) % 2 == 0
            # is_even_bottom = len(bottom_walls) % 2 == 0

            # print("pos:", pos, "is_even_left:", is_even_left, "is_even_right:", is_even_right, "is_even_top:", is_even_top, "is_even_bottom:", is_even_bottom)

            # if is_even_left and is_even_right and is_even_top and is_even_bottom:
            #     continue


            is_odd_left = len(left_walls) % 2 == 1
            is_odd_right = len(right_walls) % 2 == 1
            # is_odd_top = len(top_walls) % 2 == 1
            # is_odd_bottom = len(bottom_walls) % 2 == 1

            # is_inside = is_odd_left or is_odd_right or is_odd_top or is_odd_bottom
            is_inside = is_odd_left or is_odd_right
            print("pos:", pos, "is_odd_left:", is_odd_left, "is_odd_right:", is_odd_right, "is_inside:", is_inside)
            # print("is_odd_left:", is_odd_left, "is_odd_right:", is_odd_right, "is_odd_top:", is_odd_top, "is_odd_bottom:", is_odd_bottom)
            print("------")

            # # if not is_odd_left and not is_odd_right and not is_odd_top and not is_odd_bottom:
            # #     continue

            # print("pos:", pos, "is_odd_left:", is_odd_left, "is_odd_right:", is_odd_right, "is_odd_top:", is_odd_top, "is_odd_bottom:", is_odd_bottom)

            # if is_odd_left or is_odd_right:
            #     continue

            # if is_odd_top or is_odd_bottom:
            #     continue

            insides[row].append((pos, is_inside))
    print("insides:", insides)

    # insides = []
    # for row, line in enumerate(inputs):
    #     insides.append([])
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         if pos in pipe:
    #             continue

    #         is_inside = point_inside_polygon(row, col, pipe)
    #         insides[row].append((pos, is_inside))

    # print("insides:", insides)


    # horz_wall_gaps = []
    # for row, line in enumerate(inputs):
    #     horz_wall_gaps.append([])
    #     prev_wall = None
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         if pos not in pipe:
    #             continue

    #         if prev_wall is None:
    #             prev_wall = pos
    #             continue

    #         horz_wall_gaps[row].append(col - prev_wall[1] - 1)
    #         prev_wall = None

    # print("horz_wall_gaps:", horz_wall_gaps)


    # vert_wall_gaps = []
    # for col in range(num_cols):
    #     vert_wall_gaps.append([])
    #     prev_wall = None
    #     for row in range(num_rows):
    #         pos = (row, col)

    #         if pos not in pipe:
    #             continue

    #         if prev_wall is None:
    #             prev_wall = pos
    #             continue

    #         vert_wall_gaps[col].append(row - prev_wall[0] - 1)
    #         prev_wall = None

    # print("vert_wall_gaps:", vert_wall_gaps)

    # for row, line in enumerate(inputs):
    #     for col, char in enumerate(line):
    #         pos = (row, col)
            # searched_directions = set()
            # while len(searched_directions) < 4:
            #     options = [
            #         ["n", (pos[0] - 1, pos[1])],
            #         ["s", (pos[0] + 1, pos[1])],
            #         ["e", (pos[0], pos[1] + 1)],
            #         ["w", (pos[0], pos[1] - 1)],
            #     ]

            #     next_pos = None

            #     searched_directions.add(direction)
            #     pos = next_pos




            # if pos in pipe:
            #     print("[green]" + char + "[/green]", end="")
            # else:
            #     print(char, end="")

    # def _area_(coords):
    #     t=0
    #     for count in range(len(coords)-1):
    #         row = coords[count+1][0] + coords[count][0]
    #         col = coords[count+1][1] - coords[count][1]
    #         z = row * col
    #         t += z
    #     return abs(t/2.0)

    # area = _area_(pipe)
    # print("area:", area)


    # def _area2_(coords):
    #     t=0
    #     for count in range(len(coords)-1):
    #         t += (coords[count][0] * coords[count+1][1]) - (coords[count][1] * coords[count+1][0])
    #     return abs(t/2.0)

    # area = _area2_(pipe)
    # print("area:", area)

    # def _area3_(vs):
    #     a = 0
    #     x0,y0 = vs[0]
    #     for [x1,y1] in vs[1:]:
    #         dx = x1-x0
    #         dy = y1-y0
    #         a += 0.5*(y0*dx - x0*dy)
    #         x0 = x1
    #         y0 = y1
    #     return a

    # area = _area3_(pipe)
    # print("area:", area)


    # def find_int_coordinates(n: int, coords: list[list[int]]) -> float:
    #     rez = 0
    #     row, col = coords[n - 1]
    #     for coord in coords:
    #         rez += (row + coord[0]) * (col - coord[1])
    #         row, col = coord
    #     return abs(rez / 2)


    # print("find_int_coordinates:", find_int_coordinates(len(pipe), pipe))


    # for row, line in enumerate(inputs):
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         if char == "F":
    #             char = "⎡"
    #         elif char == "J":
    #             char = "⎦"
    #         elif char == "L":
    #             char = "⎣"
    #         elif char == "7":
    #             char = "⎤"
    #         elif char == "|":
    #             char = "⏐"
    #         elif char == "-":
    #             char = "-"

    #         if pos in pipe:
    #             print(f"[b][green]{char}[/green][/b]", end="")
    #         else:
    #             print(".", end="")
    #     print()

    # pipe.append(pipe[0])
    # checked_pipe = []
    # for pos in pipe:
    #     check_difs = [
    #         (pos[0] + 1, pos[1]),
    #         (pos[0] - 1, pos[1]),
    #         (pos[0], pos[1] + 1),
    #         (pos[0], pos[1] - 1),
    #     ]

    #     for check_pos in check_difs:
    #         if check_pos not in pipe:
    #             continue

    #     print("pos:", pos, "pipe[pos]:", pos)


    # dr = 0
    # dc = 0
    # # diff_history = []
    # pipe.append(pipe[0])

    # for pos in range(len(pipe) // 2):
    #     pa = pipe[pos]
    #     pb = pipe[pos + 1]

    #     dr += pb[0] - pa[0]
    #     dc += pb[1] - pa[1]

    #     # diff_history.append((dr, dc))
    #     print("dr:", dr, "dc:", dc)

    #     # print("pa:", pa, "pb:", pb)



    # for row, line in enumerate(inputs):
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         p_copy = pipe.copy()
    #         p_copy.append(pos)
    #         p_copy.sort()

    #         index = p_copy.index(pos)
    #         print("index:", index, "pos:", pos)

    #         # if pos in pipe:
    #         #     print("[green]" + char + "[/green]", end="")
    #         # else:
    #         #     print(char, end="")
    #     print()


    # flow = []
    # for row, line in enumerate(inputs):
    #     last_pos = None
    #     flow.append([])
    #     for col, char in enumerate(line):
    #         pos = (row, col)

    #         if char == ".":
    #             flow[row].append(".")
    #             last_pos = pos
    #             continue

    #         if last_pos is None:
    #             flow[row].append("(")
    #             last_pos = pos
    #             continue

    #         if pos in pipe and last_pos not in pipe:
    #             flow[row].append("(")
    #             last_pos = pos
    #             continue

    #         if pos not in pipe:
    #             flow[row].append(char)
    #             last_pos = pos
    #             continue

    #         if pos in pipe and last_pos in pipe:
    #             last_idx = pipe.index(last_pos)
    #             curr_idx = pipe.index(pos)

    #             if last_idx < curr_idx:
    #                 flow[row].append("=")
    #                 last_pos = pos
    #                 continue

    #             flow[row].append(")")
    #             last_pos = last_pos
    #             continue

    # for row in flow:
    #     print("".join(row))
    # print("\n")



            # if pos in pipe:
            #     if last_pos is None:
            #         flow.append(pos)
            #         last_pos = pos
            #         continue

            #     last_idx = pipe.index(last_pos)
            #     curr_idx = pipe.index(pos)

            #     if last_idx < curr_idx:


            # if (i, j) in pipe:
            #     print("[green]" + char + "[/green]", end="")
            # else:
            #     print(char, end="")
        # print()


    # # search right
    # right_spaces = set()
    # for i, pos in enumerate(pipe):
    #     row = pos[0]
    #     col = pos[1]
    #     line = inputs[row]
    #     end_col = None

    #     for ei in range(col, len(line)):
    #         if (row, ei) in pipe:
    #             end_col = ei

    #     for ci, c in enumerate(line[col:end_col]):
    #         check_pos = (row, col + ci)

    #         if check_pos in pipe[i:]:
    #             continue

    #         right_spaces.add(check_pos)

    # left_spaces = set()
    # for i, pos in enumerate(pipe[::-1]):
    #     row = pos[0]
    #     col = pos[1]
    #     line = inputs[row]
    #     end_col = None

    #     for ei in range(0, col+1):
    #         if (row, ei) in pipe:
    #             end_col = ei
    #             break

    #     for ci, c in enumerate(line[end_col:col]):
    #         check_pos = (row, ci)

    #         if check_pos in pipe[i:]:
    #             continue

    #         left_spaces.add(check_pos)

    # print(right_spaces.intersection(left_spaces))

    # pipe.append(pipe[0])
    # allow_pos = [
    #     set(),
    #     set(),
    # ]
    # for pi in range(2):
    #     pipe = pipe if pi == 0 else pipe[::-1]
    #     for i, pos in enumerate(pipe):
    #         row = pos[0]
    #         col = pos[1]
    #         line = inputs[row]

    #         dset = []
    #         if pi == 0:
    #             dset = line[col:]
    #         else:
    #             dset = line[:col+1]

    #         for ci, c in enumerate(dset):
    #             check_pos = (row, col + ci)

    #             if check_pos in pipe[i:]:
    #                 continue

    #             allow_pos[pi].add(check_pos)

    # print("allow_pos:", allow_pos)
    # print(allow_pos[0].intersection(allow_pos[1]))



    # middle = len(pipe) // 2
    # segments = [
    #     pipe[:middle+1],
    #     pipe[middle:],
    # ]
    # brackets = []
    # is_open = True
    # for row, line in enumerate(inputs):
    #     brackets.append([])
    #     for col, char in enumerate(line):
    #         if char == ".":
    #             brackets[row].append(".")
    #             continue

    #         pos = (row, col)
    #         if pos not in pipe:
    #             brackets[row].append(char)
    #             continue

    #         # is_last_row = row == len(inputs) - 1
    #         is_last_col = col == len(line) - 1

    #         if is_last_col:
    #             brackets[row].append(")")
    #             is_open = True
    #             continue

    #         if is_open:
    #             brackets[row].append("(")
    #         else:
    #             brackets[row].append(")")

    #         is_open = not is_open

    #         # if pos in segments[0]:
    #         #     brackets[row].append("(")
    #         #     continue

    #         # if pos in segments[1]:
    #         #     brackets[row].append(")")
    #         #     continue

    # for row in inputs:
    #     print("".join(row))
    # print("\n")


    # for row in brackets:
    #     print("".join(row))
    # print("\n")


    # # flat_brackets = [char for row in brackets for char in row]
    # # print("".join(flat_brackets))


    # for row, line in enumerate(brackets):
    #     num_open = line.count("(")
    #     num_close = line.count(")")

    #     if num_open != num_close or num_open == 0 or num_close == 0:
    #         continue

    #     print("line:", "".join(line))
    #     print("row:", row, "num_open:", num_open, "num_close:", num_close)
    #     print("---")

    #     # is_
    #     # for col, char in enumerate(line):
    #     #     if char == "(":
    #     #         print("row:", row, "col:", col, "num_open:", num_open, "num_close:", num_close)
    #     #         break



    #     # print("row:", row, "num_open:", num_open, "num_close:", num_close)

    # print("=========================================")




    # for segment in segments:
    #     row_gaps = []
    #     col_gaps = []
    #     for i in range(len(segment) // 2):
    #         print("i:", i, "segment[i]:", segment[i], "segment[i * -1]:", segment[i * -1])
    #         from_start = segment[i]
    #         from_end = segment[i * -1]

    #         col_gaps.append(abs(from_start[1] - from_end[1]))
    #         row_gaps.append(abs(from_start[0] - from_end[0]))

    #     print("row_gaps:", row_gaps, "col_gaps:", col_gaps)


    # middle = len(pipe) // 2
    # pipe.append(pipe[0])
    # segments = [
    #     pipe[:middle+1],
    #     pipe[middle:],
    # ]

    # for segment in segments:
    #     print("segment:", segment)
    #     row_gaps = []
    #     col_gaps = []
    #     for i in range(len(segment) // 2):
    #         print("i:", i, "segment[i]:", segment[i], "segment[i * -1]:", segment[i * -1])
    #         from_start = segment[i]
    #         from_end = segment[i * -1]

    #         col_gaps.append(abs(from_start[1] - from_end[1]))
    #         row_gaps.append(abs(from_start[0] - from_end[0]))

    #     print("row_gaps:", row_gaps, "col_gaps:", col_gaps)




    # return abs((b-a)/2)


# test_inputs = get_inputs(filename=SAMPLE_INPUTS_1_FILENAME)
# test_answer = process(test_inputs)
# print("test answer:", test_answer)
# # assert test_answer == 4

# test_inputs = get_inputs(filename=SAMPLE_INPUTS_2_FILENAME)
# test_answer = process(test_inputs)
# print("test answer:", test_answer)
# assert test_answer == 4

test_inputs = get_inputs(filename=SAMPLE_INPUTS_3_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
# assert test_answer == 8

# test_inputs = get_inputs(filename=SAMPLE_INPUTS_4_FILENAME)
# test_answer = process(test_inputs)
# print("test answer:", test_answer)
# assert test_answer == 10

# inputs = get_inputs(filename=INPUT_FILENAME)
# answer = process(inputs)
# print("answer:", answer)
# assert answer == 7145
