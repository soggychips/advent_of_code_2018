import re
from dateutil.parser import parse
from helpers import *


def get_data(text):
    re_str = "\[(?P<timestamp>[^\]]+)\] \w+ (?P<action>up|asleep|#\d+)"
    data = sorted([{'datetime': parse(obj['timestamp']), 'action': obj['action']} for obj in
                   [re.match(re_str, line).groupdict() for line in text]], key=lambda x: x['datetime'])
    return data


def part1(data):
    guard_data, guard_id, sleep_start = {}, None, None
    for piece in data:
        if piece['action'].startswith('#'):
            guard_id = int(piece['action'][1:])
            if guard_id not in guard_data:
                guard_data[guard_id] = {'sleeptime': 0, 'minutes': {}}
        elif piece['action'] == 'asleep':
            sleep_start = piece['datetime'].minute
        else:  # wake up condition
            sleep_end = piece['datetime'].minute
            guard_data[guard_id]['sleeptime'] += (sleep_end - sleep_start)
            for minute in range(sleep_start, sleep_end + 1):
                if minute not in guard_data[guard_id]['minutes']:
                    guard_data[guard_id]['minutes'][minute] = 0
                guard_data[guard_id]['minutes'][minute] += 1

    sleepiest_guard_id = max(guard_data.keys(), key=lambda _id: guard_data[_id]['sleeptime'])

    minutes = guard_data[sleepiest_guard_id]['minutes']
    median = max(minutes.keys(), key=lambda minute: minutes[minute])

    print median * sleepiest_guard_id
    return guard_data


def part2(guard_data):
    consistent_guard_id, cons_guard_median, highest_count = None, 0, 0
    for guard_id, stats in guard_data.iteritems():
        if stats['sleeptime'] == 0:
            continue
        minutes = stats['minutes']
        median = max(minutes.keys(), key=lambda minute: minutes[minute])
        median_count = minutes[median]
        if median_count > highest_count:
            consistent_guard_id = guard_id
            cons_guard_median = median
            highest_count = median_count

    print consistent_guard_id * cons_guard_median


if __name__ == '__main__':
    text = get_input(4)
    data = get_data(text)
    guard_data = part1(data)
    part2(guard_data)
