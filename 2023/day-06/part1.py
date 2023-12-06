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
    output = 1

    race_times = list(map(int, inputs[0].split(":")[1].strip().split()))
    race_dists = list(map(int, inputs[1].split(":")[1].strip().split()))

    for time, dist in list(zip(race_times, race_dists)):
        num_times_won = 0
        for speed in range(0, time + 1):
            distance_traveled = speed * (time - speed)

            if distance_traveled > dist:
                num_times_won += 1

        output *= num_times_won

    return output


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 288

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 1159152
