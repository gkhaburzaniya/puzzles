target = 1000

answer = 0
for i in range (1, target + 1):
    L = [int(x) for x in str(i)]
    L.reverse()
    L = list(enumerate(L))

    if i == 1000:
        answer += len('thousand')
    elif i >= 100:
        answer += len('hundred')
        if L[0][1] != 0 or L[1][1] != 0:
            answer += len('and')
    if i >= 10 and L[1][1] == 1:
        if L[0][1] == 0:
            answer += len('ten')
        elif L[0][1] == 1:
            answer += len('eleven')
        elif L[0][1] == 2:
            answer += len('twelve')
        elif L[0][1] == 3:
            answer += len('thirteen')
        elif L[0][1] == 4:
            answer += len('fourteen')
        elif L[0][1] == 5:
            answer += len('fifteen')
        elif L[0][1] == 6:
            answer += len('sixteen')
        elif L[0][1] == 7:
            answer += len('seventeen')
        elif L[0][1] == 8:
            answer += len('eighteen')
        elif L[0][1] == 9:
            answer += len('nineteen')
    for j in L:
        if j[0] >= 2 or len(L) < 2 or (j[0] != 1 and L[1][1] != 1):
            if j[1] == 1:
                answer += len('one')
            elif j[1] == 2:
                answer += len('two')
            elif j[1] == 3:
                answer += len('three')
            elif j[1] == 4:
                answer += len('four')
            elif j[1] == 5:
                answer += len('five')
            elif j[1] == 6:
                answer += len('six')
            elif j[1] == 7:
                answer += len('seven')
            elif j[1] == 8:
                answer += len('eight')
            elif j[1] == 9:
                answer += len('nine')
        elif L[1][1] != 1:
            if j[1] == 2:
                answer += len('twenty')
            elif j[1] == 3:
                answer += len('thirty')
            elif j[1] == 4:
                answer += len('forty')
            elif j[1] == 5:
                answer += len('fifty')
            elif j[1] == 6:
                answer += len('sixty')
            elif j[1] == 7:
                answer += len('seventy')
            elif j[1] == 8:
                answer += len('eighty')
            elif j[1] == 9:
                answer += len('ninety')
print(answer)
