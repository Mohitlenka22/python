import numpy as np

def c():
    v1 = np.array([1, 2, 3])
    v2 = np.array([5, 8, 0])
    print(np.inner(v1, v2))
    print(np.outer(v1, v2))
    print(np.dot(v1, v2))

    m1 = np.array([[1, 9, 4],
                  [2, 4, 9],
                   [1, 2, 3]])
    m2 = np.array([[2, 0, 34],
                   [1, 2, 4],
                   [1, 1, 0]])

    print(np.inner(m1, m2))
    print((np.outer(m1, m2)))
    print(np.dot(m1, m2))

    a = np.array([1, 2])
    b = np.array([3, 6])
    print(np.cross(a, b))

    print(np.prod([m1, m2]))
    a = np.exp(m1)
    print(a)
    print(m1.T)
    print(m1.transpose())

