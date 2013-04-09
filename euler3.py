from primes import is_prime, low_prime

target = 600851475143
temp = target
while not is_prime(temp):
    temp //= low_prime(temp)
answer = temp
