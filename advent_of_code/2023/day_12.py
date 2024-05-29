import re
import time
from functools import cache
start = time.time()

puzzle_input = open("inputs/day_12.txt").readlines()


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
PATTERN = re.compile(r"#+\.")


@cache
def find_ways(springs, records):
    ways = 0
    if UNKNOWN not in springs:
        records_filled = [len(damaged_springs) - 1
                          for damaged_springs in PATTERN.findall(springs)]
        if tuple(records_filled) == records:
            ways += 1
        return ways
    first_unknown = springs.index(UNKNOWN)
    records_filled = [len(damaged_springs) - 1
                      for damaged_springs
                      in PATTERN.findall(springs[:first_unknown])]
    if len(records_filled) > len(records):
        return 0
    for i, record in enumerate(records_filled):
        if record != records[i]:
            return 0
    records = records[len(records_filled):]
    start_string = ""
    last_damaged = re.search(r"#+\?", springs[:first_unknown + 1])
    if last_damaged:
        start_string = springs[last_damaged.start():first_unknown]
    ways += find_ways(
        start_string + OPERATIONAL + springs[first_unknown + 1:], records)
    ways += find_ways(
        start_string + DAMAGED + springs[first_unknown + 1:], records)

    return ways


answer = 0
for line in puzzle_input:
    words = line.split()
    words[0] = words[0] + "."
    line_springs = words[0]
    line_records = [int(record) for record in words[1].split(',')]

    line_ways = find_ways(line_springs, tuple(line_records))
    answer += line_ways


answer_2 = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * 4 + words[0] + "."
    words[1] = (words[1] + ",") * 4 + words[1]
    line_springs = words[0]
    line_records = [int(record) for record in words[1].split(',')]

    line_ways = find_ways(line_springs, tuple(line_records))
    answer_2 += line_ways

print(answer, answer_2)
print(time.time() - start)
