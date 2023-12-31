from dataclasses import dataclass

puzzle_input = open("inputs/day_12_input.txt")


damaged = "#"
operational = "."
unknown = "?"


@dataclass
class Record:
    length: int
    start: int = 0
    end: int = 0


def find_way(some_records, some_springs, springs_start=0):
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
                    (spring == unknown or spring == damaged) and
                    operational not in springs_left[i:i + record.length] and
                    (
                        len(springs_left) == i + record.length or
                        springs_left[i + record.length] != damaged
                    )
            ):
                record.start = springs_start + start_i + i
                record.end = springs_start + start_i + i + record.length - 1
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
    ways += find_way(records, springs)
    for i in range(len(records)):
        new_springs_start = records[-(i + 1)].start + 1
        new_springs = springs[new_springs_start:]
        for j in range(len(new_springs)):
            ways += find_way(records[-(i + 1):],
                             new_springs[j:],
                             new_springs_start)

print(ways)
