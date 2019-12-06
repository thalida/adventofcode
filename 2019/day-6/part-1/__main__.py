# https://adventofcode.com/2019/day/6

import os
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def get_orbit_map(orbits):
  orbits = orbits.copy()
  orbit_map = {}

  total_orbits = len(orbits)
  i = 0
  while i < total_orbits:
    center, orbiting = orbits[i].split(')')

    if center not in orbit_map:
      orbit_map[center] = []

    orbit_map[center].append(orbiting)
    i += 1

  return orbit_map


def calc_total_orbits(orbit_map, chain=["COM"]):
  node = chain[-1]
  sum = len(chain) - 1

  if node not in orbit_map:
    return sum

  for next_node in orbit_map[node]:
    new_chain = chain.copy()
    new_chain.append(next_node)
    nested_orbit_sum = calc_total_orbits(orbit_map, chain=new_chain)
    sum += nested_orbit_sum

  return sum

def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  orbit_map = get_orbit_map(inputs)
  answer = calc_total_orbits(orbit_map)
  print(f'answer:', answer)

main()
