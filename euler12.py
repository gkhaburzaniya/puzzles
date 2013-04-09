from primes import prime_factors

target = 500
temp, divisors, i = 0, 0, 1
while divisors <= target:
    temp += i
    i += 1
    divisors, factors = 0, prime_factors(temp)
    for j in range(len(factors)):
        if j == 0:
            divisors += 1
            increase = 1
        elif factors[j] == factors[j - 1]:
            divisors += increase
        elif factors[j] != factors[j - 1]:
            divisors, increase = 2*divisors + 1, divisors + 1
    divisors += 1
answer = temp
