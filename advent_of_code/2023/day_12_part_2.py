from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


damaged = "#"
operational = "."
unknown = "?"


def find_ways(pattern, springs, unknown_damageds, start_i=0):
    ways = 0
    for i, spring in enumerate(springs[start_i:]):
        if spring == unknown:
            test_springs = (springs[:i + start_i] + damaged
                            + springs[i + start_i + 1:])
            if re.fullmatch(pattern, test_springs):
                if unknown_damageds == 1:
                    ways += 1
                else:
                    ways += find_ways(pattern, test_springs,
                                      unknown_damageds - 1, i + start_i + 1)
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
