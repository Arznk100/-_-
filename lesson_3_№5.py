import numpy
import numpy as np

M = int(input())
a = np.zeros((M, M))
top = 0
bottom = M - 1
left = 0
right = M - 1
counter = 1
while counter <= M * M:
    for i in range(left, right + 1):
        a[top][i] = counter
        counter += 1
    top += 1

    for i in range(top, bottom + 1):
        a[i][right] = counter
        counter += 1
    right -= 1

    for i in range(right, left - 1, -1):
        a[bottom][i] = counter
        counter += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        a[i][left] = counter
        counter += 1
    left += 1
print(a)

    