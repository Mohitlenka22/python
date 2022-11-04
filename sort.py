import numpy as  np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr, kind='heapsort'))

arr = np.array([True, False, True])
print(np.sort(arr))

d = [('sName', 'S20'), ('marks', 'i4'), ('section', 'i4')]

values = [('jason', 1000, 1), ('json', 456, 3), ('agdjr', 234, 90)]

a = np.array(values, dtype=d)
print(np.sort(a, order='marks'))

