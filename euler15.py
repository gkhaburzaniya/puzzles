from matrix import matrix

target = 20
m = matrix(target + 1, target + 1, 1)
for i in range(1, target + 1):
    for j in range(1, target + 1):
        m[i][j] = m[i - 1][j] + m[i][j - 1]
answer = m[target][target]
