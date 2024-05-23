import time
start_time = time.time()
puzzle_input = open("inputs/day_10.txt")

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
loop_tiles = [start_location]
steps = 1
while current_location != start_location:
    steps += 1
    loop_tiles.append(current_location)
    current_location, previous_location = (
        find_next_location(current_location, previous_location),
        current_location
    )

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


tiles_in_loop = []

for y in range(len(maze)):
    for x in range(puzzle_size):
        tiles_above = []
        if (y, x) not in loop_tiles:
            for loop_tile in loop_tiles:
                if loop_tile[0] < y and loop_tile[1] == x:
                    maze_symbol = maze[loop_tile[0]][loop_tile[1]]
                    if maze_symbol == start:
                        maze_symbol = start_symbol
                    if maze_symbol != ns:
                        tiles_above.append(maze_symbol)
        num_up = 0
        nws = 0
        nes = 0
        sws = 0
        ses = 0
        # "F" + "J" means 1, "F" + "L" means 2
        for symbol in tiles_above:
            if symbol == ew:
                num_up += 1
            if symbol == nw:
                nws += 1
            if symbol == ne:
                nes += 1
            if symbol == sw:
                sws += 1
            if symbol == se:
                ses += 1
        num_up += ses + nes
        if num_up % 2 == 1:
            tiles_in_loop.append((x, y))

print(len(tiles_in_loop))
print(time.time() - start_time)
import day_10
missing_tiles = [tile for tile in tiles_in_loop if tile not in day_10.orig_tiles]
extra_tiles = [tile for tile in day_10.orig_tiles if tile not in tiles_in_loop]
same_tiles = [tile for tile in tiles_in_loop if tile in day_10.orig_tiles]

print("Missing Tiles")
print(sorted(missing_tiles))
print(len(missing_tiles))
print("Extra Tiles")
print(sorted(extra_tiles))
print(len(extra_tiles))
print("Same Tiles")
print(sorted(same_tiles))
print(len(same_tiles))
