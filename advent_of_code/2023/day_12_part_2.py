import re
import time
from functools import cache
start = time.time()

puzzle_input = open("inputs/day_12.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
MULTIPLIER = 4
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


total_ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * MULTIPLIER + words[0] + "."
    words[1] = (words[1] + ",") * MULTIPLIER + words[1]
    line_springs = words[0]
    line_records = [int(record) for record in words[1].split(',')]

    line_ways = find_ways(line_springs, tuple(line_records))
    total_ways += line_ways

print(total_ways)
print(time.time() - start)
