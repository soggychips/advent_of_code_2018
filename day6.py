from string import ascii_letters
from collections import namedtuple
from helpers import *

Coord = namedtuple('Coordinate', ['x', 'y'])


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


@timed
def gather_data(text):
    coord_data = zip(ascii_letters, [(int(x[0]), int(x[1])) for x in (d.split(", ") for d in text)])
    coord_data = {letter: Coord(*coords) for letter, coords in coord_data}

    largest_dir = max(max(coord_data.values(), key=lambda coord: max(coord))) + 1
    grid = [[{'is_coord': False, 'closest_point': '-', 'closest_dist': None} for x in range(largest_dir)] for y in
            range(largest_dir)]

    for name, coord in coord_data.iteritems():
        grid[coord.y][coord.x].update({
            'is_coord': True,
            'closest_point': name,
            'closest_dist': 0
        })

    for x in range(largest_dir):
        for y in range(largest_dir):

            point = grid[y][x]
            if point['is_coord']:
                continue

            for letter, coord in coord_data.iteritems():
                man_dist = manhattan_distance(x, y, coord.x, coord.y)
                closest_dist = point['closest_dist']

                if closest_dist is None or man_dist < closest_dist:
                    point.update({
                        'closest_point': letter,
                        'closest_dist': man_dist
                    })
                elif man_dist == closest_dist:
                    point['closest_point'] = '.'

    return grid, coord_data, largest_dir


@timed
def part1(grid, coord_data, largest_dir):
    counts = {name: 0 for name in coord_data.keys()}
    for x in range(largest_dir):
        for y in range(largest_dir):
            closest = grid[y][x]['closest_point']
            if closest != ".":
                if x == 0 or y == 0 or x == largest_dir - 1 or y == largest_dir - 1:
                    counts[closest] = -1
                if counts[closest] >= 0:
                    counts[closest] += 1

    return max(counts.values())


@timed
def part2(coord_data, largest_dir, max_dist=10000):
    region_size = 0
    last_dist = 0
    sum_of_man_dist = 0

    for x in range(largest_dir):
        for y in range(largest_dir):
            if region_size > 0 and last_dist > sum_of_man_dist:  # break condition if we've left the safe region
                return region_size
            sum_of_man_dist = 0
            for coord in coord_data.values():
                sum_of_man_dist += manhattan_distance(x, y, coord.x, coord.y)
                if sum_of_man_dist >= max_dist:
                    break
            if sum_of_man_dist < max_dist:
                region_size += 1
            last_dist = sum_of_man_dist

    return region_size


if __name__ == '__main__':
    text = get_input(6)
    grid, coord_data, largest_dir = gather_data(text)
    print part1(grid, coord_data, largest_dir)
    print part2(coord_data, largest_dir)
