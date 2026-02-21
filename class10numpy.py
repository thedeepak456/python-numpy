# Shape of an Array
# The shape of an array is the number of elements in each dimension.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]])
arr2 = np.array([1, 2, 3, 4], ndmin=5)

print(arr.shape)
print(arr1.shape)
print(arr2.shape)

