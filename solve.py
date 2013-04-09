from timeit import timeit

i = input('\nSolve which problem?\n')
while i is not 'q':
    print(timeit(
        'from euler' + i +
        ' import answer; print("\\nAnswer\\n" + str(answer) + "\\n\\nTime")',
        number=1), '\n')
    i = input('Solve which problem?\n')
