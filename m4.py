import numpy as np

def d():
    a = np.array([[1, 2],
                 [3, 5]])
    b = np.array([1, 0])
    print(np.linalg.solve(a, b))