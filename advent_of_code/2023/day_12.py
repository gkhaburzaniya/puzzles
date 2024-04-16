from itertools import product
import re

from dataclasses import dataclass

puzzle_input = open("inputs/day_12.txt")


damaged = "#"
operational = "."
unknown = "?"


@dataclass
class Record:
    length: int
    start: int = 0
    end: int = 0


def find_way(some_records, some_springs):
    prev_record = None
    for record in some_records:
        if not prev_record:
            start_i = 0
        else:
            start_i = prev_record.end + 2
        springs_left = some_springs[start_i:]
        for i, spring in enumerate(springs_left):
            if len(springs_left) < i + record.length:
                return False
            if (
                    spring == damaged and
                    operational not in springs_left[i:i + record.length] and
                    (
                        len(springs_left) == i + record.length or
                        springs_left[i + record.length] != damaged
                    )
            ):
                record.start = start_i + i
                record.end = start_i + i + record.length - 1
                prev_record = record
                break
            elif spring == damaged:
                return False
    print(records)
    if damaged not in springs[records[-1].end + 1:]:
        return True
    else:
        return False


ways = 0
for line in puzzle_input:
    words = line.split()
    springs = words[0]
    records = [Record(int(record)) for record in words[1].split(',')]
    final_damageds = sum([record.length for record in records])
    damageds = len(re.findall(r"#", springs))
    unknowns = len(re.findall(r"\?", springs))
    unknown_damageds = final_damageds - damageds
    unknown_operationals = unknowns - unknown_damageds
    possibilities = product("#.", repeat=unknowns)
    for possibility in possibilities:
        possibility = list(possibility)
        if len([item for item in possibility if item == damaged]) != unknown_damageds:
            continue
        new_springs = ""
        for spring in springs:
            if spring == unknown:
                new_springs += possibility.pop(0)
            else:
                new_springs += spring
        ways += find_way(records, new_springs)

print(ways)
