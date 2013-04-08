from timeit import timeit

i = input("Which problem do you want to test?")
print(timeit('import euler' + str(i), number = 1))
