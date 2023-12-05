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
    seeds = list(map(int, inputs[0].split(":")[1].strip().split(" ")))
    seed_map = {seed: seed for seed in seeds}

    map_label = None
    in_map = False
    mapped_seeds = defaultdict(list)
    for idx, line in enumerate(inputs[2:]):
        if len(line) == 0:
            in_map = False
            continue

        if line.find(":") != -1:
            map_label = line.split(":")[0]
            in_map = True
            continue

        if in_map:
            for orig_seed, mapped_seed in seed_map.items():
                if orig_seed in mapped_seeds[map_label]:
                    continue

                dest, src, num_range = list(map(int, line.split()))
                in_range = src <= mapped_seed <= src + num_range - 1

                if in_range:
                    seed_map[orig_seed] = dest + (mapped_seed - src)
                    mapped_seeds[map_label].append(orig_seed)

    return min(seed_map.values())


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 35

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 379811651
