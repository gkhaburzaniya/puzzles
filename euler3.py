from primes import is_prime, low_prime

target = 600851475143
while not is_prime(target):
    target //= low_prime(target)
answer = target
print(answer)
