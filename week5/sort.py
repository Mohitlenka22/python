import numpy as np

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr, kind='heapsort'))
# arr = np.array([True, False, True])
# print(np.sort(arr))
new_dtype = [('sName', 'S20'), ('marks', 'i4'), ('section', 'i4')]
values = [('mohit', 100, 3), ('lokesh', 120, 1), ('Guna sekhar', 111, 2)]
a = np.array(values, dtype=new_dtype)
print(np.sort(a, order='marks'))
print(np.sort(a, order='section'))