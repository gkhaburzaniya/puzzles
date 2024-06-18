puzzle_input = open("inputs/day_15.txt").read()


def find_hash(step):
    value = 0
    for char in step:
        value = ((value + ord(char)) * 17) % 256
    return value


total_value = 0
for item in puzzle_input.strip().split(","):
    total_value += find_hash(item)

print(total_value)
