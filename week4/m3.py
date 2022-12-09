import numpy as np

def c():
    v1 = np.array([1, 2, 3])
    v2 = np.array([5, 8, 0])
    print(np.inner(v1, v2))
    print(np.outer(v1, v2))
    print(np.dot(v1, v2))
    print(np.cross(v1, v2))
    a = np.exp(v1)
    print(a)

c()
