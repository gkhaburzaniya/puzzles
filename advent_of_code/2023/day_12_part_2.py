import re
import time

start = time.time()
new_start = start

puzzle_input = open("inputs/day_12_input.txt")


DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
MULTIPLIER = 0
cached_patterns = {}


def find_ways(curr_spans, filled_records=0):
    curr_ways = 0
    curr_record = records[filled_records]
    if filled_records == len(records) - 1:
        for span in curr_spans:
            damaged_spans = list(re.finditer("#+", span))
            if damaged_spans:
                damaged_spans_start = damaged_spans[0].start()
                damaged_spans_end = damaged_spans[-1].end()
                damage_len = damaged_spans_end - damaged_spans_start
                excess_len = curr_record - damage_len
                curr_ways = 1 + min(len(span) - damage_len, 2 * excess_len)
                break
            if len(span) >= curr_record:
                curr_ways += len(span) - curr_record + 1
    else:
        for i, span in enumerate(curr_spans):
            damaged_spans = list(re.finditer("#+", span))
            if damaged_spans:
                # Record fits before damage starts
                for j in range(damaged_spans[0].start() - (curr_record + 1)):
                    new_span = span[j+curr_record+1:]
                    new_spans = [new_span]
                    if len(curr_spans) > i + 1:
                        new_spans += curr_spans[i+1:]
                    if others_fit(new_spans, filled_records + 1):
                        curr_ways += find_ways(new_spans, filled_records + 1)
                # Damage starts
                for dam_span in damaged_spans:
                    if len(span) - dam_span.start() < curr_record:
                        return curr_ways
                    new_spans = []
                    if dam_span.end() + 1 < len(span):
                        new_span = span[dam_span.end() + 1]
                        new_spans += [new_span]
                    if len(curr_spans) > i + 1:
                        new_spans += curr_spans[i + 1:]
                    if others_fit(new_spans, filled_records + 1):
                        curr_ways += find_ways(new_spans,
                                               filled_records + 1)
                return curr_ways
            for j in range(len(span) - curr_record + 1):
                new_spans = []
                if len(span) > j + curr_record + 1:
                    new_span = span[j+curr_record+1]
                    new_spans += [new_span]
                if len(curr_spans) > i + 1:
                    new_spans += curr_spans[i + 1:]
                if others_fit(new_spans, filled_records + 1):
                    curr_ways += find_ways(new_spans, filled_records + 1)
                else:
                    break

    return curr_ways


def others_fit(curr_spans, filled_records):
    curr_springs = ".".join(curr_spans) + "."
    pattern = patterns[filled_records]
    if re.fullmatch(pattern, curr_springs):
        return True
    else:
        return False


ways = 0
for line in puzzle_input:
    words = line.split()
    words[0] = (words[0] + "?") * MULTIPLIER + words[0]
    words[1] = (words[1] + ",") * MULTIPLIER + words[1]
    springs = words[0]
    records = [int(record) for record in words[1].split(',')]
    patterns = []
    for i in range(len(records)):
        re_pattern = r"[?.]*"
        for record in records[i:]:
            re_pattern += r"[?#]{" + str(record) + r"}[?.]+"
        patterns.append(re.compile(re_pattern))
    spans = re.findall(r"[?#]+", springs)
    line_ways = find_ways(spans)
    print(spans, line_ways)
    ways += line_ways

print(ways)
print(time.time() - start)
