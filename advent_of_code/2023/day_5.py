#!/usr/bin/pypy

import time

from dataclasses import dataclass

start = time.time()

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

seeds_2 = []
soils_2 = []
fertilizers_2 = []
waters_2 = []
lights_2 = []
temperatures_2 = []
humidities_2 = []
locations_2 = []


all_transforms = [locations_2, humidities_2, temperatures_2, lights_2,
                  waters_2, fertilizers_2, soils_2]


@dataclass
class Transform:
    destination_start: int
    sourse_start: int
    length: 0

    def __lt__(self, other):
        return self.destination_start < other.destination_start

    @property
    def destination_end(self):
        return self.destination_start + self.length


def transform(tform, destination, sourse):
    if not words:
        destination.extend(sourse)
        return
    items_to_del = []
    for i, item in enumerate(sourse):
        if tform.sourse_start <= item < tform.sourse_start + tform.length:
            destination.append(
                item - tform.sourse_start + tform.destination_start)
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
        for word in words:
            if word.isdigit():
                seeds.append(int(word))
        for i, word in enumerate(words[1:]):
            if i % 2 == 0:
                word_start = int(word)
            else:
                seeds_2.append((start, word_start + int(word)))
        continue

    destination_start, sourse_start, length = (
        int(words[0]), int(words[1]), int(words[2]))
    tform = Transform(destination_start, sourse_start, length)

    if heading == "seed-to-soil":
        transform(tform, soils, seeds)

        soils_2.append(tform)
    elif heading == "soil-to-fertilizer":
        soils.extend(seeds)
        seeds = []
        transform(tform, fertilizers, soils)

        fertilizers_2.append(tform)
    elif heading == "fertilizer-to-water":
        fertilizers.extend(soils)
        soils = []
        transform(tform, waters, fertilizers)

        waters_2.append(tform)
    elif heading == "water-to-light":
        waters.extend(fertilizers)
        fertilizers = []
        transform(tform, lights, waters)

        lights_2.append(tform)
    elif heading == "light-to-temperature":
        lights.extend(waters)
        waters = []
        transform(tform, temperatures, lights)

        temperatures_2.append(tform)
    elif heading == "temperature-to-humidity":
        temperatures.extend(lights)
        lights = []
        transform(tform, humidities, temperatures)

        humidities_2.append(tform)
    elif heading == "humidity-to-location":
        humidities.extend(temperatures)
        temperatures = []
        transform(tform, locations, humidities)

        locations_2.append(tform)

locations.extend(humidities)


answer = min(locations)

for i, transform_type in enumerate(all_transforms):
    all_transforms[i] = sorted(transform_type)

ranges = []
num = 0
for transform in locations_2:
    ranges.append((num, transform.destination_start, num))
    ranges.append((transform.destination_start,
                   transform.destination_end,
                   transform.destination_start))
    num = transform.destination_end


for transform_type in all_transforms:
    new_ranges = []
    for length in ranges:
        for transform in transform_type:
            if length[1] <= transform.destination_start:
                new_ranges.append(length)
                break
            elif (transform.destination_start >= length[0]
                  and transform.destination_end <= length[1]):
                new_ranges.append((
                    length[0],
                    transform.destination_start,
                    length[2]
                ))
                new_ranges.append((
                    transform.sourse_start,
                    transform.sourse_start + transform.length,
                    length[2] + (transform.destination_start - length[0])
                ))
                length = (
                    transform.destination_end,
                    length[1],
                    length[2] + transform.destination_end - length[0]
                )
            elif (length[0] >= transform.destination_start
                  and length[1] <= transform.destination_end):
                new_ranges.append((
                    transform.sourse_start + (
                            length[0] - transform.destination_start),
                    transform.sourse_start + (
                            length[1] - transform.destination_start),
                    length[2]
                ))
                break
            elif (transform.destination_start < length[1]
                  <= transform.destination_end):
                new_ranges.append((
                    length[0],
                    transform.destination_start,
                    length[2]
                ))
                new_ranges.append((
                    transform.sourse_start,
                    transform.sourse_start + transform.length,
                    length[2] + (transform.destination_start - length[0])
                ))
                break
            elif (transform.destination_start >= length[0]
                  and length[1] >= transform.destination_end):
                new_ranges.append((
                    transform.sourse_start + (
                            length[0] - transform.destination_start),
                    transform.sourse_start + transform.length,
                    length[2]
                ))
                length = (
                    transform.destination_start + transform.length,
                    length[1],
                    length[2] + (transform.destination_start - length[0])
                )
        else:
            new_ranges.append(length)
    else:
        ranges = new_ranges
        ranges.sort()


ranges.sort(key=lambda span: span[2])


def check_span(span):
    for seed in seeds_2:
        if seed[0] <= span[0] < seed[1]:
            return span[2]
        if span[0] <= seed[0] < span[1]:
            return span[2] + (seed[0] - span[0])


for length in ranges:
    answer_2 = check_span(length)
    if answer_2:
        break

print(time.time() - start)
print(answer, answer_2)
