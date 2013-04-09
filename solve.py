from timeit import timeit

i = input('\nSolve which problem?\n')
while i[0] != 'q' and i[0] != 'Q' and i[0] != 'e' and i[0] != 'E':
    print(timeit(
        'from euler' + i +
        ' import answer; print("\\nAnswer\\n" + str(answer) + "\\n\\nTime")',
        number=1), '\n')
    i = input('Solve which problem?\n')
