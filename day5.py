from helpers import *


def are_opposites(a, b):
    return abs(ord(a) - ord(b)) == 32


def destroy_opposites(polymer):
    new_polymer = polymer[0]
    for i in range(1, len(polymer)):
        if len(new_polymer) == 0:
            new_polymer += polymer[i]
            continue
        if are_opposites(new_polymer[-1], polymer[i]):
            new_polymer = new_polymer[:-1]
        else:
            new_polymer += polymer[i]
    return new_polymer


@timed
def part1(text):
    polymer = destroy_opposites(text)
    print len(polymer)


@timed
def part2(text):
    units = list(set([letter.lower() for letter in text]))
    data = {}
    for unit in units:
        polymer = text.replace(unit, '')
        polymer = polymer.replace(unit.upper(), '')
        polymer = destroy_opposites(polymer)
        data[unit] = len(polymer)

    print data[min(data.keys(), key=lambda unit: data[unit])]


if __name__ == '__main__':
    text = get_input(5)[0]
    part1(text)
    part2(text)
