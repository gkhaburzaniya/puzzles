puzzle_input = open("inputs/day_11_input.txt")

rows = [line.strip() for line in puzzle_input]
columns = [""] * len(rows[0])
for row in rows:
    for i, char in enumerate(row):
        columns[i] += char
        if "#" not in row:
            columns[i] += char

rows = [""] * len(columns[0])
new_columns = []
for column in columns:
    new_columns.append(column)
    if "#" not in column:
        new_columns.append(column)
    for i, char in enumerate(column):
        rows[i] += char
        if "#" not in column:
            rows[i] += char

columns = new_columns

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
        total_distance += distance

print(total_distance)
