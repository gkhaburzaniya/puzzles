from functools import cache
puzzle_input = open("inputs/day_14.txt")

EMPTY = "."
ROUND = "O"
CUBE = "#"
start_field = tuple((*line.strip(),) for line in puzzle_input)
max_y = len(start_field) - 1
max_x = len(start_field[0]) - 1


def load(field):
    north_load = 0
    for y, row in enumerate(field):
        for x, space in enumerate(row):
            if space == ROUND:
                north_load += max_y - y + 1
    return north_load


@cache
def tilt_north(field):
    field = [list(row) for row in field]
    for y, row in enumerate(field):
        for x, space in enumerate(row):
            if space == ROUND:
                for k in range(1, y + 1):
                    if field[y - k][x] != EMPTY:
                        field[y][x] = EMPTY
                        field[y - k + 1][x] = ROUND
                        break
                else:
                    field[y][x] = EMPTY
                    field[0][x] = ROUND
    return tuple(tuple(row) for row in field)


@cache
def tilt_south(field):
    field = [list(row) for row in field]
    for y in range(max_y, -1, -1):
        row = field[y]
        for x, space in enumerate(row):
            if space == ROUND:
                for k in range(1, max_y - y + 1):
                    if field[y + k][x] != EMPTY:
                        field[y][x] = EMPTY
                        field[y + k - 1][x] = ROUND
                        break
                else:
                    field[y][x] = EMPTY
                    field[max_y][x] = ROUND
    return tuple(tuple(row) for row in field)


@cache
def tilt_west(field):
    field = [list(row) for row in field]
    for y, row in enumerate(field):
        for x, space in enumerate(row):
            if space == ROUND:
                for k in range(1, x + 1):
                    if field[y][x - k] != EMPTY:
                        field[y][x] = EMPTY
                        field[y][x - k + 1] = ROUND
                        break
                else:
                    field[y][x] = EMPTY
                    field[y][0] = ROUND
    return tuple(tuple(row) for row in field)


@cache
def tilt_east(field):
    field = [list(row) for row in field]
    for y, row in enumerate(field):
        for x in range(max_x, -1, -1):
            space = field[y][x]
            if space == ROUND:
                for k in range(1, max_x - x + 1):
                    if field[y][x + k] != EMPTY:
                        field[y][x] = EMPTY
                        field[y][x + k - 1] = ROUND
                        break
                else:
                    field[y][x] = EMPTY
                    field[y][max_x] = ROUND
    return tuple(tuple(row) for row in field)


new_field = tilt_north(start_field)
answer = load(new_field)
new_field = tilt_west(new_field)
new_field = tilt_south(new_field)
new_field = tilt_east(new_field)

fields = []
total_cycles = 1_000_000_000
inner_cycles = 1
while inner_cycles < total_cycles:
    new_field = tilt_north(new_field)
    new_field = tilt_west(new_field)
    new_field = tilt_south(new_field)
    new_field = tilt_east(new_field)
    inner_cycles += 1
    if tilt_north.cache_info().hits > 0:
        try:
            last_hit = len(fields) - fields[::-1].index(new_field) - 1
            cycle_length = len(fields) - last_hit
            break
        except ValueError:
            fields.append(new_field)

remainder = (total_cycles - inner_cycles - 1) % cycle_length
answer_2 = load(fields[remainder])

print(answer, answer_2)
