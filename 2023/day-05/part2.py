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
    seed_pairs = [
        (seed_pair[0], seed_pair[0] + seed_pair[1] - 1)
        for seed_pair in list(zip(*[iter(seeds)] * 2))
    ]
    seed_map = {seed_pair: seed_pair for seed_pair in seed_pairs}

    in_map = False
    for idx, line in enumerate(inputs[2:]):
        if len(line) == 0:
            in_map = False
            continue

        if line.find(":") != -1:
            mapped_seeds = []
            in_map = True
            continue

        if in_map:
            for orig_seed_range, seed_range in seed_map.copy().items():
                if orig_seed_range in mapped_seeds:
                    continue

                dest, src, num_range = list(map(int, line.split()))

                src_min = src
                src_max = src + num_range - 1
                seed_min = seed_range[0]
                seed_max = seed_range[1]

                if src_min > seed_max or src_max < seed_min:
                    continue

                overlapping_min = max(src_min, seed_min)
                overlapping_max = min(src_max, seed_max)

                dest_min = dest + (overlapping_min - src_min)
                dest_max = dest_min + (overlapping_max - overlapping_min)

                if overlapping_min == seed_min and overlapping_max == seed_max:
                    seed_map[orig_seed_range] = (dest_min, dest_max)
                    mapped_seeds.append(orig_seed_range)
                    continue

                seed_map[(overlapping_min, overlapping_max)] = (dest_min, dest_max)
                mapped_seeds.append((overlapping_min, overlapping_max))
                del seed_map[orig_seed_range]

                if overlapping_min > seed_min:
                    seed_map[(seed_min, overlapping_min - 1)] = (
                        seed_min,
                        overlapping_min - 1,
                    )

                if overlapping_max < seed_max:
                    seed_map[(overlapping_max + 1, seed_max)] = (
                        overlapping_max + 1,
                        seed_max,
                    )

    return min(seed_map.values())[0]


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 46

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 27992443
