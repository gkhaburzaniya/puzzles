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


def tiles_energized(starting_beam):
    beams = [starting_beam]
    energized_tiles = set()
    while beams:
        beam = beams.pop()
        try:
            tile = puzzle[beam.location]
        except KeyError:
            continue

        if beam.direction in tile.passed_beams:
            continue
        tile.passed_beams.add(beam.direction)
        energized_tiles.add(beam.location)

        if tile.symbol == UR_MIRROR:
            if beam.direction == RIGHT:
                beam.direction = UP
            elif beam.direction == LEFT:
                beam.direction = DOWN
            elif beam.direction == UP:
                beam.direction = RIGHT
            elif beam.direction == DOWN:
                beam.direction = LEFT
        elif tile.symbol == UL_MIRROR:
            if beam.direction == RIGHT:
                beam.direction = DOWN
            elif beam.direction == LEFT:
                beam.direction = UP
            elif beam.direction == UP:
                beam.direction = LEFT
            elif beam.direction == DOWN:
                beam.direction = RIGHT
        elif tile.symbol == V_SPLITTER and beam.direction in (RIGHT, LEFT):
            beam.direction = UP
            beams.append(Beam(beam.location, DOWN))
        elif tile.symbol == H_SPLITTER and (beam.direction in (UP, DOWN)):
            beam.direction = RIGHT
            beams.append(Beam(beam.location, LEFT))

        if beam.direction == RIGHT:
            beam.location = (beam.location[0] + 1, beam.location[1])
        elif beam.direction == LEFT:
            beam.location = (beam.location[0] - 1, beam.location[1])
        elif beam.direction == UP:
            beam.location = (beam.location[0], beam.location[1] - 1)
        elif beam.direction == DOWN:
            beam.location = (beam.location[0], beam.location[1] + 1)

        beams.append(beam)
    reset_tiles()
    return len(energized_tiles)


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
            if location in splitters_started:
                orig_splitter = orig_splitter or location
                temp_energized = energized
                raise PreemptiveError
            splitters_started.add(location)
            try:
                energized = energized | beam_energizes(location, UP)
            except PreemptiveError:
                energized = energized | temp_energized
            try:
                energized = energized | beam_energizes(location, DOWN)
            except PreemptiveError:
                energized = energized | temp_energized
            if orig_splitter == location or orig_splitter is None:
                orig_splitter = None
                splitters_started.clear()
                return frozenset(energized)
            else:
                temp_energized = energized
                raise PreemptiveError
        elif tile.symbol == H_SPLITTER and (direction in (UP, DOWN)):
            if location in splitters_started:
                temp_energized = energized
                orig_splitter = orig_splitter or location
                raise PreemptiveError
            splitters_started.add(location)
            try:
                energized = energized | beam_energizes(location, RIGHT)
            except PreemptiveError:
                energized = energized | temp_energized
            try:
                energized = energized | beam_energizes(location, LEFT)
            except PreemptiveError:
                energized = energized | temp_energized
            if orig_splitter == location or orig_splitter is None:
                orig_splitter = None
                splitters_started.clear()
                return frozenset(energized)
            else:
                temp_energized = energized
                raise PreemptiveError

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
