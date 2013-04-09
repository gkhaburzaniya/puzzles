target = 1000000
maxlength, D = 1, {1:1}
for i in range(2, target):
    length, n = 0, i
    while n not in D:
        length += 1
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
    D[i] = length = length + D[n]
    if length > maxlength:
        maxlength = length
        temp = i
answer = temp
