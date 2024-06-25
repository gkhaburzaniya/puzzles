from dataclasses import dataclass, field
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
        tile.passed_beams = set()


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
    return len(energized_tiles)


answer = tiles_energized(Beam((0, 0), RIGHT))
max_energized_tiles = 0


for x in range(max_x + 1):
    current_tiles_energized = tiles_energized(Beam((x, 0), DOWN))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    reset_tiles()
    current_tiles_energized = tiles_energized(Beam((x, max_y), UP))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    reset_tiles()

for y in range(max_y + 1):
    current_tiles_energized = tiles_energized(Beam((0, y), RIGHT))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    reset_tiles()
    current_tiles_energized = tiles_energized(Beam((max_x, y), LEFT))
    if current_tiles_energized > max_energized_tiles:
        max_energized_tiles = current_tiles_energized
    reset_tiles()

answer_2 = max_energized_tiles

print(answer, answer_2)
print(time.time() - start)
