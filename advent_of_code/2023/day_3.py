puzzle_input = open("inputs/day_3_input.txt")


class Num:
    def __init__(self, start, end, num):
        self.start = start
        self.end = end
        self.num = int(num)

    def adjacent(self, char_positions):
        for position in char_positions:
            if self.start - 1 <= position <= self.end + 1:
                return True
        return False

    def __repr__(self):
        return f"{self.start}:{self.end} {self.num}"


def find_nums(third_line):
    third_line_nums = []
    on_num = False
    num = ""
    for i, char in enumerate(third_line):
        if not on_num and char.isdigit():
            on_num = True
            num += char
            num_start = i
        elif on_num and i == (len(third_line) - 1) and char.isdigit():
            num += char
            third_line_nums.append(Num(num_start, i, num))
        elif on_num and char.isdigit():
            num += char
        elif on_num and not char.isdigit():
            third_line_nums.append(Num(num_start, i-1, num))
            num = ""
            on_num = False

    return third_line_nums


def process_line(first_line_nums, middle_line_nums, middle_line,
                 third_line_nums):
    line_total = 0
    char_positions = [i for i, char in enumerate(middle_line)
                      if not char.isdigit() and char != "."]
    nums_to_del = []
    for i, num in enumerate(first_line_nums):
        if num.adjacent(char_positions):
            line_total += num.num
            nums_to_del.append(i)
    for i in reversed(nums_to_del):
        del first_line_nums[i]
    nums_to_del = []
    for i, num in enumerate(middle_line_nums):
        if num.adjacent(char_positions):
            line_total += num.num
            nums_to_del.append(i)
    for i in reversed(nums_to_del):
        del middle_line_nums[i]
    nums_to_del = []
    for i, num in enumerate(third_line_nums):
        if num.adjacent(char_positions):
            line_total += num.num
            nums_to_del.append(i)
    for i in reversed(nums_to_del):
        del third_line_nums[i]
    return line_total


prev_line = ""
prev_line_nums = []
curr_line = ""
curr_line_nums = []
next_line = ""
next_line_nums = []
total = 0


for line in puzzle_input:
    prev_line = curr_line
    prev_line_nums = curr_line_nums
    curr_line = next_line
    curr_line_nums = next_line_nums
    next_line = line.strip()
    next_line_nums = find_nums(next_line)

    total += process_line(prev_line_nums, curr_line_nums, curr_line,
                          next_line_nums)

prev_line = curr_line
prev_line_nums = curr_line_nums
curr_line = next_line
curr_line_nums = next_line_nums
next_line = ""
next_line_nums = find_nums(next_line)

total += process_line(prev_line_nums, curr_line_nums, curr_line,
                      next_line_nums)

print(total)
