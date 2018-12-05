# https://adventofcode.com/2018/day/4

import os
from pprint import pprint
import functools
import re
from collections import defaultdict

from datetime import datetime
import time

script_dir = os.path.dirname(__file__)
inputs = []
with open(os.path.join(script_dir,'input.txt'), 'r') as f:
  inputs = f.read().splitlines()

def run(raw_logs):
    entry_reg = r"\[(.*)\]\s(.*)"
    guard_id_reg = r".*\#(\d*).*"
    date_fmt = '%Y-%m-%d %H:%M'

    sorted_logs = sorted(raw_logs, key=lambda entry: entry.split('] ')[0])
    
    sleep_data = {}
    sleepiest_guard = None
    predictable_guard = None
    curr_guard_data = None
    for entry in sorted_logs:
        event_datetime, event = re.search(entry_reg, entry).groups()
        guard_match = re.match(guard_id_reg, event)
        next_guard_id = list(guard_match.groups())[0] if guard_match else None
        
        if next_guard_id:
            next_guard_id = int(next_guard_id)
            if sleep_data.get(next_guard_id) is None:
                sleep_data[next_guard_id] = {
                    'id': next_guard_id,
                    'sleep_start': None,
                    'sleepiest_minute': (0, 0),
                    'sleep_minutes': {},
                    'total_sleep': 0,
                }

            curr_guard_data = sleep_data.get(next_guard_id)
            continue;

        if event == 'falls asleep':
            curr_guard_data['sleep_start'] = event_datetime
            continue;
        
        start = curr_guard_data['sleep_start']
        start_min = int(start.split(':')[1])
        stop = event_datetime
        diff = datetime.strptime(stop, date_fmt) - datetime.strptime(start, date_fmt)
        minutes = int(diff.seconds / 60)
        
        for i in range(minutes):
            minute = start_min + i if start_min + i < 60 else 0
            amount_slept = curr_guard_data['sleep_minutes'].get(minute, 0) + 1
            curr_guard_data['sleep_minutes'][minute] = amount_slept
            if amount_slept > curr_guard_data['sleepiest_minute'][1]:
                curr_guard_data['sleepiest_minute'] = (minute, amount_slept)

        curr_guard_data['sleep_start'] = None
        curr_guard_data['total_sleep'] += minutes;

        if sleepiest_guard is None or curr_guard_data['total_sleep'] > sleepiest_guard['total_sleep']:
            sleepiest_guard = curr_guard_data

        if predictable_guard is None or curr_guard_data['sleepiest_minute'][1] > predictable_guard['sleepiest_minute'][1]:
            predictable_guard = curr_guard_data

    return predictable_guard['id'] * predictable_guard['sleepiest_minute'][0]

pprint(run(inputs))
