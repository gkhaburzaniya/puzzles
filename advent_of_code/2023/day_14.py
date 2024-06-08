import time
from functools import cache
start_time = time.time()
puzzle_input = open("inputs/day_14.txt")

EMPTY = "."
ROUND = "O"
CUBE = "#"
field = tuple((*line.strip(),) for line in puzzle_input)
max_y = len(field) - 1
max_x = len(field[0]) - 1


def load():
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


def print_field():
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(field[y][x], end="")
        print("")


field = tilt_north(field)
answer = load()
field = tilt_west(field)
field = tilt_south(field)
field = tilt_east(field)
print_field()
print(load())

for _ in range(2):
    field = tilt_north(field)
    field = tilt_west(field)
    field = tilt_south(field)
    field = tilt_east(field)
    print_field()
    print(load())
    if tilt_north.cache_info().hits > 0:
        break

answer_2 = load()

print(answer, answer_2)
print(time.time() - start_time)
