import numpy
import numpy as np

def roots(matrix):
    n = matrix.shape[0]
    m = 0
    for i in range(n):
        for j in range(i + 1, n):
            if(matrix[i][i] != 0):
                matrix[j] -= matrix[i] * (matrix[j][i] / matrix[i][i])
        
    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            if matrix[i][i] != 0:
                matrix[k] -= matrix[i] * (matrix[k][i] / matrix[i][i])
    for i in range(n):
        if( matrix[i][i] != 0):
            matrix[i] /= matrix[i][i]
    return matrix


N,M = map(int,input().split())
matrix = np.zeros((N,M))
for i in range(N):
    matrix[i] = list(map(int,input().split()))
print(roots(matrix))