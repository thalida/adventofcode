from collections import Counter
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
    strengths = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    strengths.reverse()

    def sort_fn(line):
        hand = line.split()[0]
        card_counts = Counter(hand)

        counts_without_j = [count for card, count in card_counts.items() if card != "J"]

        largest_set = max(counts_without_j) if len(counts_without_j) > 0 else 0
        largest_set += card_counts.get("J", 0)

        num_single_cards = len([count for count in card_counts.values() if count == 1])

        # Give a bump to full house and two pair
        if largest_set < 4 and num_single_cards < 2:
            largest_set += 0.5

        # sort first by largest set, then by card strengths
        return [largest_set] + [strengths.index(card) for card in hand]

    sorted_cards = sorted(
        inputs,
        key=sort_fn,
    )

    score = 0
    for idx, line in enumerate(sorted_cards):
        bid = line.split()[1]
        score += int(bid) * (idx + 1)

    return score


test_inputs = get_inputs(filename=SAMPLE_INPUTS_FILENAME)
test_answer = process(test_inputs)
print("test answer:", test_answer)
assert test_answer == 5905

inputs = get_inputs(filename=INPUT_FILENAME)
answer = process(inputs)
print("answer:", answer)
assert answer == 250577259
