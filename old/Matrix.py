def CreateMatrix(x, y):
    createdMatrix = []
    i = 0
    for r in range(x):
        createdMatrix.append([])
    for r in range(x):
        for c in range(y):
            createdMatrix[r].append(i%10) #c for reverse
            i+=1
    return createdMatrix
def DrawMatrix(matrix):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            print(matrix[c][r], end='  ')
        print()
def SumMatrix(matrix):
    sum = 0
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            sum += matrix[c][r]
    return sum
def ElementCountMatrix(matrix):
    return len(matrix) * len(matrix[0])
def ArithmeticMatrix(matrix):
    return '{:.2f}'.format(SumMatrix(matrix) / ElementCountMatrix(matrix))
def MaxMatrix(matrix):
    max = 0
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            if matrix[c][r] > max:
                max = matrix[c][r]
    return max
def MinMatrix(matrix):
    min = 0
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            if matrix[c][r] < min:
                min = matrix[c][r]
    return min
def GetFirst(matrix):
    return matrix[0][0]
def GetLast(matrix):
    return matrix[-1][-1]
def ArrayList(matrix):
    arr = []
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            arr.append(matrix[c][r])
    arr.sort()
    return list(dict.fromkeys(arr))
def Search(matrix, find):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            if matrix[c][r] == find:
                return True
    return False
def BobbleSort(matrix):
    # arr = []
    # for c in range(len(matrix)):
    #     for r in range(len(matrix[c])):
    #         arr.append(matrix[c][r])
    # for i in range(len(arr) - 1):
    #     for j in range(0, len(arr) - 1 - i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr

    arr = [matrix[c][r] for c in range(len(matrix)) for r in range(len(matrix[c]))]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


matrix = CreateMatrix(5, 5)
DrawMatrix(matrix)
print('sum of elements equals', SumMatrix(matrix))
print('count of elements equals', ElementCountMatrix(matrix))
print('arithmetic mean equals', ArithmeticMatrix(matrix))
print('maximal element of matrix is', MaxMatrix(matrix))
print('minimal element of matrix is', MinMatrix(matrix))
print(matrix)
print('first element is', GetFirst(matrix))
print('last element is', GetLast(matrix))
print('sorted elements are', ArrayList(matrix))
print(Search(matrix, 11))
print(BobbleSort(matrix))