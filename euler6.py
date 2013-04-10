"""Solve problem 6 of Project Euler and store the answer in answer."""
target = 100
square_of_sum = sum(range(1, target + 1))**2
squares = []
for i in range(1, target + 1):
    squares.append(i**2)
sum_of_squares = sum(squares)
answer = square_of_sum - sum_of_squares
