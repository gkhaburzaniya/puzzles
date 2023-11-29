"""Solve problem 7 of Project Euler and store the answer in answer."""
from primes import is_prime

target = 10001
i, temp = 0, 1
while(i < target):
    temp += 1
    if is_prime(temp):
        i += 1
answer = temp
