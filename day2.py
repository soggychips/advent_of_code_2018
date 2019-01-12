from helpers import get_input, timed


@timed
def part1(data):
    twos, threes = 0, 0
    for line in data:
        count_map = {}
        for letter in line:
            if letter not in count_map:
                count_map[letter] = 0
            count_map[letter] += 1
        twos += 1 if len(filter(lambda count: count == 2, count_map.values())) > 0 else 0
        threes += 1 if len(filter(lambda count: count == 3, count_map.values())) > 0 else 0
    return twos * threes


@timed
def part2(data):
    def intersection(a, b):
        diff, result = 0, ''
        for i, a_letter in enumerate(a):
            b_letter = b[i]
            if a_letter == b_letter:
                result += a_letter
            else:
                diff += 1
                if diff > 1:
                    return False
        return result

    for i, current_id in enumerate(data):
        for _id in data[i + 1:]:
            result = intersection(current_id, _id)
            if result:
                return result


if __name__ == '__main__':
    data = get_input(2)
    print part1(data)
    print part2(data)
