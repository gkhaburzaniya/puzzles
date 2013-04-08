target = 4000000
sum, n1, n2 = 0, 1, 1
while n2 < target:
    n1, n2 = n2, n1 + n2
    if n1%2 == 0:
        sum += n1
answer = sum
print(answer)
