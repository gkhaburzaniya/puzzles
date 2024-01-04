from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"


def find_ways(pattern, springs, start_i=0, filled_records=0):
    ways = 0
    curr_record = records[filled_records]
    for i, spring in enumerate(springs[start_i:]):
        if spring == UNKNOWN:
            if springs[start_i + i + curr_record] == DAMAGED:
                continue
            test_springs = (
                    springs[:start_i + i] + DAMAGED * curr_record +
                    OPERATIONAL + springs[start_i + i + curr_record + 1:]
            )
            if re.fullmatch(pattern, test_springs):
                if len(re.findall(DAMAGED, test_springs)) == sum(records):
                    ways += 1
                else:
                    ways += find_ways(pattern,
                                      test_springs,
                                      i + start_i + curr_record + 1,
                                      filled_records + 1)
            if (UNKNOWN not in test_springs[start_i + i:] and
                    springs[start_i + i + curr_record] != UNKNOWN):
                break
        elif spring == DAMAGED:
            new_re = ""
            for record in records[filled_records:]:
                new_re += r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+"
            if not re.fullmatch(new_re, springs[start_i + i:]):
                break
            test_springs = (
                    springs[:i + start_i] + DAMAGED * curr_record + OPERATIONAL
                    + springs[i + start_i + curr_record + 1:])
            if len(re.findall(DAMAGED, test_springs)) == sum(records):
                ways += 1
            if (UNKNOWN not in test_springs[start_i + i:] and
                    springs[start_i + i + curr_record] != UNKNOWN):
                break
            ways += find_ways(pattern,
                              test_springs,
                              i + start_i + curr_record + 1,
                              filled_records + 1)
    return ways


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * 0 + words[0] + "."
    words[1] = (words[1] + ",") * 0 + words[1]
    springs = words[0]
    records = [int(record) for record in words[1].split(',')]
    damageds = sum(records)
    known_damageds = len(re.findall("#", springs))
    unknown_damageds = damageds - known_damageds
    re_pattern = r"(?:\.|\?)*"
    for record in records:
        re_pattern += r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+"
    ways += find_ways(re_pattern, springs)


print(ways)
