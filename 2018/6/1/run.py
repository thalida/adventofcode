# https://adventofcode.com/2018/day/6

from pprint import pprint
from collections import defaultdict
import os

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def distance(pos1, pos2): 
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def run(orig_coords):
    grid = None
    coords = list(map(lambda c: list(map(lambda i: int(i), c.split(', '))), inputs))
    min_x = min(coords, key=lambda c: c[0])[0]
    min_y = min(coords, key=lambda c: c[1])[1]
    max_x = max(coords, key=lambda c: c[0])[0]
    max_y = max(coords, key=lambda c: c[1])[1]
    counts = defaultdict(lambda: 0)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = list(map(lambda c: distance(c, [x, y]), coords))
            min_distance = min(distances)
            has_multi_min = distances.count(min_distance) > 1

            if not has_multi_min:
                coord_index = distances.index(min_distance)
                coord = coords[coord_index]
                counts[tuple(coord)] += 1
    
    return max(dict(counts).values())

print(run(inputs))
