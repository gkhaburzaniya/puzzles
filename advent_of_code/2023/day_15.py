puzzle_input = open("inputs/day_14.txt")

for line in puzzle_input:
    current_value = 0
    for char in line.strip():
        current_value = ((current_value + ord(char)) * 17) % 256

print(current_value)
