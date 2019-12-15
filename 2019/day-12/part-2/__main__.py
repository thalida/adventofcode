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

def minify_moons(moons):
  min_moons = []
  for moon in moons:
    min_moon = ''.join(map(str, moon['pos'].values())) + ''.join(map(str, moon['vel'].values()))
    min_moons.append(min_moon)
  return ''.join(min_moons)

def process(inputs):
  moon_combos = list(combinations(list(range(0, 4)), 2))
  moons = []
  for i in range(0, 4):
    moons.append({
        'pos': parse_position(inputs[i]),
        'vel': {'x': 0, 'y': 0, 'z': 0},
        'pot': 0,
        'kin': 0,
    })

  previous_states = []
  previous_states.append(minify_moons(moons))

  print('STEP', 0)
  for moon in moons:
    print(moon['pos'], moon['vel'])
  print()

  steps = 1
  while True:
    print('STEP', steps)

    # all_x = [moon['pos']['x'] for moon in moons]
    # sorted_x = sorted(list(set(all_x)))
    # x0_index = sorted_x.index(moons[0]['pos']['x'])
    # x1_index = sorted_x.index(moons[1]['pos']['x'])
    # x2_index = sorted_x.index(moons[2]['pos']['x'])
    # x3_index = sorted_x.index(moons[3]['pos']['x'])
    # print(sorted_x, x0_index, x1_index, x2_index, x3_index)

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
        # print(larger_pos_moon, smaller_pos_moon, moons[larger_pos_moon]['vel'], moons[smaller_pos_moon]['vel'])

    # update position
    for moon in moons:
      moon['pot'] = 0
      moon['kin'] = 0

      for axis in ['x', 'y', 'z']:
        moon['pos'][axis] += moon['vel'][axis]
        moon['pot'] += abs(moon['pos'][axis])
        moon['kin'] += abs(moon['vel'][axis])

      moon['total'] = moon['pot'] * moon['kin']

      print(moon['pos'], moon['vel'])

    print()

    if steps >= 3000:
      break

    minified_moons = minify_moons(moons)
    if minified_moons in previous_states:
      print('hsdfsd')
      return steps

    previous_states.append(minified_moons)

    steps += 1

  # return outputs


def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(inputs)
  print(f'answer:', answer)


main()
