puzzle_input = open("inputs/day_11.txt")
expansion_rate = 1000000

rows = [line.strip() for line in puzzle_input]
columns = [""] * len(rows[0])
big_rows = []
big_columns = []
for j, row in enumerate(rows):
    if "#" not in row:
        big_rows.append(j)
    for i, char in enumerate(row):
        columns[i] += char

for i, column in enumerate(columns):
    if "#" not in column:
        big_columns.append(i)


galaxies = []
for x, column in enumerate(columns):
    for y, char in enumerate(column):
        if char == "#":
            galaxies.append((x, y))

total_distance = 0
for _ in range(len(galaxies)-1):
    working_galaxy = galaxies.pop()
    for galaxy in galaxies:
        distance = (abs(galaxy[0] - working_galaxy[0])
                    + abs(galaxy[1] - working_galaxy[1]))
        for big_column in big_columns:
            if (galaxy[0] < big_column < working_galaxy[0] or
                    working_galaxy[0] < big_column < galaxy[0]):
                distance += expansion_rate - 1
        for big_row in big_rows:
            if (galaxy[1] < big_row < working_galaxy[1] or
                    working_galaxy[1] < big_row < galaxy[1]):
                distance += expansion_rate - 1
        total_distance += distance

print(total_distance)
