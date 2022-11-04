import numpy as np

def b():
    matrix = np.arange(9).reshape(3, 3)
    print(*matrix)
    x, y = np.linalg.eig(matrix)
    print(type(x))
    print(type(y))
