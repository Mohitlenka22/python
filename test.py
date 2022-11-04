import numpy as np
import sys

'''
a = [1,2,3,4]
# Numpy creating methods
my_arr1 = np.array(a,ndmin=1)
print(my_arr1,my_arr1.dtype)
my_arr2 = np.zeros((2,2))
print(my_arr2)
my_arr3 = np.ones((3,4))
print(my_arr3)
my_arr4 = np.empty((2,2))
print(my_arr4)
# print(sys.getsizeof(1)*len(a),my_arr.itemsize * my_arr.size)
my_arr5 = np.arange(1,15,2) #np.arnage(start,stop,step)
print(my_arr5)
my_arr6 = np.linspace(1,10,10) #linspace(start,stop,total_elements)
print(my_arr6)
my_arr7 = np.full((2,2),23)
print(my_arr7)
'''
m1 = np.array([[1,2,3],
               [1,1,1],
               [2,0,1]])
m2 = np.array([[1,0,0],
               [1,0,1],
               [2,3,4]])
print(m1 * m2)
print(m1.T) # attribute
m1 = m1.transpose() # method
print(m1 * m2)
print(m1 + m2)
print(np.sqrt(m2)) #applies sqrt for every element
print(np.exp(m2)) #applies exponential for every element

m3 = np.arange(0,15,1)
m3 = m3.reshape(5,3)
print(m3)
print(type(m3))
m4 = np.array([1,2,3,4,5])
print(m4.mean())
print(np.median(m4))
print(np.std(m4))
print(np.percentile(m4,75))
print(np.corrcoef(m4))
print(np.cumsum(m4))
print(m4.sum(axis=0))
print(m4.argmax())
print(m4.argmin())
print(m4.argsort())
print(m4.max())
print(m4.min())
print(m4.sort())