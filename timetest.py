from timeit import timeit

n = 14
for i in range (1, n + 1):
    print(timeit('import Euler' + str(i), number = 1))
