from dataclasses import dataclass, field

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
    passed_beams: set = field(default_factory=set)


puzzle = {(x, y): Tile(char)
          for y, line in enumerate(puzzle_input)
          for x, char in enumerate(line.strip())}


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
print(answer)
