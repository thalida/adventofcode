import math
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

    for idx, line in enumerate(inputs):
        game_sets = line.split(":")[1].strip().split(";")
        counts = {}

        for game_set in game_sets:
            game_set = game_set.strip().split(",")

            for play in game_set:
                play = play.strip().split(" ")
                amount = int(play[0])
                color = play[1]

                if amount > counts.get(color, 0):
                    counts[color] = amount

        output += math.prod(counts.values())

    return output


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 2286

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 72422
