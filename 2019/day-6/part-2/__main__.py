# https://adventofcode.com/2019/day/6

import os

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


def get_path(orbit_map, chain):
  node = chain[-1]
  parent_node = [key for (key, value) in orbit_map.items() if node in value]

  if len(parent_node) == 0:
    return chain

  chain.append(parent_node[0])
  return get_path(orbit_map, chain)


def main():
  inputs = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  orbit_map = get_orbit_map(inputs)
  you_node = [key for (key, value) in orbit_map.items() if 'YOU' in value][0]
  san_node = [key for (key, value) in orbit_map.items() if 'SAN' in value][0]
  you_path = get_path(orbit_map, [you_node])
  san_path = get_path(orbit_map, [san_node])
  short_path = len(set(you_path) ^ set(san_path))

  print(f'answer:', short_path)

main()
