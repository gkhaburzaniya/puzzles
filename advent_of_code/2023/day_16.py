puzzle_input = open("inputs/day_16.txt")


field = {(x, y): char
         for y, line in enumerate(puzzle_input)
         for x, char in enumerate(line.strip())}
