puzzle_input = open("puzzle_input.txt").read()
elves = [[]]
current_elf = 0

for line in puzzle_input.split("\n"):
    if line == "":
        current_elf += 1
        elves.append([])
    else:
        elves[current_elf].append(int(line))

elf_totals = [sum(elf) for elf in elves]

print(max(elf_totals))

top_three = []
for i in range(3):
    top_three.append(max(elf_totals))
    elf_totals.remove(max(elf_totals))

print(sum(top_three))
