import itertools

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
        for word in words:
            if word.isdigit():
                seeds.append(int(word))
        for i, word in enumerate(words[1:]):
            if i % 2 == 0:
                start = int(word)
            else:
                seeds_2.append((start, start + int(word)))
    elif heading == "seed-to-soil":
        transform(line.split(), soils, seeds)
        soils_2.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "soil-to-fertilizer":
        transform(line.split(), fertilizers, soils)
        fertilizers_2.append(
            Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "fertilizer-to-water":
        transform(line.split(), waters, fertilizers)
        waters_2.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "water-to-light":
        transform(line.split(), lights, waters)
        lights_2.append(Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "light-to-temperature":
        transform(line.split(), temperatures, lights)
        temperatures_2.append(
            Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "temperature-to-humidity":
        transform(line.split(), humidities, temperatures)
        humidities_2.append(
            Transform(int(words[0]), int(words[1]), int(words[2])))
    elif heading == "humidity-to-location":
        transform(line.split(), locations, humidities)
        locations.extend(humidities)

        locations_2.append(
            Transform(int(words[0]), int(words[1]), int(words[2])))


answer = min(locations)

for i, transform_type in enumerate(all_transforms):
    all_transforms[i] = sorted(transform_type)


# def check_num(num):
#     i = num
#     for transform_type in all_transforms:
#         for transform in transform_type:
#             if i < transform.destination_start:
#                 break
#             if transform.destination_start <= i < transform.destination_start + transform.length:
#                 i = i - transform.destination_start + transform.sourse_start
#                 break
#     for seed in seeds_2:
#         if seed[0] <= i < seed[1]:
#             return num
#
#
# for j in itertools.count():
#     if check_num(j):
#         answer_2 = j
#         break

# ranges = []
# num = 0
# for transform in locations_2:
#     ranges.append((num, transform.destination_start, num))
#     ranges.append((transform.destination_start,
#                    transform.destination_start + transform.length,
#                    transform.destination_start))
#     num = transform.destination_start + transform.length
#
#
# def final_ranges(ranges):
#     for transform_type in all_transforms:
#         new_ranges = []
#         for transform in transform_type:
#             for length in ranges:
#                 if length[1] < transform.destination_start or length[0] >= transform.destination_start + transform.length:
#                     new_ranges.append(length)
#                 elif transform.destination_start > length[0] and transform.destination_start + transform.length <= length[1]:
#                     new_ranges.append((length[0], transform.destination_start, length[2]))
#                     new_ranges.append((transform.sourse_start, transform.sourse_start + transform.length, length[2] + (transform.destination_start - length[0])))
#                     new_ranges.append((transform.destination_start + transform.length, length[1], length[2] + (transform.destination_start - length[0]) + transform.length))
#                 elif length[0] >= transform.destination_start and length[1] < transform.destination_start + transform.length:
#                     new_ranges.append((transform.sourse_start + (length[0] - transform.destination_start), transform.sourse_start + (length[1] - transform.destination_start), length[2]))
#                 elif transform.destination_start <= length[1] < transform.destination_start + transform.length:
#                     new_ranges.append((length[0], transform.destination_start, length[2]))
#                     new_ranges.append((transform.sourse_start, transform.sourse_start + transform.length, length[2] + (transform.destination_start - length[0])))
#                 elif transform.destination_start >= length[0] and length[1] > transform.destination_start + transform.length:
#                     new_ranges.append((transform.sourse_start + (length[0] - transform.destination_start), transform.sourse_start + transform.length, length[2]))
#                     new_ranges.append((transform.destination_start + transform.length, length[1], length[2] + (transform.destination_start - length[0])))
#
#         else:
#             ranges = new_ranges
#             ranges.sort()
#     return ranges
#
#
# ranges = final_ranges(ranges)
# ranges.sort(key=lambda length: length[2])
#
#
# def check_lengths(length):
#     for seed in seeds_2:
#         if (
#                 (seed[0] <= length[0] < seed[1])
#                 or (seed[0] <= length[1] < seed[1])
#                 or (length[0] < seed[0] and length[1] > seed[1])
#         ):
#             return length
#
#
# for length in ranges:
#     if check_lengths(length):
#         answer_2 = length
#         break

print(answer)
