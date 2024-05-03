puzzle_input = open("inputs/day_9.txt")

total = 0
total_2 = 0
for line in puzzle_input:
    value_sets = [[int(word) for word in line.split()]]
    while set(value_sets[-1]) != {0}:
        new_values = []
        for i, value in enumerate(value_sets[-1][1:]):
            new_values.append(value - value_sets[-1][i])
        value_sets.append(new_values)
    value_sets.reverse()
    for i, values in enumerate(value_sets[1:]):
        values.append(values[-1] + value_sets[i][-1])
        values.insert(0, (values[0] - value_sets[i][0]))

    total += value_sets[-1][-1]
    total_2 += value_sets[-1][0]

print(total, total_2)
