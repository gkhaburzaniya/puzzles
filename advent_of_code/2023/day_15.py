puzzle_input = open("inputs/day_15.txt").read()

total_value = 0
for step in puzzle_input.strip().split(","):
    current_value = 0
    for char in step:
        current_value = ((current_value + ord(char)) * 17) % 256
    total_value += current_value

print(total_value)
