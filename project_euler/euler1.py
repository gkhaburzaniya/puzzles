"""Solve problem 1 of Project Euler and store the answer in answer."""
target = 1000
answer = sum(i for i in range(target) if i%3 == 0 or i%5 == 0)
