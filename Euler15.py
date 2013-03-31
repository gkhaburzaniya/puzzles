target = 20

matrix = []
for i in range(target + 1):
    for j in range(target + 1):
        matrix.append((i, j))
for i in range(target**2):
    S = {(1, 1)}
