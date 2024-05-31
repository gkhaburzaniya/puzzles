puzzle_input = open("inputs/day_14.txt")

EMPTY = "."
ROUND = "O"
CUBE = "#"

total = 0

field = [[*line.strip()] for line in puzzle_input]
for y, row in enumerate(field):
    for x, space in enumerate(row):
        if space == ROUND:
            for k in range(1, y + 1):
                if field[y - k][x] != EMPTY:
                    field[y][x] = EMPTY
                    field[y - k + 1][x] = ROUND
                    total += len(field) - (y - k + 1)
                    break
            else:
                field[y][x] = EMPTY
                field[0][x] = ROUND
                total += len(field)
answer = total
print(answer)
