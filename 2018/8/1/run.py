# https://adventofcode.com/2018/day/8

import os
from collections import defaultdict
from pprint import pprint

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

# inputs = ["2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"]
# 2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
#                 2 (3) [1, 1, 2]              
# 0 (3) [10, 11, 12]          1 (1) [2]
#                                 0 (1) [99]

def build_tree(items, all_meta=[], tree=None):
    while items:
        children = items.pop(0)
        num_meta = items.pop(0)

        node = {
            'num_meta': num_meta,
            'children': [],
            'meta': None,
        }
        
        if tree is None:
            tree = node

        for i in range(children):
            child_node, all_meta = build_tree(items, all_meta=all_meta, tree=node)
            node['children'].append(child_node)

        if num_meta > 0:
            node['meta'] = items[0:num_meta]
            all_meta += node['meta']
            del items[0:num_meta]
            return (node, all_meta)

items = list(map(lambda x: int(x), inputs[0].split(' ')))
tree, all_meta = build_tree(items)
pprint(sum(all_meta))
