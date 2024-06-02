import time
start_time = time.time()
puzzle_input = open("inputs/day_14.txt")

EMPTY = "."
ROUND = "O"
CUBE = "#"
field = [[*line.strip()] for line in puzzle_input]
max_y = len(field) - 1
max_x = len(field[0]) - 1


def load():
    north_load = 0
    for y, row in enumerate(field):
        for x, space in enumerate(row):
            if space == ROUND:
                north_load += max_y - y + 1
    return north_load


def tilt_north():
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


def tilt_south():
    for y, row in enumerate(field):
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


def tilt_west():
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


def tilt_east():
    for y, row in enumerate(field):
        for x, space in enumerate(row):
            if space == ROUND:
                for k in range(1, max_x - x + 1):
                    if field[y][x + k] != EMPTY:
                        field[y][x] = EMPTY
                        field[y][x + k - 1] = ROUND
                        break
                else:
                    field[y][x] = EMPTY
                    field[y][max_x] = ROUND


tilt_north()
answer = load()
tilt_west()
tilt_south()
tilt_east()

for _ in range(100_000):
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()

answer_2 = load()

print(answer, answer_2)
print(time.time() - start_time)
