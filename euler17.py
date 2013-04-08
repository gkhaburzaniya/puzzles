target = 1000
temp = 0
for i in range (1, target + 1):
    digits = [int(x) for x in str(i)]
    digits.reverse()
    digits = list(enumerate(digits))

    if i == 1000:
        temp += len('thousand')
    elif i >= 100:
        temp += len('hundred')
        if digits[0][1] != 0 or digits[1][1] != 0:
            temp += len('and')
    if i >= 10 and digits[1][1] == 1:
        if digits[0][1] == 0:
            temp += len('ten')
        elif digits[0][1] == 1:
            temp += len('eleven')
        elif digits[0][1] == 2:
            temp += len('twelve')
        elif digits[0][1] == 3:
            temp += len('thirteen')
        elif digits[0][1] == 4:
            temp += len('fourteen')
        elif digits[0][1] == 5:
            temp += len('fifteen')
        elif digits[0][1] == 6:
            temp += len('sixteen')
        elif digits[0][1] == 7:
            temp += len('seventeen')
        elif digits[0][1] == 8:
            temp += len('eighteen')
        elif digits[0][1] == 9:
            temp += len('nineteen')
    for j in digits:
        if j[0] >= 2 or len(digits) < 2 or (j[0] != 1 and digits[1][1] != 1):
            if j[1] == 1:
                temp += len('one')
            elif j[1] == 2:
                temp += len('two')
            elif j[1] == 3:
                temp += len('three')
            elif j[1] == 4:
                temp += len('four')
            elif j[1] == 5:
                temp += len('five')
            elif j[1] == 6:
                temp += len('six')
            elif j[1] == 7:
                temp += len('seven')
            elif j[1] == 8:
                temp += len('eight')
            elif j[1] == 9:
                temp += len('nine')
        elif digits[1][1] != 1:
            if j[1] == 2:
                temp += len('twenty')
            elif j[1] == 3:
                temp += len('thirty')
            elif j[1] == 4:
                temp += len('forty')
            elif j[1] == 5:
                temp += len('fifty')
            elif j[1] == 6:
                temp += len('sixty')
            elif j[1] == 7:
                temp += len('seventy')
            elif j[1] == 8:
                temp += len('eighty')
            elif j[1] == 9:
                temp += len('ninety')
answer = temp
print(answer)
