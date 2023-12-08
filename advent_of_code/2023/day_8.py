from dataclasses import dataclass

puzzle_input = open("day_8_input.txt")

instructions = None
nodes = {}


@dataclass
class Node:
    left: str
    right: str


for line in puzzle_input:
    words = line.split()

    if not instructions:
        instructions = words[0]
        continue
    if not words:
        continue

    left = words[2][1:-1]
    right = words[3][:-1]

    nodes[words[0]] = (Node(left, right))

current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    for instruction in instructions:
        if instruction == "L":
            current_node = nodes[current_node].left
        else:
            current_node = nodes[current_node].right
        steps += 1
        if current_node == "ZZZ":
            break

print(steps)
