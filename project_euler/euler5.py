"""Solve problem 5 of Project Euler and store the answer in answer."""
from primes import lcm

target = 20
answer = lcm(range(1, target + 1))
