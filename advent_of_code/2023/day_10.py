puzzle_input = open("inputs/day_10_input.txt")

ns = "|"
ew = "-"
ne = "L"
nw = "J"
sw = "7"
se = "F"
ground = "."
start = "S"
maze = []
start_location = None


def find_first_move(current_location, previous_location=None):

    return (
        check_location((current_location[0] - 1, current_location[1]),
                       previous_location, [ns, sw, se]) or
        check_location((current_location[0], current_location[1] + 1),
                       previous_location, [ew, nw, sw]) or
        check_location((current_location[0] + 1, current_location[1]),
                       previous_location, [ns, ne, nw]) or
        check_location((current_location[0], current_location[1] - 1),
                       previous_location, [ew, ne, se])
    )


def check_location(test_location, previous_location, continuations):
    if (test_location != previous_location and
            maze[test_location[0]][test_location[1]] in continuations):
        return test_location


def simple_check(test_location, previous_location):
    if test_location != previous_location:
        return test_location


def find_next_location(current_location, previous_location):
    current_symbol = maze[current_location[0]][current_location[1]]
    if current_symbol == ns:
        return (
            simple_check((current_location[0]-1, current_location[1]),
                           previous_location) or
            simple_check((current_location[0] + 1, current_location[1]),
                           previous_location)
        )
    elif current_symbol == ew:
        return (
            simple_check((current_location[0], current_location[1] + 1),
                           previous_location) or
            simple_check((current_location[0], current_location[1] - 1),
                           previous_location)
        )
    elif current_symbol == ne:
        return (
            simple_check((current_location[0] - 1, current_location[1]),
                           previous_location) or
            simple_check((current_location[0], current_location[1] + 1),
                           previous_location)
        )
    elif current_symbol == nw:
        return (
            simple_check((current_location[0], current_location[1] - 1),
                           previous_location) or
            simple_check((current_location[0] - 1, current_location[1]),
                           previous_location)
        )
    elif current_symbol == sw:
        return (
            simple_check((current_location[0] + 1, current_location[1]),
                           previous_location) or
            simple_check((current_location[0], current_location[1] - 1),
                           previous_location)
        )
    elif current_symbol == se:
        return (
            simple_check((current_location[0] + 1, current_location[1]),
                           previous_location) or
            simple_check((current_location[0], current_location[1] + 1),
                           previous_location)
        )


for i, line in enumerate(puzzle_input):
    if i == 0:
        puzzle_size = len(line)
        maze.append([ground] * puzzle_size)
    maze.append([])
    for j, char in enumerate(line):
        if j == 0:
            maze[i+1].append(ground)
        if char == start:
            start_location = (i+1, j+1)
        maze[i+1].append(char)
    maze[i+1].append(ground)
maze.append([ground] * puzzle_size)


current_location = find_first_move(start_location)
previous_location = start_location
steps = 1
while current_location:
    steps += 1
    current_location, previous_location = (
        find_next_location(current_location, previous_location),
        current_location
    )

print((steps - 1)/2)
