target, div1, div2 = 1000, 3, 5
answer = sum(i for i in range(target) if i % div1 == 0 or i % div2 == 0)
print(answer)
