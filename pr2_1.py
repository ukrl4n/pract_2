def solveGauss(inMatrix, inVector, dimension=3):
    print(f"solving by gauss method {dimension}x{dimension}...")

    for i in range(dimension):
        inMatrix[i].append(inVector[i])

    for i in range(dimension):
        pivot = inMatrix[i][i]
        inMatrix[i] = [x / pivot for x in inMatrix[i]]
        for j in range(i + 1, dimension):
            factor = inMatrix[j][i]
            inMatrix[j] = [inMatrix[j][k] - factor * inMatrix[i][k] for k in range(dimension + 1)]

    for i in range(dimension - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = inMatrix[j][i]
            inMatrix[j] = [inMatrix[j][k] - factor * inMatrix[i][k] for k in range(dimension + 1)]

    return [row[-1] for row in inMatrix]

print('2v')
inMatrix1 = [[2.50, -0.91, -0.32], [-0.91, 3.64, -0.48], [0.48, -0.98, 2.14]]
inVector1 = [0.287, 5.418, 5.908]
solution1 = solveGauss(inMatrix1, inVector1)
print('Solution:', solution1)

print('7v:')
inMatrix2 = [[2.75, 1.12, -0.6], [1.06, 2.98, -0.86], [-1.18, -1.36, 3.02]]
inVector2 = [3.066, 5.328, 5.790]
solution2 = solveGauss(inMatrix2, inVector2)
print('Solution:', solution2)