import re
from helpers import *
from collections import deque
from string import uppercase

re_str = " (\w{1}) "

text = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""


@timed
def get_data(text):
    data = {}
    for step in list(set(re.findall(re_str, text))):
        data[step] = {'blocks': [], 'prereqs': [], 'processing_time': uppercase.index(step) + 1}

    text = text.split('\n')

    for line in text:
        steps = re.findall(re_str, line)
        data[steps[0]]['blocks'].append(steps[1])
        data[steps[1]]['prereqs'].append(steps[0])
    return data


@timed
def part1(data):
    steps = ''
    q = deque()
    for step in sorted(filter(lambda k: not data[k]['prereqs'], data), reverse=True):
        q.append(step)

    while q:
        step = q.pop()
        if step in steps:
            continue
        steps += step
        del (data[step])
        for d in data.values():
            try:
                d['prereqs'].remove(step)
            except:
                pass
        for step in sorted(filter(lambda k: not data[k]['prereqs'], data), reverse=True):
            q.append(step)

    print steps
    return steps


@timed
def part2(instructions, data, workers=5, time_offset=60):
    workers = {"w{}".format(worker_id): None for worker_id in range(workers)}
    time, tasks_done, q = 0, '', deque()
    for step in sorted(filter(lambda k: not data[k]['prereqs'], data), reverse=True):
        q.append(step)

    while True:  # time loop
        available_tasks = ''
        # do work
        time += 1
        break


if __name__ == '__main__':
    text = get_input(7)
    # text = """Step C must be finished before step A can begin.
    # Step C must be finished before step F can begin.
    # Step A must be finished before step B can begin.
    # Step A must be finished before step D can begin.
    # Step B must be finished before step E can begin.
    # Step D must be finished before step E can begin.
    # Step F must be finished before step E can begin."""
    data = get_data(text)
    instructions = part1(data)

    data = get_data(text)
    from pprint import pprint

    pprint(data)

    print part2(instructions, data, workers=2, time_offset=0)
