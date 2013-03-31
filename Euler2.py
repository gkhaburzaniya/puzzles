if True:
    target = 4000000

    answer, n1, n2 = 0, 1, 1
    while n2 < target:
        n1, n2 = n2, n1 + n2
        if n1 % 2 == 0:
            answer += n1
    print(answer)
    input('Press ENTER')
