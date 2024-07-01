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


def reset_tiles():
    for tile in puzzle.values():
        tile.passed_beams.clear()


@cache
def beam_energizes(location, direction, passed_splitters=None):
    energized = set()
    passed_splitters = set(passed_splitters) if passed_splitters else set()
    start_location, start_direction = location, direction
    while True:
        try:
            tile = puzzle[location]
            energized.add(location)
        except KeyError:
            return frozenset(energized)

        if tile.symbol == UR_MIRROR:
            if direction == RIGHT:
                direction = UP
            elif direction == LEFT:
                direction = DOWN
            elif direction == UP:
                direction = RIGHT
            elif direction == DOWN:
                direction = LEFT
        elif tile.symbol == UL_MIRROR:
            if direction == RIGHT:
                direction = DOWN
            elif direction == LEFT:
                direction = UP
            elif direction == UP:
                direction = LEFT
            elif direction == DOWN:
                direction = RIGHT
        elif tile.symbol == V_SPLITTER and direction in (RIGHT, LEFT):
            if location in passed_splitters:
                return frozenset(energized)
            passed_splitters.add(location)
            energized = energized | beam_energizes(location, UP,
                                                   frozenset(passed_splitters))
            energized = energized | beam_energizes(location, DOWN,
                                                   frozenset(passed_splitters))
            return frozenset(energized)
        elif tile.symbol == H_SPLITTER and (direction in (UP, DOWN)):
            if location in passed_splitters:
                return frozenset(energized)
            passed_splitters.add(location)
            energized = energized | beam_energizes(location, RIGHT,
                                                   frozenset(passed_splitters))
            energized = energized | beam_energizes(location, LEFT,
                                                   frozenset(passed_splitters))
            return frozenset(energized)

        if direction == RIGHT:
            location = (location[0] + 1, location[1])
        elif direction == LEFT:
            location = (location[0] - 1, location[1])
        elif direction == UP:
            location = (location[0], location[1] - 1)
        elif direction == DOWN:
            location = (location[0], location[1] + 1)

        if (location, direction) == (start_location, start_direction):
            return frozenset(energized)


answer = len(beam_energizes((0, 0), RIGHT))
print(answer)
# max_energized_tiles = 0
#
#
# for x in range(max_x + 1):
#     current_tiles_energized = len(beam_energizes((x, 0), DOWN))
#     if current_tiles_energized > max_energized_tiles:
#         max_energized_tiles = current_tiles_energized
#     current_tiles_energized = len(beam_energizes((x, max_y), UP))
#     if current_tiles_energized > max_energized_tiles:
#         max_energized_tiles = current_tiles_energized
#
# for y in range(max_y + 1):
#     current_tiles_energized = len(beam_energizes((0, y), RIGHT))
#     if current_tiles_energized > max_energized_tiles:
#         max_energized_tiles = current_tiles_energized
#     current_tiles_energized = len(beam_energizes((max_x, y), RIGHT))
#     if current_tiles_energized > max_energized_tiles:
#         max_energized_tiles = current_tiles_energized
#
# answer_2 = max_energized_tiles
#
# print(answer, answer_2)
print(time.time() - start)
