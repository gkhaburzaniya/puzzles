target = 999
temp = 0
for i in range(target, 0, -1):
    for j in range(target, 0, -1):
        k = i * j
        kstr = str(k)
        for m in range(len(kstr)):
            if kstr[m] != kstr[-(m + 1)]:
                break
        else:
            if k > temp:
                temp = k
                lowest = min(i, j)
            break
    if i < lowest:
        break
answer = temp
print(answer)
