import numpy as np


n = int(input())
arr = np.zeros((n,n), dtype=np.uint8)
for i in range(n):
    for j in range(n):
        arr[i][j] = 1
        print(arr[i][j], end='')
    print('\n')