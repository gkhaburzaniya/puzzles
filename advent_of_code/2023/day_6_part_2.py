from math import sqrt, floor, ceil

puzzle_input = open("inputs/day_6.txt").readlines()

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
print(ways_to_beat)
