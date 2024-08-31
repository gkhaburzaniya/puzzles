puzzle_input = open("inputs/day_4.txt").readlines()

total = 0

instances = [1] * len(puzzle_input)
for i, line in enumerate(puzzle_input):
    winning_numbers = []
    your_numbers = False
    score = 0
    matches = 0
    for value in line.split()[2:]:
        if value != "|" and not your_numbers:
            winning_numbers.append(int(value))
        elif value == "|":
            your_numbers = True
        elif your_numbers and int(value) in winning_numbers:
            matches += 1
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score
    for j in range(matches):
        instances[i+1+j] += instances[i]

total_2 = sum(instances)

print(total, total_2)
