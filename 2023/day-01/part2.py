import re
from pathlib import Path

from rich import pretty, print

pretty.install()


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILENAME = "inputs.txt"
SAMPLE_INPUTS_FILENAME = "inputs_sample_2.txt"


def get_inputs(filename=INPUT_FILENAME):
    filepath = Path(SCRIPT_DIR, filename)
    with open(filepath, "r") as f:
        inputs = f.read().splitlines()

    return inputs


def process(inputs):
    output = 0

    wordmap = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for line in inputs:
        indexes = {min: None, max: None}

        for word in wordmap.keys():
            word_indexes = [m.start() for m in re.finditer(word, line)]

            for idx in word_indexes:
                indexes[idx] = wordmap[word]

        for idx, letter in enumerate(line):
            is_number = letter.isnumeric()
            if is_number:
                indexes[idx] = letter

        min_idx = min(indexes.keys())
        max_idx = max(indexes.keys())
        num = int(f"{indexes[min_idx]}{indexes[max_idx]}")

        output += num

    return output


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 281

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 54203
