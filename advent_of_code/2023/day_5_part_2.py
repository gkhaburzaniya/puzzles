from dataclasses import dataclass

puzzle_input = open("inputs/day_5.txt")

heading = "seeds"
seeds = []
soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []

all_transforms = [locations, humidities, temperatures, lights, waters, fertilizers, soils]

@dataclass
class Transform:
    destination_start: int
    sourse_start: int
    length: 0

    def __lt__(self, other):
        return self.destination_start < other.destination_start


def transform(words, destination, sourse):
    if not words:
        destination.extend(sourse)
        return
    destination_start = int(words[0])
    sourse_start = int(words[1])
    length = int(words[2])
    items_to_del = []
    for i, item in enumerate(sourse):
        if sourse_start <= item < sourse_start + length:
            destination.append(item - sourse_start + destination_start)
            items_to_del.append(i)
    for i in reversed(items_to_del):
        del sourse[i]


for line in puzzle_input:
    if "seed-to-soil" in line:
        heading = "seed-to-soil"
        continue
    elif "soil-to-fertilizer" in line:
        heading = "soil-to-fertilizer"
        continue
    elif "fertilizer-to-water" in line:
        heading = "fertilizer-to-water"
        continue
    elif "water-to-light" in line:
        heading = "water-to-light"
        continue
    elif "light-to-temperature" in line:
        heading = "light-to-temperature"
        continue
    elif "temperature-to-humidity" in line:
        heading = "temperature-to-humidity"
        continue
    elif "humidity-to-location" in line:
        heading = "humidity-to-location"
        continue
    elif line == "\n":
        continue

    words = line.split()
    if heading == "seeds":
        for i, word in enumerate(words[1:]):
            if i % 2 == 0:
                start = int(word)
            else:
                seeds.append((start, start + int(word)))
    elif heading == "seed-to-soil":
        soils.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "soil-to-fertilizer":
        fertilizers.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "fertilizer-to-water":
        waters.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "water-to-light":
        lights.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "light-to-temperature":
        temperatures.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "temperature-to-humidity":
        humidities.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "humidity-to-location":
        locations.append(Transform(int(words[0]), int(words[1]), int(words[2])))

for i, transform_type in enumerate(all_transforms):
    all_transforms[i] = sorted(transform_type)


def check_num(num):
    i = num
    for transform_type in all_transforms:
        for transform in transform_type:
            if i < transform.destination_start:
                break
            if transform.destination_start <= i < transform.destination_start + transform.length:
                i = i - transform.destination_start + transform.sourse_start
                break
    for seed in seeds:
        if seed[0] <= i < seed[1]:
            return num

import itertools
for j in itertools.count():
    if check_num(j):
        print(j)
        break
