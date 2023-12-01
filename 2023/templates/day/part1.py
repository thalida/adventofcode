import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = os.path.join(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return list(inputs)


def process(inputs):
    outputs = inputs.copy()
    return outputs


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print(f"test answer:", test_answer)
assert test_answer == []

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print(f"answer:", answer)
assert answer == []
