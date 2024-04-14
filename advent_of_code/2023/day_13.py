puzzle_input = open("inputs/day_13_input.txt")


def distance(first_string, second_string):
    differences = 0
    for i, char in enumerate(first_string):
        if char != second_string[i]:
            differences += 1
    return differences


def solve(field):
    before_mirror = find_mirror(field)
    before_mirror_2 = find_mirror_2(field)
    if not before_mirror or not before_mirror_2:
        field = flip(field)
    if not before_mirror:
        before_mirror = find_mirror(field)
    else:
        before_mirror *= 100
    if not before_mirror_2:
        before_mirror_2 = find_mirror_2(field)
    else:
        before_mirror_2 *= 100
    return before_mirror, before_mirror_2


def flip(field):
    new_field = [""] * len(field[0])
    for row in field:
        for i, char in enumerate(row):
            new_field[i] += char
    return new_field


def find_mirror(field):
    for i in range(len(field) - 1):
        for j in range(min(i + 1, len(field) - i - 1)):
            if field[i + j + 1] != field[i - j]:
                break
        else:
            return i + 1


def find_mirror_2(field):
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


answer, answer_2 = 0, 0
puzzle = []

for line in puzzle_input:
    if line == "\n":
        solution = solve(puzzle)
        answer += solution[0]
        answer_2 += solution[1]
        puzzle = []
    else:
        puzzle.append(line.strip())

solution = solve(puzzle)
answer += solution[0]
answer_2 += solution[1]

print(answer, answer_2)
