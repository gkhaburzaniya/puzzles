puzzle_input = open("inputs/day_4_input.txt")

total = 0

for line in puzzle_input:
    winning_numbers = []
    your_numbers = False
    score = 0
    for value in line.split()[2:]:
        if value != "|" and not your_numbers:
            winning_numbers.append(int(value))
        elif value == "|":
            your_numbers = True
        elif your_numbers and int(value) in winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
    total += score

print(total)
