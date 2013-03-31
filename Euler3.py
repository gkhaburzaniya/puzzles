if True:
    target = 600851475143

    from Primes import is_prime, low_prime
    while True:
        if is_prime(target):
            answer = target
            break
        target //= low_prime(target)
    print(answer)
    raw_input('Press ENTER')
