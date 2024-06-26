from collections import defaultdict

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


def north(loc):
    return loc[0], loc[1] - 1


def east(loc):
    return loc[0] + 1, loc[1]


def south(loc):
    return loc[0], loc[1] + 1


def west(loc):
    return loc[0] - 1, loc[1]


def find_first_move(current_location, previous_location=None):

    return (
        check_location(north(current_location),
                       previous_location, [ns, sw, se]) or
        check_location(east(current_location),
                       previous_location, [ew, nw, sw]) or
        check_location(south(current_location),
                       previous_location, [ns, ne, nw]) or
        check_location(west(current_location),
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
            simple_check(north(current_location), previous_location) or
            simple_check(south(current_location), previous_location)
        )
    elif current_symbol == ew:
        return (
            simple_check(east(current_location), previous_location) or
            simple_check(west(current_location), previous_location)
        )
    elif current_symbol == ne:
        return (
            simple_check(north(current_location), previous_location) or
            simple_check(east(current_location), previous_location)
        )
    elif current_symbol == nw:
        return (
            simple_check(north(current_location), previous_location) or
            simple_check(west(current_location), previous_location)
        )
    elif current_symbol == sw:
        return (
            simple_check(south(current_location), previous_location) or
            simple_check(west(current_location), previous_location)
        )
    elif current_symbol == se:
        return (
            simple_check(south(current_location), previous_location) or
            simple_check(east(current_location), previous_location)
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
last_move = loop_tiles[-2]
first_last_xs = [first_move[0], last_move[0]]
first_last_ys = [first_move[1], last_move[1]]


if start_location[0] + 1 in first_last_xs:
    if start_location[1] + 1 in first_last_ys:
        start_symbol = se
    elif start_location[1] - 1 in first_last_ys:
        start_symbol = ne
    else:
        start_symbol = ew
elif start_location[0] - 1 in first_last_xs:
    if start_location[1] + 1 in first_last_ys:
        start_symbol = sw
    else:
        start_symbol = nw
else:
    start_symbol = ns

maze[start_location[0], start_location[1]] = start_symbol
loop_tiles = {tile: maze[tile] for tile in loop_tiles}

horizontal_complements = {ns: [ns, ne, se, ground],
                          ew: [],
                          ne: [],
                          nw: [ns, ne, se, ground],
                          sw: [ns, ne, se, ground],
                          se: []}

vertical_complements = {ns: [],
                        ew: [ew, sw, se, ground],
                        ne: [ew, sw, se, ground],
                        nw: [ew, sw, se, ground],
                        sw: [],
                        se: []
                        }

new_maze = defaultdict(lambda: ground)

for key in maze.keys():
    if key not in loop_tiles:
        maze[key] = ground

for key in loop_tiles:
    tile = maze[key]
    x, y = key[0], key[1]
    new_maze[2 * x, 2 * y] = wall
    if maze[x + 1, y] not in horizontal_complements[tile]:
        new_maze[2 * x + 1, 2 * y] = wall
    if maze[x, y + 1] not in vertical_complements[tile]:
        new_maze[2 * x, 2 * y + 1] = wall

new_start_location = (2 * start_location[0], 2 * start_location[1])
start_nodes = [north(east(new_start_location)),
               south(east(new_start_location)),
               south(west(new_start_location)),
               north(west(new_start_location)),]
start_nodes = [node for node in start_nodes if new_maze[node] == ground]
nodes_to_check = [start_nodes.pop()]
tiles_in_loop = []

while nodes_to_check:
    location = nodes_to_check.pop()
    if location[0] == -1 or location[1] == -1:
        for tile in tiles_in_loop:
            new_maze[tile] = ground
        tiles_in_loop = []
    elif new_maze[location] == ground:
        new_maze[location] = "inside"
        if location[0] % 2 == 0 and location[1] % 2 == 0:
            tiles_in_loop.append(location)
        nodes_to_check.append(north(location))
        nodes_to_check.append(east(location))
        nodes_to_check.append(south(location))
        nodes_to_check.append(west(location))
    if not nodes_to_check and not tiles_in_loop:
        nodes_to_check = [start_nodes.pop()]

# orig_tiles = [(tile[0]//2 + 1, tile[1]//2 + 1) for tile in tiles_in_loop]
answer_2 = len(tiles_in_loop)

print(answer, answer_2)
