if True:
    target, divisor1, divisor2 = 1000, 3, 5

    answer = 0
    for i in range(target):
        if i % divisor1 == 0 or i % divisor2 == 0:
            answer += i
    print(answer)
    input("Press ENTER")
