import numpy as np

arr = np.array([[1, 2, 3],
              [1, 0, 3],
              [2, 4, 5]])
def a():
    print(np.linalg.matrix_rank(arr))
    print(np.linalg.det(arr))
    print(np.trace(arr))