import re
from helpers import *


@timed
def get_data(text):
    re_str = '#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,2})x(\d{1,2})'
    data = {}
    for line in text:
        groups = re.match(re_str, line).groups()
        _id, x, y, dx, dy = (int(g) for g in groups)
        data[_id] = {
            'x': x,
            'y': y,
            'dx': dx,
            'dy': dy
        }
    return data


@timed
def part1(data):
    gt_one = 0
    fabric = [[0 for y in range(1000)] for x in range(1000)]
    for d in data.itervalues():
        for x in range(d['x'], d['x'] + d['dx']):
            for y in range(d['y'], d['y'] + d['dy']):
                if fabric[y][x] == 1:
                    gt_one += 1
                fabric[y][x] += 1

    print gt_one


@timed
def part2(data):
    fabric = [[0 for y in range(1000)] for x in range(1000)]
    id_counts = {_id: 1 for _id in data}

    for _id, d in data.iteritems():
        for x in range(d['x'], d['x'] + d['dx']):
            for y in range(d['y'], d['y'] + d['dy']):
                if fabric[y][x] != 0:
                    id_counts[fabric[y][x]] = 0
                    id_counts[_id] = 0
                fabric[y][x] = _id

    result = filter(lambda _id: id_counts[_id] == 1, id_counts)[0]
    print result


if __name__ == '__main__':
    text = get_input(3)
    data = get_data(text)
    part1(data)
    part2(data)
