from math import sqrt

def is_prime(n):
    """Return True if passed integer is a prime. False otherwise."""
    if n < 2:
        #Integers smaller than 2 are not prime.
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, round(sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

def lcm(numbers):
    """Return least common multiple of passed list."""
    lcm, m = 1, []
    for i in numbers:
        for j in m:
            if i%j == 0:
                i //= j
        while i > 1:
            lcm *= low_prime(i)
            m.append(low_prime(i))
            i //= low_prime(i)
    return lcm

def low_prime(n):
    """Return smallest prime factor of passed integer."""
    if n < 2:
        #Integers smaller than 2 do not have prime factors.
        return None
    if n%2 == 0:
        return 2
    for i in range(3, round(sqrt(n)) + 1, 2):
        if n%i == 0 and is_prime(i):
            return i
    return n

def primes_below(n):
    """Return a list of all prime numbers below passed integer."""
    primes, m = [2], [x for x in range(n)]
    if n <= 2:
        #There are no primes below 2.
        return []
    for i in range(3, n, 2):
        if m[i] != 0 and is_prime(i):
            primes.append(i)
            for j in range(i, n, i):
                m[j] = 0
    return primes

def prime_factors(n):
    """Return a list of all prime factors of passed integer."""
    #Integers smaller than 2 do not have prime factors.
    primes = []
    while n >= 2:
        i = low_prime(n)
        primes.append(i)
        n //= i
    return primes
