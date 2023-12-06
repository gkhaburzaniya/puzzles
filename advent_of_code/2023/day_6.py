puzzle_input = open("day_6_input.txt").readlines()

times = [int(time) for time in puzzle_input[0].split() if time.isdigit()]
records = [int(record) for record in puzzle_input[1].split() if record.isdigit()]

multiple = 1
for i, time in enumerate(times):
    ways_to_beat = 0
    for j in range(time):
        if j * (time - j) > records[i]:
            ways_to_beat += 1
    multiple *= ways_to_beat

print(multiple)
