from math import sqrt
def is_prime(n):
    """When passed a number returns True if it is prime, False if not."""
    if n < 2 or n - round(n) != 0:
        print('Numbers smaller than 2 and non-integers are never prime.')
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
    """When passed a list returns the least common multiple of that list."""
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
    """When passed a number returns its smallest prime factor."""
    if n < 2 or n - round(n) != 0:
        print('Numbers smaller than 2 and non-integers do not have prime',
              'factors')
        return None
    for i in range(2, int(sqrt(n) + 2)):
        if n % i == 0 and is_prime(i):
            return i
    return n

def primes_below(n):
    """When passed a number returns a list of all prime numbers < n"""
    L, M = [2], [x for x in range(3, n, 2)]
    if n <= 2:
        print('There are no primes below 2')
        return None
    for i in range(3, n, 2):
        if M[i // 2 - 1] != 0 and is_prime(i):
            L.append(i)
            for j in range(i, n, 2 * i):
                M[j // 2 - 1] = 0
    return L

def prime_factors(n):
    """When passed a number returns a list of all its prime factors"""
    if n < 2 or n - round(n) != 0:
        print('Numbers smaller than 2 and non-integers do not have prime',
              'factors')
    L = []
    while n >= 2:
        i = low_prime(n)
        L.append(i)
        n //= i
    return L
