from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
MULTIPLIER = 4


def find_ways(springs, start_i=0, filled_records=0):
    curr_ways = 0
    if filled_records == len(records):
        return ways
    curr_record = records[filled_records]
    pattern = record_patterns[0]

    for i, spring in enumerate(springs[start_i:]):
        if not re.fullmatch(record_patterns[filled_records], springs[start_i + i:]):
            break
        if springs[start_i + i + curr_record] == DAMAGED:
            continue
        if spring == UNKNOWN:
            test_springs = (
                    springs[:start_i + i] + DAMAGED * curr_record +
                    OPERATIONAL + springs[start_i + i + curr_record + 1:]
            )
            if re.fullmatch(pattern, test_springs):
                if len(re.findall(DAMAGED, test_springs)) == sum(records):
                    curr_ways += 1
                else:
                    curr_ways += find_ways(test_springs,
                                           i + start_i + curr_record + 1,
                                           filled_records + 1)
            if (UNKNOWN not in test_springs[start_i + i:] and
                    springs[start_i + i + curr_record] != UNKNOWN):
                break
        elif spring == DAMAGED:
            test_springs = (
                    springs[:i + start_i] + DAMAGED * curr_record + OPERATIONAL
                    + springs[i + start_i + curr_record + 1:])
            if len(re.findall(DAMAGED, test_springs)) == sum(records):
                curr_ways += 1
            if (UNKNOWN not in test_springs[start_i + i:] and
                    springs[start_i + i + curr_record] != UNKNOWN):
                break
            curr_ways += find_ways(test_springs,
                                   i + start_i + curr_record + 1,
                                   filled_records + 1)
    return curr_ways


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * MULTIPLIER + words[0] + "."
    words[1] = (words[1] + ",") * MULTIPLIER + words[1]
    springs = words[0]
    records = [int(record) for record in words[1].split(',')]
    record_patterns = []
    for i in range(len(records)):
        re_pattern = r"(?:\.|\?)*"
        for record in records[i:]:
            re_pattern += r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+"
        record_patterns.append(re_pattern)
    ways += find_ways(springs)
    print(line, ways)
