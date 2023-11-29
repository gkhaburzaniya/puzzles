"""Solve problem 16 of Project Euler and store the answer in answer."""
target = 1000
number = 2**target
digits = [int(x) for x in str(number)]
answer = sum(digits)
