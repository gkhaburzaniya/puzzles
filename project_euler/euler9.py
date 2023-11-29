"""Solve problem 9 of Project Euler and store the answer in answer."""
target = 1000
temp = 0
for a in range (1, target):
    for b in range (1, target):
        c = target - a - b
        if a**2 + b**2 == c**2:
            temp = a*b*c
            break
    if temp != 0:
        break
answer = temp
