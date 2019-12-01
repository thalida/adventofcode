# https://adventofcode.com/2019/day/1

import os
import math

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'module_masses.txt'


def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def calc_fuel(mass):
    return math.floor(int(mass) / 3) - 2


def calc_flight_fuel(masses):
  # let's keep the original set of masses clean
  masses_copy = masses.copy()
  total_fuel = 0

  for mass in masses_copy:
      fuel = calc_fuel(mass)

      # If we require additional fuel for this mass...
      #   1) add it to the total fuel required
      #   2) add the fuel required to calculate the additional fuel needed to
      #     support this new mass
      if fuel > 0:
          total_fuel += fuel
          masses_copy.append(fuel)

  return total_fuel


def main():
  module_masses = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = calc_flight_fuel(module_masses)
  print(f'answer:', answer)

main()
