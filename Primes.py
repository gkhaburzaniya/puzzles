from math import sqrt
def is_prime(n):
    """Returns True if passed integer is a prime. False otherwise."""
    if n < 2:
        #Integers smaller than 2 are not prime.
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)+2), 2):
        if n % i == 0:
            return False
    return True

def lcm(L):
    """Returns least common multiple of passed list."""
    lcm, M = 1, []
    for i in L:
        for j in M:
            if i % j == 0:
                i //= j
        while i > 1:
            lcm *= low_prime(i)
            M.append(low_prime(i))
            i //= low_prime(i)
    return lcm

def low_prime(n):
    """Returns smallest prime factor of passed integer."""
    if n < 2:
        #Integers smaller than 2 do not have prime factors
        return None
    for i in range(2, int(sqrt(n) + 2)):
        if n % i == 0 and is_prime(i):
            return i
    return n

def primes_below(n):
    """Returns a list of all prime numbers below passed integer."""
    L, M = [2], [x for x in range(3, n, 2)]
    if n <= 2:
        #There are no primes below 2
        return None
    for i in range(3, n, 2):
        if M[i // 2 - 1] != 0 and is_prime(i):
            L.append(i)
            for j in range(i, n, 2 * i):
                M[j // 2 - 1] = 0
    return L

def prime_factors(n):
    """Returns a list of all prime factors of passed integer."""
    #Integers smaller than 2 and non-integers do not have prime factors
    L = []
    while n >= 2:
        i = low_prime(n)
        L.append(i)
        n //= i
    return L
