puzzle_input = open("inputs/day_9_input.txt")

total = 0
for line in puzzle_input:
    value_sets = [[int(word) for word in line.split()]]
    while set(value_sets[-1]) != {0}:
        new_values = []
        for i, value in enumerate(value_sets[-1][1:]):
            new_values.append(value - value_sets[-1][i])
        value_sets.append(new_values)
    value_sets.reverse()
    for i, values in enumerate(value_sets[1:]):
        values.append(values[-1]+value_sets[i][-1])
    total += value_sets[-1][-1]

print(total)
