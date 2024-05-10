# TODO implement floodfill

puzzle_input = open("inputs/day_10.txt").readlines()

ns = "|"
ew = "-"
ne = "L"
nw = "J"
sw = "7"
se = "F"
ground = "."
start = "S"
wall = "#"


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
            maze[test_location] in continuations):
        return test_location


def simple_check(test_location, previous_location):
    if test_location != previous_location:
        return test_location


def find_next_location(current_location, previous_location):
    current_symbol = maze[current_location]
    if current_symbol == ns:
        return (
            simple_check((current_location[0], current_location[1] - 1),
                         previous_location) or
            simple_check((current_location[0], current_location[1] + 1),
                         previous_location)
        )
    elif current_symbol == ew:
        return (
            simple_check((current_location[0] + 1, current_location[1]),
                         previous_location) or
            simple_check((current_location[0] - 1, current_location[1]),
                         previous_location)
        )
    elif current_symbol == ne:
        return (
            simple_check((current_location[0], current_location[1] - 1),
                         previous_location) or
            simple_check((current_location[0] + 1, current_location[1]),
                         previous_location)
        )
    elif current_symbol == nw:
        return (
            simple_check((current_location[0] - 1, current_location[1]),
                         previous_location) or
            simple_check((current_location[0], current_location[1] - 1),
                         previous_location)
        )
    elif current_symbol == sw:
        return (
            simple_check((current_location[0], current_location[1] + 1),
                         previous_location) or
            simple_check((current_location[0] - 1, current_location[1]),
                         previous_location)
        )
    elif current_symbol == se:
        return (
            simple_check((current_location[0], current_location[1] + 1),
                         previous_location) or
            simple_check((current_location[0] + 1, current_location[1]),
                         previous_location)
        )


maze = {}

puzzle_size = (len(puzzle_input[0]) - 1, len(puzzle_input))

for y, line in enumerate(puzzle_input):
    line = line.strip()
    for x, char in enumerate(line):
        if char == start:
            start_location = (x, y)
        maze[x, y] = char
raw_maze = maze.copy()

for x in range(-1, puzzle_size[0] + 1):
    maze[x, -1] = ground
    maze[x, puzzle_size[1]] = ground

for y in range(-1, puzzle_size[1] + 1):
    maze[-1, y] = ground
    maze[puzzle_size[0], y] = ground

cur_loc = find_first_move(start_location)
prev_loc = start_location
steps = 1
loop_tiles = [start_location]

while cur_loc:
    steps += 1
    loop_tiles.append(cur_loc)
    cur_loc, prev_loc = (
        find_next_location(cur_loc, prev_loc),
        cur_loc
    )

answer = (steps - 1)//2


first_move = loop_tiles[1]
last_move = loop_tiles[-1]
first_last_ys = [first_move[0], last_move[0]]
first_last_xs = [first_move[1], last_move[1]]

if start_location[0] + 1 in first_last_ys:
    if start_location[1] + 1 in first_last_xs:
        start_symbol = se
    elif start_location[1] - 1 in first_last_xs:
        start_symbol = sw
    else:
        start_symbol = ns
elif start_location[0] - 1 in first_last_ys:
    if start_location[1] + 1 in first_last_xs:
        start_symbol = ne
    else:
        start_symbol = nw
else:
    start_symbol = ew

horizontal_complements = {ns: [ns, ne, se, ground],
                          ew: [ground],
                          ne: [ground],
                          nw: [ns, ne, ground],
                          sw: [ns, se, ground],
                          se: [ground]}

vertical_complements = {ns: [ground],
                        ew: [ew, ne, se, ground],
                        ne: [ew, sw, ground],
                        nw: [ew, ne, ground],
                        sw: [ground],
                        se: [ground]
                        }

maze[start_location[0], start_location[1]] = start_symbol
new_maze = {}

for x in range(-1, 2 * puzzle_size[0] + 1):
    new_maze[x, -1] = ground
    new_maze[x, 2 * puzzle_size[1]] = ground

for y in range(-1, 2 * puzzle_size[1] + 1):
    new_maze[-1, y] = ground
    new_maze[2 * puzzle_size[0], y] = ground

for x in range(-2, 2 * puzzle_size[0] + 2):
    new_maze[x, -2] = wall
    new_maze[x, 2 * puzzle_size[1] + 1] = wall

for y in range(-2, 2 * puzzle_size[1] + 2):
    new_maze[-2, y] = wall
    new_maze[2 * puzzle_size[0] + 1, y] = ground


for x in range(puzzle_size[0]):
    for y in range(puzzle_size[1]):
        tile = maze[x, y]
        new_maze[2 * x + 1, 2 * y + 1] = ground
        if tile == ground:
            new_maze[2 * x, 2 * y] = ground
            new_maze[2 * x + 1, 2 * y] = ground
            new_maze[2 * x, 2 * y + 1] = ground
        else:
            new_maze[2 * x, 2 * y] = wall
            if maze[x + 1, y] in horizontal_complements[tile]:
                new_maze[2 * x + 1, 2 * y] = ground
            else:
                new_maze[2 * x + 1, 2 * y] = wall
            if maze[x, y + 1] in vertical_complements[tile]:
                new_maze[2 * x, 2 * y + 1] = ground
            else:
                new_maze[2 * x, 2 * y + 1] = wall


def floodfill(location):
    if new_maze[location] != ground:
        return
    new_maze[location] = "inside"
    floodfill((location[0], location[1] + 1))
    floodfill((location[0], location[1] - 1))
    floodfill((location[0] - 1, location[1]))
    floodfill((location[0] + 1, location[1]))


floodfill((-1, -1))
tiles_in_loop = 0
for x in range(puzzle_size[0]):
    for y in range(puzzle_size[1]):
        if new_maze[2 * x, 2 * y] == ground:
            tiles_in_loop += 1


answer_2 = tiles_in_loop

print(answer, answer_2)
