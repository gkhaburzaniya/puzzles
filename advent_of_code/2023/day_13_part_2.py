puzzle_input = open("inputs/day_13_input.txt")


def distance(first_string, second_string):
    differences = 0
    for i, char in enumerate(first_string):
        if char != second_string[i]:
            differences += 1
    return differences


def solve(field):
    before_mirror = find_mirror(field)
    if not before_mirror:
        field = flip(field)
        before_mirror = find_mirror(field)
    else:
        before_mirror *= 100
    return before_mirror


def flip(field):
    new_field = [""] * len(field[0])
    for row in field:
        for i, char in enumerate(row):
            new_field[i] += char
    return new_field


def find_mirror(field):
    for i in range(len(field) - 1):
        smudge_found = False
        for j in range(min(i + 1, len(field) - i - 1)):
            comparison_row = field[i + j + 1]
            mirrored_row = field[i - j]
            if field[i + j + 1] != field[i - j]:
                if (
                        not smudge_found
                        and distance(comparison_row, mirrored_row) == 1
                ):
                    smudge_found = True
                    continue
                break
        else:
            if smudge_found:
                return i + 1


answer = 0
puzzle = []

for line in puzzle_input:
    if line == "\n":
        answer += solve(puzzle)
        puzzle = []
    else:
        puzzle.append(line.strip())
answer += solve(puzzle)
print(answer)
