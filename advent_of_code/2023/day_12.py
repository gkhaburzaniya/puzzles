from functools import cache

puzzle_input = open("inputs/day_12.txt")

DAMAGED = "#"
OPERATIONAL = "."
UNKNOWN = "?"
OPERATIONAL_OR_UNKNOWN = OPERATIONAL + UNKNOWN


def solve(springs, records, multiplier=1):
    springs = springs * multiplier
    records = records * multiplier

    @cache
    def dynamic_solve(checked_springs, filled_records, ways=0):
        if checked_springs == len(springs):
            return filled_records == len(records)

        if springs[checked_springs] in OPERATIONAL_OR_UNKNOWN:
            ways += dynamic_solve(checked_springs + 1, filled_records)

        try:
            next_record = checked_springs + records[filled_records]
            if (OPERATIONAL not in springs[checked_springs:next_record]
                    and DAMAGED not in springs[next_record]):
                ways += dynamic_solve(next_record + 1, filled_records + 1)
        except IndexError:
            pass

        return ways

    return dynamic_solve(0, 0)


answer = answer_2 = 0
for line in puzzle_input:
    line_springs, line_records = line.split()
    line_springs = (line_springs + UNKNOWN)
    line_records = [int(record) for record in line_records.split(",")]
    answer += solve(line_springs, line_records)
    answer_2 += solve(line_springs, line_records, 5)

print(answer, answer_2)
