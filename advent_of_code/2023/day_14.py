puzzle_input = open("inputs/day_14.txt")

EMPTY = "."
ROUND = "O"
CUBE = "#"

total = 0

field = [[*line.strip()] for line in puzzle_input]
for i, row in enumerate(field):
    for j, space in enumerate(row):
        if space == ROUND:
            for k in range(1, i + 1):
                if field[i - k][j] != EMPTY:
                    field[i][j] = EMPTY
                    field[i - k + 1][j] = ROUND
                    total += len(field) - (i - k + 1)
                    break
            else:
                field[i][j] = EMPTY
                field[0][j] = ROUND
                total += len(field)

print(total)
