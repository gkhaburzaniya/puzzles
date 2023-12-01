import math

puzzle_input = open("day_1_input.txt")

digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
          "six": "6", "seven": "7", "eight": "8", "nine": "9"}

total = 0


def first_spelled_digit(string):
    digit_start = math.inf
    spelled_digit = None
    for digit in digits.keys():
        current_digit_start = string.find(digit)
        if 0 <= current_digit_start < digit_start:
            digit_start = current_digit_start
            spelled_digit = digits[digit]
    return spelled_digit


def last_spelled_digit(string):
    digit_start = 0
    spelled_digit = None
    for digit in digits.keys():
        current_digit_start = string.find(digit)
        if current_digit_start >= digit_start:
            digit_start = current_digit_start
            spelled_digit = digits[digit]
    return spelled_digit


for line in puzzle_input:
    num = ""
    for i, char in enumerate(line):
        if char.isdigit():
            num += first_spelled_digit(line[:i]) or char
            break
    else:
        num += first_spelled_digit(line)

    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            num += last_spelled_digit(line[-i:]) or char
            break
    else:
        num += last_spelled_digit(line)
    total += int(num)

print(total)
