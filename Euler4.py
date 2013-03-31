if True:
    target = 999
    
    answer = lowest = 0
    for i in range(target, 0, -1):
        for j in range(target, 0, -1):
            k = i * j
            kstr = str(k)
            for m in range(len(kstr)):
                if kstr[m] != kstr[-(m + 1)]:
                    break
            else:
                if k > answer:
                    answer = k
                    lowest = min(i, j)
                break
        if i < lowest:
            break
    print(answer)
    input("Press ENTER")