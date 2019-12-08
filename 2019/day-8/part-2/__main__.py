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

def decode_image(image_data):
  image_size = {'width': 25, 'height': 6}
  image_area = image_size['width'] * image_size['height']
  total_pixels = len(image_data)
  num_layers = int(total_pixels / image_area)

  BLACK = 0
  WHITE = 1
  TRANSPARENT = 2

  decoded_image = []
  decoded_multi_array = []

  for pixel_idx in range(0, image_area):
    for layer_idx in range(0, num_layers):
      layer_start_idx = layer_idx * image_area
      layer_pixel_idx = layer_start_idx + pixel_idx
      pixel = int(image_data[layer_pixel_idx])

      if pixel == BLACK or pixel == WHITE:
        decoded_image.append(str(pixel))

        if pixel_idx % image_size['width'] == 0:
          decoded_multi_array.append([])

        insert_val = '🁢' if pixel == WHITE else ' '
        decoded_multi_array[-1].append(insert_val)
        break

  for row in decoded_multi_array:
    print(''.join(row))

def main():
  image_data = get_image_data(SCRIPT_DIR, INPUT_FILENAME)
  decode_image(image_data)

main()
