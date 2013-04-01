target = 20

matrix = [[1 for x in range(target + 1)] for x in range(target + 1)]
for i in range(1, target + 1):
    for j in range(1, target + 1):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
answer = matrix[target][target]
print(answer)
