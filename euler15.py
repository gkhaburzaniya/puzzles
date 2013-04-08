target = 20

from matrix import matrix
M = matrix(target + 1, target + 1, 1)
for i in range(1, target + 1):
    for j in range(1, target + 1):
        M[i][j] = M[i - 1][j] + M[i][j - 1]
answer = M[target][target]
print(answer)
