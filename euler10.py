"""Solve problem 10 of Project Euler and store the answer in answer."""
from primes import primes_below

target = 2000000
answer = sum(primes_below(target))
