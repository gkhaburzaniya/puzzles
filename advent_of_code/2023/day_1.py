import math

puzzle_input = open("inputs/day_1.txt")

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

DIGITS_2 = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5",
            "six", "6", "seven", "7", "eight", "8", "nine", "9"]

translate = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}

total = 0
total_2 = 0


def solve(digits, problem):
    first_digit = "0"
    second_digit = "0"
    first_digit_pos = math.inf
    second_digit_pos = math.inf
    for digit in digits:
        current_pos = problem.find(digit)
        if current_pos != -1 and current_pos < first_digit_pos:
            first_digit = digit
            first_digit_pos = current_pos

        current_pos = problem[::-1].find(digit[::-1])
        if current_pos != -1 and current_pos < second_digit_pos:
            second_digit = digit
            second_digit_pos = current_pos
    if not first_digit.isdigit():
        first_digit = translate[first_digit]
    if not second_digit.isdigit():
        second_digit = translate[second_digit]
    return int(first_digit + second_digit)


for line in puzzle_input:
    total += solve(DIGITS, line)
    total_2 += solve(DIGITS_2, line)


print(total, total_2)
