import re
import time
start = time.time()
new_start = start

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
MULTIPLIER = 4
cached_patterns = {}


def find_ways(curr_springs, filled_records=0):
    curr_ways = 0
    if filled_records == len(records):
        return curr_ways
    curr_record = records[filled_records]
    pattern = patterns[filled_records]
    curr_sum = sums[filled_records]
    records_left = tuple(records[filled_records:])
    for i, spring in enumerate(curr_springs):
        if not pattern.fullmatch(curr_springs[i:]):
            break
        if DAMAGED in curr_springs[:i]:
            break
        if curr_springs[i + curr_record] == DAMAGED:
            continue
        if spring == UNKNOWN or spring == DAMAGED:
            test_springs = (
                    curr_springs[:i] + DAMAGED * curr_record +
                    OPERATIONAL + curr_springs[i + curr_record + 1:]
            )
            if (test_springs, records_left) in cached_patterns:
                curr_ways += cached_patterns[(test_springs, records_left)]
            elif pattern.fullmatch(test_springs):
                if len(re.findall(DAMAGED, test_springs)) == curr_sum:
                    new_ways = 1
                else:
                    new_ways = find_ways(test_springs[i+curr_record+1:],
                                         filled_records + 1)
                cached_patterns[(test_springs, records_left)] = new_ways
                curr_ways += new_ways
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
        patterns.append(re.compile(re_pattern))
        sums.append(sum(records[i:]))

    line_ways = find_ways(springs)
    print(line, line_ways)
    ways += line_ways

print(ways)
print(time.time() - start)
