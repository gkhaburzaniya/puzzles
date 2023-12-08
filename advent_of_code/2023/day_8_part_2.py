from dataclasses import dataclass
from math import lcm

puzzle_input = open("day_8_input.txt")

instructions = None
nodes = {}
starting_nodes = []


@dataclass
class Node:
    node: str
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
    node = Node(words[0], left, right)

    nodes[node.node] = node

    if node.node[2] == "A":
        starting_nodes.append(node)


steps = 0
finished_nodes = []

for starting_node in starting_nodes:
    current_node = starting_node
    while current_node.node[2] != "Z":
        for instruction in instructions:
            if instruction == "L":
                current_node = nodes[current_node.left]
            else:
                current_node = nodes[current_node.right]
            steps += 1
            if current_node.node[2] == "Z":
                finished_nodes.append(steps)
                steps = 0
                break

print(lcm(*finished_nodes))
