#!/usr/bin/python3.12

import time as t

from math import sqrt, floor, ceil

start = t.time()

puzzle_input = open("inputs/day_6.txt").readlines()

times = [int(time) for time in puzzle_input[0].split() if time.isdigit()]
records = [
    int(record) for record in puzzle_input[1].split() if record.isdigit()]

multiple = 1
for i, time in enumerate(times):
    ways_to_beat = 0
    for j in range(time):
        if j * (time - j) > records[i]:
            ways_to_beat += 1
    multiple *= ways_to_beat


time = ""
record = ""
for word in puzzle_input[0].split():
    if word.isdigit():
        time += word
for word in puzzle_input[1].split():
    if word.isdigit():
        record += word
time = int(time)
record = int(record)

min_to_beat = ceil((time - sqrt(time**2 - 4 * record))/2)
max_to_beat = floor((time + sqrt(time**2 - 4 * record))/2)
ways_to_beat = max_to_beat - min_to_beat + 1

print(t.time() - start)
print(multiple, ways_to_beat)
