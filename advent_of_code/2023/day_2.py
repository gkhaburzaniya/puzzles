puzzle_input = open("inputs/day_2.txt")

red = 12
green = 13
blue = 14

total = 0
total_2 = 0

for i, game in enumerate(puzzle_input):
    game_id = i + 1
    min_red = 0
    min_green = 0
    min_blue = 0
    matches = game.split(':')[1].split(";")
    for match in matches:
        pebbles = match.split(',')

        for pebble in pebbles:
            red_index = pebble.find("red")
            if red_index != -1 and int(pebble[1:red_index - 1]) > min_red:
                min_red = int(pebble[1:red_index - 1])
            green_index = pebble.find("green")
            if green_index != -1 and int(pebble[1:green_index - 1]) > min_green:
                min_green = int(pebble[1:green_index - 1])
            blue_index = pebble.find("blue")
            if blue_index != -1 and int(pebble[1:blue_index - 1]) > min_blue:
                min_blue = int(pebble[1:blue_index - 1])

    if min_red <= red and min_green <= green and min_blue <= blue:
        total += game_id
    total_2 += min_red * min_green * min_blue

print(total, total_2)
