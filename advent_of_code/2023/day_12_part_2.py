from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"


def find_ways(pattern, springs, unknown_damageds, start_i=0, filled_records=0):
    ways = 0
    record = records[filled_records]
    for i, spring in enumerate(springs[start_i:]):
        if spring == UNKNOWN:
            test_springs = (
                        springs[:start_i + i] + DAMAGED * record + OPERATIONAL
                        + springs[start_i + i + record + 1:])
            if re.fullmatch(pattern, test_springs):
                if unknown_damageds == record:
                    ways += 1
                else:
                    filled_records += 1
                    ways += find_ways(pattern,
                                      test_springs,
                                      unknown_damageds - record,
                                      i + start_i + record + 1,
                                      filled_records)
        if spring == DAMAGED:
            new_re = ""
            for record in records[filled_records + 1:]:
                new_re += r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+"
            if not re.fullmatch(r"(?:#|\?){" + str(record) + r"}(?:\.|\?)+",
                                springs[start_i + 1:]):
                break
            test_springs = (
                    springs[:i + start_i] + DAMAGED * record + OPERATIONAL
                    + springs[i + start_i + record + 1:])
            filled_records += 1
            ways += find_ways(pattern,
                              test_springs,
                              unknown_damageds,
                              i + start_i + record + 1,
                              filled_records)
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
    ways += find_ways(re_pattern, springs, unknown_damageds)


print(ways)
