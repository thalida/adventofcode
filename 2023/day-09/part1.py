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
    history_sequences = defaultdict(list)

    for idx, line in enumerate(inputs):
        nums = list(map(int, line.split()))
        history_sequences[idx].append(nums.copy())

        while set(nums) != set([0]):
            nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            history_sequences[idx].append(nums)

    for history_sequence in history_sequences.values():
        history_sequence.reverse()
        for i, _ in enumerate(history_sequence):
            if i == 0:
                history_sequence[i].append(0)
                continue

            last = history_sequence[i][-1]
            below = history_sequence[i - 1][-1]
            history_sequence[i].append(last + below)

    return sum([diffs[-1][-1] for diffs in history_sequences.values()])


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 114

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 1789635132
