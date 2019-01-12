from helpers import get_input, timed


@timed
def part1(data):
    return sum(data)


@timed
def part2(data):
    frequency, seen = 0, set()
    while True:
        for change in data:
            frequency += change
            if frequency in seen:
                return frequency
            seen.add(frequency)


if __name__ == '__main__':
    data = [int(n) for n in get_input(1)]
    print part1(data)
    print part2(data)
