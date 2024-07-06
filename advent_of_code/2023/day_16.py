from dataclasses import dataclass, field
from functools import cache

import time
start = time.time()

puzzle_input = open("inputs/day_16.txt").read().splitlines()

EMPTY = "."
UR_MIRROR = "/"
UL_MIRROR = "\\"
V_SPLITTER = "|"
H_SPLITTER = "-"
LEFT = "<"
RIGHT = ">"
UP = "^"
DOWN = "v"
RIGHTLEFT = RIGHT + LEFT
UPDOWN = UP + DOWN


def right(point):
    return point[0] + 1, point[1]


def left(point):
    return point[0] - 1, point[1]


def up(point):
    return point[0], point[1] - 1


def down(point):
    return point[0], point[1] + 1


TRANSFORM_DICT = {(EMPTY, RIGHT): (RIGHT, right),
                  (EMPTY, LEFT): (LEFT, left),
                  (EMPTY, UP): (UP, up),
                  (EMPTY, DOWN): (DOWN, down),
                  (UR_MIRROR, RIGHT): (UP, up),
                  (UR_MIRROR, LEFT): (DOWN, down),
                  (UR_MIRROR, UP): (RIGHT, right),
                  (UR_MIRROR, DOWN): (LEFT, left),
                  (UL_MIRROR, RIGHT): (DOWN, down),
                  (UL_MIRROR, LEFT): (UP, up),
                  (UL_MIRROR, UP): (LEFT, left),
                  (UL_MIRROR, DOWN): (RIGHT, right),
                  (V_SPLITTER, UP): (UP, up),
                  (V_SPLITTER, DOWN): (DOWN, down),
                  (H_SPLITTER, RIGHT): (RIGHT, right),
                  (H_SPLITTER, LEFT): (LEFT, left)}


@dataclass
class Beam:
    location: tuple
    direction: str


@dataclass
class Tile:
    symbol: str
    passed_beams: set = field(default_factory=set)


max_x = len(puzzle_input[0]) - 1
max_y = len(puzzle_input) - 1
puzzle = {(x, y): Tile(char)
          for y, line in enumerate(puzzle_input)
          for x, char in enumerate(line)}


class PreemptiveError(Exception):
    pass


splitters_started = set()
temp_energized = set()
orig_splitter = None


@cache
def beam_energizes(location, direction):
    global temp_energized, orig_splitter

    energized = set()
    start_location, start_direction = location, direction
    while True:
        try:
            tile = puzzle[location]
            energized.add(location)
        except KeyError:
            return frozenset(energized)

        if tile.symbol == V_SPLITTER and direction in RIGHTLEFT:
            if location in splitters_started:
                orig_splitter = orig_splitter or location
                temp_energized = energized
                raise PreemptiveError
            splitters_started.add(location)
            try:
                energized.update(beam_energizes(location, UP))
            except PreemptiveError:
                energized.update(temp_energized)
            try:
                energized.update(beam_energizes(location, DOWN))
            except PreemptiveError:
                energized.update(temp_energized)
            if orig_splitter == location or orig_splitter is None:
                orig_splitter = None
                splitters_started.clear()
                return frozenset(energized)
            else:
                temp_energized = energized
                raise PreemptiveError
        elif tile.symbol == H_SPLITTER and direction in UPDOWN:
            if location in splitters_started:
                temp_energized = energized
                orig_splitter = orig_splitter or location
                raise PreemptiveError
            splitters_started.add(location)
            try:
                energized.update(beam_energizes(location, RIGHT))
            except PreemptiveError:
                energized.update(temp_energized)
            try:
                energized.update(beam_energizes(location, LEFT))
            except PreemptiveError:
                energized.update(temp_energized)
            if orig_splitter == location or orig_splitter is None:
                orig_splitter = None
                splitters_started.clear()
                return frozenset(energized)
            else:
                temp_energized = energized
                raise PreemptiveError
        else:
            direction, change = TRANSFORM_DICT[(tile.symbol, direction)]
            location = change(location)

        if (location, direction) == (start_location, start_direction):
            return frozenset(energized)


answer = len(beam_energizes((0, 0), RIGHT))
max_energized_tiles = 0


for x in range(max_x + 1):
    current_tiles_energized = len(beam_energizes((x, 0), DOWN))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    current_tiles_energized = len(beam_energizes((x, max_y), UP))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized

for y in range(max_y + 1):
    current_tiles_energized = len(beam_energizes((0, y), RIGHT))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    current_tiles_energized = len(beam_energizes((max_x, y), RIGHT))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized

answer_2 = max_energized_tiles

print(answer, answer_2)
print(time.time() - start)
