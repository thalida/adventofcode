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
        num_sets = line.split(":")[1].strip().split("|")

        winning_nums = set(num_sets[0].strip().split(" "))
        have_nums = set(num_sets[1].strip().split(" "))

        matching_nums = winning_nums.intersection(have_nums) - set([""])
        num_matches = len(matching_nums)

        if num_matches == 0:
            continue

        score = 1
        for _ in range(1, num_matches):
            score *= 2

        output += score

    return output


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 13

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 21959
