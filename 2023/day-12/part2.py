import itertools
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



def product(*args, repeat=1, target_sum=None):
    pools = [tuple(pool) for pool in args] * repeat
    products = [[]]

    new_pools = []
    num_middle = repeat - 2
    for i, pool in enumerate(pools):
        is_first = i == 0
        is_last = i == repeat - 1

        if not is_first and not is_last:
            pool = pool[1:]
            if num_middle > 1:
                pool = pool[:-1]

        if is_first or is_last:
            pool = pool[:-num_middle]

        new_pools.append(pool)
    pools = new_pools

    print("pools:", pools)

    for pool in pools:
        extended_products = []
        for n in pool:
            for p in products:
                new_set = p + [n]

                if sum(new_set) > target_sum:
                    continue

                if len(new_set) < repeat:
                    extended_products.append(new_set)

                if len(new_set) == repeat:
                    yield tuple(new_set)

        products = extended_products



def process(inputs):
    num_arragements = 0

    for idx, line in enumerate(inputs):
        line_num = idx + 1
        print("[b][yellow]processing line:[/yellow][/b]", line_num)
        print(line)

        input_conditions, damage_counts_str = line.split()

        input_conditions = "?".join([input_conditions] * 5)
        damage_counts_str = ",".join([damage_counts_str] * 5)

        print(input_conditions, damage_counts_str)

        damage_counts = [int(count) for count in damage_counts_str.split(",")]
        damage_sets = ["#" * count for count in damage_counts]

        num_dots = len(input_conditions) - sum(damage_counts)
        num_gaps = len(damage_sets) + 1
        print("getting product...")
        dot_combos = product(range(0, num_dots + 1), repeat=num_gaps, target_sum=num_dots)

        potential_condition_sets = []
        for combo in dot_combos:
            dot_set = ["." * num for num in combo]
            test_condition = "".join([x for x in itertools.chain(*itertools.zip_longest(dot_set, damage_sets)) if x is not None])

            if len(test_condition) != len(input_conditions):
                continue

            condition_damage_sets = [x for x in test_condition.split(".") if x != ""]
            if len(condition_damage_sets) != len(damage_sets):
                continue

            potential_condition_sets.append(test_condition)

        valid_sets = []
        for condition_set in potential_condition_sets:
            is_valid = True
            for i in range(len(condition_set)):
                input_char = input_conditions[i]
                condition_char = condition_set[i]

                if input_char == "?":
                    continue

                if input_char != condition_char:
                    is_valid = False
                    break

            if is_valid:
                valid_sets.append(condition_set)
                num_arragements += 1

    return num_arragements


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 525152

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 7350
