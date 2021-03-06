# https://adventofcode.com/2019/day/1

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'


def get_inputs(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs


def parse_inputs(inputs):
  elements = {}

  for input in inputs:
    uses, creates = input.split(' => ')
    amount_created, type_created = creates.split(' ')
    requires = {}
    for use in uses.split(', '):
      amount, element = use.split(' ')
      requires[element] = int(amount)

    elements[type_created] = {
        'quantity': int(amount_created),
        'requires': requires
    }
  return elements


def get_required_materials(elements, element, quantity, available_materials={}, all_requirements={}, i=0):
  if element not in elements:
    return all_requirements, available_materials

  if element in available_materials:
    amount_created = available_materials[element]
  else:
    amount_created = 0

  creates_quantity = elements[element]['quantity']
  requires = elements[element]['requires']

  while amount_created < quantity:
    # print('  '*i, element, amount_created, quantity)
    for required_element, required_amount in requires.items():
      # print(required_element)
      if required_element in all_requirements:
        all_requirements[required_element] += required_amount
      else:
        all_requirements[required_element] = required_amount

      all_requirements, available_materials = get_required_materials(
          elements, required_element, required_amount, all_requirements=all_requirements, available_materials=available_materials, i=i+1)

    amount_created += creates_quantity
    # print('  '*i, element, amount_created, quantity)

  available_materials[element] = amount_created - quantity
  # print('  '*i, element, available_materials[element])
  # print()

  return all_requirements, available_materials

def forecast_amount(elements, element, with_element, with_amount, available_materials={}, all_requirements={}, i=0):
  available_materials[with_element] = with_amount

  created = 0
  while available_materials[with_element] >= with_amount:
    all_requirements, available_materials = get_required_materials(elements, 'FUEL', 1, available_materials=available_materials, all_requirements=all_requirements)
    created += 1
    print(created)

  print(created)


def process(elements):
  elements = parse_inputs(elements)
  forecast = forecast_amount(elements, 'FUEL', 'ORE', 1000000000000)
  pprint(forecast)
  return forecast


def main():
  elements = get_inputs(SCRIPT_DIR, INPUT_FILENAME)
  answer = process(elements)


main()
