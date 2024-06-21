puzzle_input = open("inputs/day_15.txt").read()

INSERT = "="


def find_hash(step):
    value = 0
    for char in step:
        value = ((value + ord(char)) * 17) % 256
    return value


answer = 0
for item in puzzle_input.strip().split(","):
    answer += find_hash(item)

    boxes = [[] for _ in range(256)]
    if INSERT in item:
        label, focal_length = item.split(INSERT)
        focal_length = int(focal_length)
        box = boxes[find_hash(label)]
        try:
            box_labels = [label for label, _ in box]
            box[box_labels.index(label)] = (label, focal_length)
        except ValueError:
            box.append((label, focal_length))
    else:
        label = item[:-1]
        box = boxes[find_hash(label)]
        box_labels = [label for label, _ in box]
        try:
            del box[box_labels.index(label)]
        except ValueError:
            pass

print(answer)
