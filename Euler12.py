if True:
    target = 500
    
    from Primes import prime_factors
    answer, divisors, i = 0, 0, 1
    while divisors <= target:
        answer += i
        i += 1
        divisors = 0
        L = prime_factors(answer)
        for j in range(len(L)):
            if j == 0:
                divisors += 1
                increase = 1
            elif L[j] == L[j - 1]:
                divisors += increase
            elif L[j] != L[j - 1]:
                divisors, increase = 2 * divisors + 1, divisors + 1
        divisors += 1
    print(answer)
    raw_input("Press ENTER")
