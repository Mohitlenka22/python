import numpy as np

k = list(map(int, input().split()))
arr = np.array(k)
index = np.where(arr == 90)
print(*index)
condition = arr == 90
indexes = np.extract(condition, arr)
print(indexes)
count_arr = np.bincount(arr)
print(f'The count of 90: {count_arr[90]}')



