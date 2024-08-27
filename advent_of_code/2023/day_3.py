#!/usr/bin/python3.12

import time

from dataclasses import dataclass

start = time.time()

puzzle_input = open("inputs/day_3.txt")


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


@dataclass
class LinesAndNums:
    lines = ["", "", ""]
    nums = [[], [], []]


answer = 0
answer_2 = 0


def solve(new_line, lines, nums):
    lines[0] = lines[1]
    nums[0] = nums[1]
    lines[1] = lines[2]
    nums[1] = nums[2]
    lines[2] = new_line.strip()
    nums[2] = find_nums(lines[2])
    total_2 = 0

    char_positions = [i for i, char in enumerate(lines[1])
                      if char == "*"]
    for position in char_positions:
        adjacent_nums = []
        for num in nums[0] + nums[1] + nums[2]:
            if num.adjacent([position]):
                adjacent_nums.append(num)
        if len(adjacent_nums) == 2:
            total_2 += adjacent_nums[0].num * adjacent_nums[1].num
    total = process_line(nums[0], nums[1], lines[1], nums[2])
    return total, total_2


for line in puzzle_input:
    totals = solve(line, LinesAndNums.lines, LinesAndNums.nums)
    answer += totals[0]
    answer_2 += totals[1]

totals = solve("", LinesAndNums.lines, LinesAndNums.nums)
answer += totals[0]
answer_2 += totals[1]

print(time.time() - start)
print(answer, answer_2)
