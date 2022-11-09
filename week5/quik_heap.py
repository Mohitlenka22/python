import numpy as np

arr = np.array([[1, 7, 4],
                [0, 1, 8],
                [9, 16, 10]
                ])
print(np.sort(arr, kind='quicksort', axis=0))
print(np.sort(arr, kind='heapsort', axis=1))