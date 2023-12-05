puzzle_input = open("day_5_input.txt")

heading = "seeds"
seeds = []
soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []


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

    if heading == "seeds":
        for word in line.split():
            if word.isdigit():
                seeds.append(int(word))
    elif heading == "seed-to-soil":
        transform(line.split(), soils, seeds)
    elif heading == "soil-to-fertilizer":
        transform(line.split(), fertilizers, soils)
    elif heading == "fertilizer-to-water":
        transform(line.split(), waters, fertilizers)
    elif heading == "water-to-light":
        transform(line.split(), lights, waters)
    elif heading == "light-to-temperature":
        transform(line.split(), temperatures, lights)
    elif heading == "temperature-to-humidity":
        transform(line.split(), humidities, temperatures)
    elif heading == "humidity-to-location":
        transform(line.split(), locations, humidities)
        locations.extend(humidities)

print(min(locations))
