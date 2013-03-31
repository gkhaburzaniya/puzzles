if True:
    target = 1000
    
    answer = 0
    for a in range (1, target):
        for b in range (1, target):
            c = target - a - b
            if a**2 + b**2 == c**2:
                answer = a * b * c
                break
        if answer != 0:
            break
    print(answer)
    raw_input("Press ENTER")