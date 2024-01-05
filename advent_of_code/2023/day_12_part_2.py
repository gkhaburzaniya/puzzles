from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
MULTIPLIER = 4


def find_ways(curr_springs, filled_records=0):
    curr_ways = 0
    if filled_records == len(records):
        return curr_ways
    curr_record = records[filled_records]
    pattern = patterns[filled_records]
    curr_sum = sums[filled_records]
    for i, spring in enumerate(curr_springs):
        if not re.fullmatch(pattern, curr_springs[i:]):
            break
        if DAMAGED in curr_springs[:i]:
            break
        if curr_springs[i + curr_record] == DAMAGED:
            continue
        if spring == UNKNOWN:
            test_springs = (
                    curr_springs[:i] + DAMAGED * curr_record +
                    OPERATIONAL + curr_springs[i + curr_record + 1:]
            )
            if re.fullmatch(pattern, test_springs):
                if len(re.findall(DAMAGED, test_springs)) == curr_sum:
                    curr_ways += 1
                else:
                    curr_ways += find_ways(test_springs[i+curr_record+1:],
                                           filled_records + 1)
        elif spring == DAMAGED:
            test_springs = (
                    curr_springs[:i] + DAMAGED * curr_record + OPERATIONAL
                    + curr_springs[i + curr_record + 1:])
            if len(re.findall(DAMAGED, test_springs)) == curr_sum:
                curr_ways += 1
            curr_ways += find_ways(test_springs[i+curr_record+1:],
                                   filled_records + 1)
    return curr_ways


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * MULTIPLIER + words[0] + "."
    words[1] = (words[1] + ",") * MULTIPLIER + words[1]
    springs = words[0]
    records = [int(record) for record in words[1].split(',')]
    patterns = []
    sums = []
    for i in range(len(records)):
        re_pattern = r"(?:\.|\?)*"
        for record in records[i:]:
            re_pattern += r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+"
        patterns.append(re_pattern)
        sums.append(sum(records[i:]))

    ways += find_ways(springs)
    print(line, ways)
