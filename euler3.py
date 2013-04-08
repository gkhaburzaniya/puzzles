from primes import is_prime, low_prime

target = 600851475143
while True:
    if is_prime(target):
        answer = target
        break
    target //= low_prime(target)
print(answer)
