"""Solve problem 2 of Project Euler and store the answer in answer."""
target = 4000000
temp, n1, n2 = 0, 1, 1
while n2 < target:
    n1, n2 = n2, n1 + n2
    if n1%2 == 0:
        temp += n1
answer = temp
