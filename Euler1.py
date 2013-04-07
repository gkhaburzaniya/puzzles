target, divisor1, divisor2 = 1000, 3, 5

answer = sum(i for i in range(target)
             if i % divisor1 == 0 or i % divisor2 == 0)
print(answer)
