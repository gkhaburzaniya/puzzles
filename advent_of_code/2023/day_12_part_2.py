from itertools import combinations
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


damaged = "#"
operational = "."
unknown = "?"


def find_way(some_records, some_springs):
    records_found = 0
    springs_i = 0
    last_record = False
    for record in some_records:
        record_found = False
        while not record_found:
            spring = some_springs[springs_i]
            if (
                    spring == damaged and not last_record and
                    some_springs[springs_i:springs_i + record + 1] == damaged * record + operational
            ):
                record_found = True
                records_found += 1
                if records_found == len(some_records) - 1:
                    last_record = True
                springs_i = springs_i + record + 1
                continue
            elif (
                    spring == damaged and last_record and
                    some_springs[springs_i:springs_i + record] == damaged * record
            ):
                return True
            elif spring == damaged:
                return False
            springs_i += 1


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * 0 + words[0]
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
