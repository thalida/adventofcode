# https://adventofcode.com/2019/day/8

import os
from pprint import pprint

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_FILENAME = 'inputs.txt'

def get_image_data(dir, filename):
  file = os.path.join(dir, filename)
  inputs = []

  with open(file, 'r') as f:
    inputs = f.read().splitlines()

  return inputs[0]


def analyze_image(image_data):
  image_size = {'width': 25, 'height': 6}
  image_area = image_size['width'] * image_size['height']
  total_pixels = len(image_data)
  num_layers = int(total_pixels / image_area)

  fewest_zeros_layer = None
  layer_counts = {}

  for layer in range(0, num_layers):
    layer_start_idx = layer * image_area
    layer_end_idx = layer_start_idx + image_area

    layer_pixels = image_data[layer_start_idx:layer_end_idx]

    layer_counts[layer] = {
      'zeros': layer_pixels.count('0'),
      'ones': layer_pixels.count('1'),
      'twos': layer_pixels.count('2'),
    }

    if (
      fewest_zeros_layer is None
      or layer_counts[layer]['zeros'] < layer_counts[fewest_zeros_layer]['zeros']
    ):
      fewest_zeros_layer = layer

  return layer_counts[fewest_zeros_layer]['ones'] * layer_counts[fewest_zeros_layer]['twos']


def main():
  image_data = get_image_data(SCRIPT_DIR, INPUT_FILENAME)
  answer = analyze_image(image_data)
  print(f'answer:', answer)

main()
