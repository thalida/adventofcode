# https://adventofcode.com/2019/day/12

import os
from pprint import pprint

from itertools import combinations

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def parse_position(input_str):
  input_arr = input_str[1:-1].split(', ')
  position = {val[0:1]: int(val[2:]) for val in input_arr}
  return position


def process(inputs):
  moons = []
  for i in range(0, 4):
    moons.append({
      'pos': parse_position(inputs[i]),
      'vel': {'x': 0, 'y': 0, 'z': 0},
      'pot': 0,
      'kin': 0,
    })

  moon_combos = list(combinations(list(range(0,4)), 2))
  steps = 1
  while True:
    if steps > 1000:
      sum = 0
      for moon in moons:
        sum += moon['total']
      return sum

    # apply gravity
    for combo in moon_combos:
      moon_a, moon_b = combo
      for axis in ['x', 'y', 'z']:
        if moons[moon_a]['pos'][axis] != moons[moon_b]['pos'][axis]:
          if moons[moon_a]['pos'][axis] > moons[moon_b]['pos'][axis]:
            larger_pos_moon = moon_a
            smaller_pos_moon = moon_b
          else:
            larger_pos_moon = moon_b
            smaller_pos_moon = moon_a

          moons[larger_pos_moon]['vel'][axis] -= 1
          moons[smaller_pos_moon]['vel'][axis] += 1

    # update position
    for moon in moons:
      moon['pot'] = 0
      moon['kin'] = 0

      for axis in ['x', 'y', 'z']:
        moon['pos'][axis] += moon['vel'][axis]
        moon['pot'] += abs(moon['pos'][axis])
        moon['kin'] += abs(moon['vel'][axis])

      moon['total'] = moon['pot'] * moon['kin']

    steps += 1

  # return outputs

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(inputs)
  print(f'answer:', answer)

main()
