import math

puzzle_input = open("day_1_input.txt")

digits = ["one", "1", "two", "2", "three", "3", "four", "4", "five", "5",
          "six", "6", "seven", "7", "eight", "8", "nine", "9"]

translate = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}

total = 0


for line in puzzle_input:
    first_digit = "0"
    second_digit = "0"
    first_digit_pos = math.inf
    second_digit_pos = math.inf
    for digit in digits:
        current_pos = line.find(digit)
        if current_pos != -1 and current_pos < first_digit_pos:
            first_digit = digit
            first_digit_pos = current_pos

        current_pos = line[::-1].find(digit[::-1])
        if current_pos != -1 and current_pos < second_digit_pos:
            second_digit = digit
            second_digit_pos = current_pos
    if not first_digit.isdigit():
        first_digit = translate[first_digit]
    if not second_digit.isdigit():
        second_digit = translate[second_digit]
    total += int(first_digit + second_digit)


print(total)
