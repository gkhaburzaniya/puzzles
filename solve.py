from timeit import timeit

print(timeit(
        'from euler' + input('Solve which problem?') +
        ' import answer; print("\\nAnswer\\n" + str(answer) + "\\n\\nTime")',
        number=1), '\n')
