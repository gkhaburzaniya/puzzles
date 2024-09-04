from dataclasses import dataclass

puzzle_input = open("inputs/day_17.txt").readlines()


@dataclass
class Node:
    x: int
    y: int
    path: list
    distance: int


height = len(puzzle_input)
width = len(puzzle_input[0])

nodes = {}
for y, line in enumerate(puzzle_input):
    for x, char in enumerate(line):
        nodes[x, y] = char


# adjacent_nodes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
