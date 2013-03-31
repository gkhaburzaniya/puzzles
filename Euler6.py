if True:
    target = 100
    
    squareofsum = sum(range(1, target + 1))**2
    L = []
    for i in range(1, target + 1):
        L.append(i**2)
    sumofsquares = sum(L)
    answer = squareofsum - sumofsquares
    print(answer)
    raw_input("Press ENTER")