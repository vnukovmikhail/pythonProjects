from random import randrange

def CreateMatrix(x, y):
    createdMatrix = []
    for r in range(x):
        createdMatrix.append([])
    for r in range(x):
        for c in range(y):
            createdMatrix[r].append(randrange(0, 10))
    return createdMatrix

def DrawMatrix(matrix):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            print(matrix[c][r], end='  ')
        print()

def ReplaceMaxMin(matrix):
    arr = []
    sum = 0
    for row in matrix:
        for el in row:
            sum += el
        arr.append(sum)
        sum = 0
    print(arr)
    print('-------')
    rem = matrix[arr.index(min(arr))]
    matrix[arr.index(min(arr))] = matrix[arr.index(max(arr))]
    matrix[arr.index(max(arr))] = rem
    return matrix


matrix = CreateMatrix(3, 3)
DrawMatrix(matrix)
matrix = ReplaceMaxMin(matrix)
DrawMatrix(matrix)