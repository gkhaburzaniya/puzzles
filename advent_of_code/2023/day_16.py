from dataclasses import dataclass
from typing import Set

puzzle_input = open("inputs/day_16.txt")

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
    passed_beams: Set[str] = set


field = {(x, y): Tile(char)
         for y, line in enumerate(puzzle_input)
         for x, char in enumerate(line.strip())}
beams = [Beam((0, 0), RIGHT)]

energized_tiles = {field[0, 0]}
while beams:
    beam = beams.pop()
    tile = field[beam.location]
    if beam.direction in tile.passed_beams:
        continue
    if beam.direction == RIGHT:
        beam.location = (beam.location[0] + 1, beam.location[1])
    elif beam.direction == LEFT:
        beam.location = (beam.location[0] - 1, beam.location[1])
    elif beam.direction == UP:
        beam.location = (beam.location[0], beam.location[1] - 1)
    elif beam.direction == DOWN:
        beam.location = (beam.location[0], beam.location[1] + 1)
