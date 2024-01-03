from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


damaged = "#"
operational = "."
unknown = "?"


def find_way(some_records, some_springs):
    on_damaged = False
    damageds = []
    for i in range(len(some_springs)):
        if some_springs[i] == damaged:
            if not on_damaged:
                start = i
                on_damaged = True
        else:
            if on_damaged:
                damageds.append(i - start)
            on_damaged = False
    return damageds == some_records


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * 0 + words[0] + "."
    words[1] = (words[1] + ",") * 0 + words[1]
    springs = words[0]
    records = [int(record) for record in words[1].split(',')]
    final_damageds = sum(records)
    damageds = len(re.findall(r"#", springs))
    unknowns = len(re.findall(r"\?", springs))
    unknown_damageds = final_damageds - damageds
    unknown_operationals = unknowns - unknown_damageds
    possibilities = combinations(range(unknowns), unknown_damageds)
    for possibility in possibilities:
        new_springs = ""
        unknowns_passed = 0
        for spring in springs:
            if spring == unknown and unknowns_passed in possibility:
                new_springs += damaged
                unknowns_passed += 1
            elif spring == unknown:
                new_springs += operational
                unknowns_passed += 1
            else:
                new_springs += spring
        ways += find_way(records, new_springs)

print(ways)
