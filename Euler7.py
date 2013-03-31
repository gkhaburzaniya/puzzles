target = 10001

from Primes import is_prime
i, answer = 0, 1
while(i < target):
    answer += 1
    if is_prime(answer):
        i += 1
print(answer)
