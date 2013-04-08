target = 1000000

maxlength = 1
D = {1:1}
for i in range(2, target):
    length = 0
    n = i
    while n not in D:
        length += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    D[i] = length = length + D[n]
    if length > maxlength:
        maxlength = length
        answer = i
print(answer)
